"""MIT licensed launcher for the frozen, independently checkable archive.

Run with Python 3.10+: python -I -B verify_snapshot.py
The extracted workspace is kept for inspection. No release file is deleted.
"""
from pathlib import Path
import hashlib,json,os,subprocess,sys,uuid,zipfile

ROOT=Path(__file__).resolve().parent

def main():
    if hasattr(sys.stdout,'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8',errors='backslashreplace')
        sys.stderr.reconfigure(encoding='utf-8',errors='backslashreplace')
    if not __debug__:
        raise RuntimeError("Run without -O: certificate checks use assertions.")
    if sys.version_info < (3,10):
        raise RuntimeError("Python 3.10 or later is required.")
    manifest=ROOT/'SHA256SUMS.txt'
    for line in manifest.read_text(encoding='utf-8').splitlines():
        expected,name=line.split('  ',1)
        target=ROOT/name
        if not target.is_file():
            raise RuntimeError('Missing published file: '+name)
        if hashlib.sha256(target.read_bytes()).hexdigest()!=expected:
            raise RuntimeError('Checksum mismatch: '+name)
    destination=ROOT/'validation'/('snapshot_'+uuid.uuid4().hex[:12])
    destination.mkdir(parents=True,exist_ok=False)
    archive=ROOT/'reproducibility.zip'
    with zipfile.ZipFile(archive) as z:
        for info in z.infolist():
            name=info.filename.replace('\\','/')
            if name.startswith('/') or '..' in Path(name).parts or ':' in name:
                raise RuntimeError('Unexpected archive path: '+name)
        if z.testzip() is not None:
            raise RuntimeError('Archive CRC check failed.')
        z.extractall(destination)
    result=subprocess.run([sys.executable,'-X','utf8','-I','-B','verify.py'],cwd=destination,
        capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=180)
    (destination/'launcher_stdout.txt').write_text(result.stdout,encoding='utf-8')
    (destination/'launcher_stderr.txt').write_text(result.stderr,encoding='utf-8')
    print(result.stdout)
    if result.returncode:
        print(result.stderr,file=sys.stderr)
        raise RuntimeError('Certificate checker failed. Inspect '+str(destination))
    report={'published_checksums_verified':True,'certificate_checker_exit_code':result.returncode,
        'archive_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),
        'workspace':str(destination),'independent_expert_review':False,'formal_verification':False}
    (destination/'launcher_result.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print('Checks passed. Retained workspace:',destination)

if __name__=='__main__':
    main()
