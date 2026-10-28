#!/usr/bin/env python3
"""Verify the complete finite A1 proof data with Python's standard library.

Run without -O. No NetworkX, solver, network, or external service is used.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import sys
import time

sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'artifact'))

def main():
    if not __debug__:
        raise SystemExit('Verification requires assertions: do not run Python with -O.')
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,help='Optional path for a JSON report')
    args=parser.parse_args()
    from safe_all_cactus_certificate import verify_all_cactus_certificate
    from sparse_bip_core_certificate import verify_certificate as sparse
    from marked_theta_certificate import verify_certificate as theta
    from weak_two_marked_certificate import verify_certificate as weak
    import independent_local_review as fresh
    def read(name):return json.loads((ROOT/'artifact'/name).read_text(encoding='utf-8'))
    start=time.monotonic()
    w=read('weak_two_marked_interfaces.json')
    results={
        'tree_and_cactus':verify_all_cactus_certificate(read('safe_all_cactus_interfaces.json')),
        'sparse_core':sparse(read('sparse_bip_core_interfaces.json')),
        'two_marked':weak(w),
        'optional_marked_theta':theta(read('marked_theta_interfaces.json')),
        'fresh_path_interfaces':fresh.local_paths(),
        'fresh_two_marked_kernel':fresh.kernel(),
        'fresh_mod3_local_rules':fresh.mod3_local(),
    }
    # Verify the odd-cactus standalone table too; it is an actual supplied input.
    from safe_cactus_certificate import verify_certificate as odd
    results['standalone_odd_cactus']=odd(read('safe_cactus_interfaces.json'))
    damaged=[]
    q=copy.deepcopy(w);q['records'].pop();damaged.append(q)
    q=copy.deepcopy(w);q['records'][0]['witness']['left_state'][1]+=1;damaged.append(q)
    q=copy.deepcopy(w);q['branch_types']['m1']=[[0,3]];damaged.append(q)
    for q in damaged:
        try:weak(q)
        except (AssertionError,KeyError):pass
        else:raise AssertionError('A deliberately damaged certificate was accepted.')
    files={p.name:hashlib.sha256(p.read_bytes()).hexdigest()
           for p in sorted((ROOT/'artifact').glob('*.json'))}
    report={'finite_certificate_verification':'PASS','results':results,
            'damaged_certificates_rejected':len(damaged),'certificate_sha256':files,
            'arbitrary_degree_mother_conjecture_proved':False,
            'scope':'Exact finite calculations supporting the subcubic proof; universal structural arguments are in the manuscript',
            'formal_proof_assistant_used':False,'network_access_used':False,
            'python_version':sys.version.split()[0],'seconds':round(time.monotonic()-start,4)}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
