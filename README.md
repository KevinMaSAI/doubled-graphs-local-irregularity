# Locally irregular two-edge-colourings of doubled graphs

**Qiyuan Ma · Shanghai Jiao Tong University**  
Contact: [mqyqwerty@sjtu.edu.cn](mailto:mqyqwerty@sjtu.edu.cn) · 28 October 2026  
[中文说明](README_zh.md)

This repository accompanies the research preprint **Locally Irregular Two-Edge-Colourings of Doubled Graphs: Constructions, Extensions, and Obstructions**.

**[Read the paper (PDF)](paper.pdf)** · **[Download the complete reproducibility archive](reproducibility.zip)** · **[Novelty and related work](NOVELTY_AND_RELATED_WORK.md)**

## Mathematical scope

For a finite connected simple graph G other than K2, replace each edge by two parallel copies. The doubled-graph conjecture asks whether the copies can always be coloured red and blue so that adjacent vertices have different degrees in each colour present on their connecting edge. The parallel copies are allowed to have different colours.

The manuscript presents a **computer-assisted proof for all subcubic underlying graphs** (maximum degree at most three), together with conditional constructions for several families of unbounded maximum degree. Two sufficient conditions considered are

- delta(G) >= 8 chi(G) (2 chi(G) + 1) - 7;
- 8 delta(G) >= 7 |V(G)| + 6, with all red vertex degrees distinct and all blue vertex degrees distinct.

Here delta is minimum degree and chi is chromatic number. Further sections concern preserved boundary colours, clique interfaces, prescribed targets, signed-gap constructions and explicit obstructions to stronger proof strategies. The unrestricted conjecture for arbitrary connected graphs **is not proved**.

This is an AI-assisted research preprint. The submitted arguments and finite certificates have undergone internal computational checks; no independent expert peer review or proof-assistant verification is claimed. A bounded graph search alone is not a proof of an infinite-family statement. See [AI assistance](AI_ASSISTANCE.md) and [the literature-screening limits](NOVELTY_AND_RELATED_WORK.md).

## Files

| File | Contents |
|---|---|
| [paper.pdf](paper.pdf) | Complete 64-page English manuscript, including proof and certificate appendices. |
| [reproducibility.zip](reproducibility.zip) | All 697 released files: editable TeX, Python constructors and checkers, JSON certificates, examples, frozen research notes and validation reports. |
| [verify_snapshot.py](verify_snapshot.py) | Standard-library launcher that verifies repository checksums, extracts a new local workspace and runs the archive's complete finite-certificate checker. |
| [SHA256SUMS.txt](SHA256SUMS.txt) | SHA-256 hashes for the published top-level files. |
| [CITATION.cff](CITATION.cff) | Author and citation metadata; no DOI is assigned here. |
| [NOVELTY_AND_RELATED_WORK.md](NOVELTY_AND_RELATED_WORK.md) | Literature comparison, including known special cases and classical tools. |

The archive preserves the exact prepared Zenodo files and their directory layout. Its internal README records the earlier local preparation status. This GitHub repository is a subsequent public deposit; no Zenodo record or DOI has yet been created.

## Verify the finite certificates

Download this repository using **Code → Download ZIP**, extract it, and run from its root with Python 3.10 or later:

```sh
python -I -B verify_snapshot.py
```

No third-party packages, solver, network connection, Lean or account are required for this certificate verification. Do not use Python's `-O` option. The launcher keeps the extracted run and its report in a new `validation/snapshot_*` directory; it does not overwrite the released archive.

Alternatively, extract `reproducibility.zip`, enter the extracted directory and run:

```sh
python -I -B verify.py
```

The checker recomputes complete finite interfaces and the local two-mark kernel, checks saved witnesses by colour-copy degrees, checks additional certificate identities and audits the frozen manifest. These checks certify the specified finite data and implementation properties. The general lifting arguments are in the paper.

## Constructors and editable source

Inside the extracted reproducibility archive:

```sh
python -m pip install -r requirements.txt
python -B run_checks.py
```

The constructive checks use additional dependencies; see the archive's README for supported Python versions, timeouts and scope gates. The A1 entry point is `construct.py`, other constructors and their independent checkers are in `artifact/`, and editable TeX is in `manuscript/`.

Build the paper from that directory with `pdflatex main.tex` twice or `tectonic main.tex`. The source snapshot includes A1–A9, B1–B4, C1–C5, D1–D5 and E1–E4 through 10:25:33 CST on 28 October 2026. Those are provenance groups, not counts of independent new theorems. Later notes are outside this deposit.

## Licence and citation

Manuscript, documentation and JSON certificates: **CC BY 4.0**. Python code, including `verify_snapshot.py`: **MIT**. See [licence scope](LICENSES.md) and the full [CC BY 4.0](LICENSE_CC_BY_4_0.txt) and [MIT](LICENSE_MIT.txt) texts.

Please cite Qiyuan Ma, *Locally Irregular Two-Edge-Colourings of Doubled Graphs: Constructions, Extensions, and Obstructions*, research preprint, 2026. This GitHub deposit does not constitute journal peer review or a historical-priority certificate.
