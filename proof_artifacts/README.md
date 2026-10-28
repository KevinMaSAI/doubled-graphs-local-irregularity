# Proof artifacts

This directory exposes the main finite subcubic proof data for direct browsing. The complete frozen research and reproducibility snapshot remains in [reproducibility.zip](../reproducibility.zip), with all 697 released files, constructors, other certificate families, provenance and earlier reports.

## Entry points

| Material | Location | Scope |
|---|---|---|
| Standalone A1 finite checker | [subcubic/verify.py](subcubic/verify.py) | Rechecks the complete supplied A1 finite domains and three deliberately damaged certificates. |
| A1 certificates and verifier modules | [subcubic/artifact/](subcubic/artifact/) | Exact copies of the corresponding files in the frozen archive. |
| Complete snapshot launcher | [verify_snapshot.py](../verify_snapshot.py) | Checks published hashes and runs all standard-library finite and saved-witness checks from the full archive. |
| Verification boundary | [VERIFICATION.md](../VERIFICATION.md) | Separates finite calculations, structural arguments and implementation tests. |

From this repository root, with Python 3.10 or later:

```sh
python -I -B proof_artifacts/subcubic/verify.py
```

For the entire release:

```sh
python -I -B verify_snapshot.py
```

The A1 folder has six standard-library verifier modules and five JSON certificate files. `verify.py` is the unchanged released `verify_a1.py`, placed beside that self-contained artifact subset. The finite checker does not claim to replace the graph reductions and lifting arguments in the manuscript. See the full archive for constructors and the A2–E4 artifacts.

Python code is MIT licensed; JSON certificates and documentation are CC BY 4.0. The full licence texts and scope are in the repository root.
