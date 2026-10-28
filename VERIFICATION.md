# Verification status and boundary

| Layer | What is present | What it establishes |
|---|---|---|
| Mathematical manuscript | Complete displayed arguments in the 64-page paper | Structural reductions, hypotheses and lifting arguments must be assessed mathematically. |
| A1 finite data | Five complete certificate files, six verifier modules, and the standalone entry point | Finite interfaces, the 4,256-case weak-two-marked kernel, fresh local calculations and rejection of three corrupted certificates. |
| Other complete data | Full archive, including 836 clique bases and decorated-path data | The specified complete finite domains and supplied witness checks. |
| E1–E4 auditors | Four constructor-independent standard-library programs in the archive | Recount 972 saved colour copies and rederive saved rows, truth tables and parity conditions. |
| Additional endpoint audit | Archive's independent content audit | 1,114 bounded endpoint cases supporting the displayed path argument; bounded checks alone are not an arbitrary-length proof. |
| Constructor regression | Scope-gated implementations and documented tests in the archive | Executions on the tested inputs, not existence for every untested graph. |
| Proof assistant | No Lean or equivalent formalisation is included | No formal-verification claim is made. |
| Independent expert review | Not obtained as part of this release | Internal AI-assisted review is not external peer review. |

## Reproduce

Run from the repository root, with Python 3.10 or later and without `-O`:

```sh
python -I -B proof_artifacts/subcubic/verify.py
python -I -B verify_snapshot.py
```

The first checks the exposed A1 subset. The second verifies published SHA-256 hashes, extracts the unchanged complete archive into a new retained directory and executes its standard-library verification suite. These commands need no network, third-party packages or solver. Constructor tests need additional dependencies listed inside the archive.

The exposed A1 files and editable manuscript sources are exact copies of the frozen release. Newly added catalogue and navigation files change presentation and access only. The original paper and complete ZIP retain their public-deposit hashes.

## Read the proof obligations

For A1, finite calculations enter after the core classification, port-budget and compatibility arguments. Reading only a JSON success report does not check those reductions. The full archive's `PROOF_DEPENDENCIES.md` identifies each classical dependency and local proof obligation. Strategy obstructions in C1–C5 disprove only their specified stronger strategies.

The [novelty note](NOVELTY_AND_RELATED_WORK.md) is literature screening, not a mathematical correctness certificate. For example, ordinary orientation specialisations of the E1 signed-gap theme have relevant prior art, while the full signed statement and its precise applications require their own comparison.
