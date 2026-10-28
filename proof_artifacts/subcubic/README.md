# A1: complete finite proof interfaces

From the repository root, run:

```sh
python -I -B proof_artifacts/subcubic/verify.py
```

This uses Python 3.10 or later and its standard library. Do not use `-O`. The checker covers tree/cactus ports, sparse cores, two-marked interfaces, the optional marked-theta data, independent local calculations, and rejection of three intentionally damaged certificates. It independently recalculates the 4,256-case weak-two-marked kernel.

The code and data are byte-identical to their released archive counterparts; the launcher is the archive's `verify_a1.py` under the filename `verify.py`. The resulting finite-data audit supports A1. Its universal structural argument must also be read in the [manuscript](../../paper.pdf).

To check all other families, run `python -I -B verify_snapshot.py` from the repository root. [Verification status](../../VERIFICATION.md) records the scope. Code: MIT; data/documentation: CC BY 4.0.
