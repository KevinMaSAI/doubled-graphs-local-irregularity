# Locally irregular colourings of doubled graphs

**Qiyuan Ma · Shanghai Jiao Tong University**  
[mqyqwerty@sjtu.edu.cn](mailto:mqyqwerty@sjtu.edu.cn) · [ORCID: 0009-0000-9532-0821](https://orcid.org/0009-0000-9532-0821) · [中文说明](README_zh.md)

This repository contains **one mathematical research preprint and its supporting proof artifacts**, organised as one problem family. It presents a computer-assisted subcubic proof and further conditional constructions for locally irregular two-edge-colourings of doubled graphs.

## Navigating the collection

- Start with the **[research overview (PDF)](overview.pdf)** for a concise statement of the principal result, further constructions and checking boundaries.
- Use the **[manuscript map](CONTENTS.md)** to find results, source files and proof artifacts.
- The **[preprints directory](preprints/)** contains the complete manuscript, editable TeX, build instructions and manuscript-specific BibTeX.
- The **[proof artifacts](proof_artifacts/)** expose the A1 finite certificates and standard-library checkers. The **[complete reproducibility archive](reproducibility.zip)** preserves all 697 released files.
- Read the **[verification status](VERIFICATION.md)** and **[release history](history.md)** for scope and revisions.

## Principal result

Let G be a finite connected simple graph other than K2, and double every original edge. The manuscript presents a locally irregular red/blue edge-colouring construction for **all subcubic underlying graphs**, meaning maximum degree at most three. Parallel copies may have different colours. Along every red edge, its endpoints have distinct red degrees; along every blue edge, their blue degrees are distinct.

Further results give specified unbounded-degree constructions, prescribed interfaces and strategy obstructions. Two sufficient conditions are

$$\delta(G)\ge 8\chi(G)(2\chi(G)+1)-7,$$

and

$$8\delta(G)\ge 7|V(G)|+6.$$

Here delta is minimum degree and chi is chromatic number. The second condition admits red degrees distinct on all vertices and blue degrees distinct on all vertices. The conjecture for **arbitrary connected graphs remains unproved**.

## Verification

| Layer | Status and meaning |
|---|---|
| Manuscript | Complete displayed arguments, including structural reductions and lifting. Research preprint; independent expert peer review is not claimed. |
| Complete finite interfaces | Supplied certificate domains and independent local recalculations pass executable checks. |
| Constructor tests | Documented implementation tests under their stated hypotheses; bounded/random tests are not universal proofs. |
| Lean formalisation | None is included. Python certificates are not proof-assistant formalisation. |

From this repository root, with Python 3.10 or later:

```sh
python -I -B proof_artifacts/subcubic/verify.py
python -I -B verify_snapshot.py
```

These certificate commands need no third-party Python packages, network, solver or account. They do not replace the universal arguments. Constructor dependencies and commands are documented inside the full archive.

## Provenance and related work

OpenAI Codex assisted extensively with mathematical exploration, proof development and checking, programming, literature screening and English exposition. See **[AI assistance](AI_ASSISTANCE.md)**. The manuscript and frozen research notes record the actual release scope; later notes lie outside that snapshot.

The **[novelty and related-work note](NOVELTY_AND_RELATED_WORK.md)** distinguishes candidate contributions, known special cases and classical tools. No absolute historical-priority certificate is claimed. The A1–E4 labels are provenance groups, not a count of independent new theorems.

## Versions and citations

The initial public deposit remains accessible at [commit 07f1f72](https://github.com/KevinMaSAI/doubled-graphs-local-irregularity/tree/07f1f720200384990ef0c26540749c5d191b0e8b). Corrections and revisions are recorded in **[history.md](history.md)**; earlier Git versions remain accessible.

Use the manuscript's **[BibTeX](preprints/Locally-Irregular-Two-Edge-Colourings-of-Doubled-Graphs-October-28-2026/CITATION.bib)** or **[CITATION.cff](CITATION.cff)**. The current paper has no assigned DOI. Zenodo submission has not occurred.

Manuscript, documentation and JSON certificates: **CC BY 4.0**. Python code: **MIT**, by material type. See **[licence scopes](LICENSES.md)**. Publication organisation is inspired by the public [OpenAI mathematics repository](https://github.com/openai/math); the source review is recorded in [LAYOUT_REFERENCE.md](LAYOUT_REFERENCE.md).
