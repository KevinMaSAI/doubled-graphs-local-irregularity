# Manuscript map

**One manuscript · one problem family · graph theory**

## 001. Locally irregular two-edge-colourings of doubled graphs

**Principal claim:** every finite connected simple subcubic graph other than K2 admits a locally irregular two-edge-colouring after all edges are doubled. The manuscript also develops specified unbounded-degree constructions and interface criteria. The unrestricted doubled-graph conjecture is not proved.

| Manuscript | Materials | Checking scope |
|---|---|---|
| [Locally Irregular Two-Edge-Colourings of Doubled Graphs: Constructions, Extensions, and Obstructions](preprints/Locally-Irregular-Two-Edge-Colourings-of-Doubled-Graphs-October-28-2026/paper.pdf), Qiyuan Ma, 28 October 2026 | [Source/build](preprints/Locally-Irregular-Two-Edge-Colourings-of-Doubled-Graphs-October-28-2026/), [BibTeX](preprints/Locally-Irregular-Two-Edge-Colourings-of-Doubled-Graphs-October-28-2026/CITATION.bib), [full archive](reproducibility.zip) | [Complete finite kernels](proof_artifacts/subcubic/), [verification status](VERIFICATION.md); no Lean formalisation or independent expert peer review is claimed. |

The catalogue number 001 is a local navigation identifier. The groups below all belong to this same manuscript, and are not independent paper or novelty counts.

## Result and source index

| Group | Content | Editable source | Supporting material |
|---|---|---|---|
| A1 | Full subcubic construction, safe ports, two-marked kernel and lifting | [subcubic.tex](preprints/Locally-Irregular-Two-Edge-Colourings-of-Doubled-Graphs-October-28-2026/subcubic.tex), [appendix](preprints/Locally-Irregular-Two-Edge-Colourings-of-Doubled-Graphs-October-28-2026/subcubic_appendix.tex) | [Standalone finite checker](proof_artifacts/subcubic/), complete domains and structural arguments. |
| A2–A6, B1 | Sparse branch cores, homogeneous cores, balanced subdivisions, parity separation, path/tree boundaries | [ports_and_branches.tex](preprints/Locally-Irregular-Two-Edge-Colourings-of-Doubled-Graphs-October-28-2026/ports_and_branches.tex) | Complete interface data and the archive's family-specific constructors. |
| A7–A9 | Clique root targets, block-tree capacity, gluing given colourings | [cliques_and_gluing.tex](preprints/Locally-Irregular-Two-Edge-Colourings-of-Doubled-Graphs-October-28-2026/cliques_and_gluing.tex) | 836 supplied clique bases and the stated capacity/gluing hypotheses. |
| B2, B4 | Fixed-target reductions, factors, normal forms and structural restrictions | [targets_and_reductions.tex](preprints/Locally-Irregular-Two-Edge-Colourings-of-Doubled-Graphs-October-28-2026/targets_and_reductions.tex) | Classical matching/factor tools and problem-specific applications. |
| B3 | Actual-rule polynomial and coefficient identities | [algebra.tex](preprints/Locally-Irregular-Two-Edge-Colourings-of-Doubled-Graphs-October-28-2026/algebra.tex) | Interpolation and permanent methods are classical; particular identities are compared in the novelty note. |
| C1–C5 | Restricted-strategy obstructions, sharp interfaces and repair barriers | [obstructions.tex](preprints/Locally-Irregular-Two-Edge-Colourings-of-Doubled-Graphs-October-28-2026/obstructions.tex) and earlier interface sections | These are not counterexamples to the original conjecture. |
| D1–D2 | High minimum degree relative to chromatic number and CRT-region extensions | [high_degree.tex](preprints/Locally-Irregular-Two-Edge-Colourings-of-Doubled-Graphs-October-28-2026/high_degree.tex) | Explicit thresholds and physical external-contribution hypotheses. |
| D3, D5 | Dense antitone targets, forbidden final degrees and sequential absorption | [dense_regions.tex](preprints/Locally-Irregular-Two-Edge-Colourings-of-Doubled-Graphs-October-28-2026/dense_regions.tex) | Tutte factor inequalities, parity and target-range calculations. |
| D4 | Complement-path lifts and related infinite families | [complements.tex](preprints/Locally-Irregular-Two-Edge-Colourings-of-Doubled-Graphs-October-28-2026/complements.tex) | Explicit seeds, lifts and preservation arguments. |
| E1–E4 | Signed gaps, paired/path-cycle partitions, protected joins and odd-component root ports | [integer_partitions.tex](preprints/Locally-Irregular-Two-Edge-Colourings-of-Doubled-Graphs-October-28-2026/integer_partitions.tex) | Four standard-library auditors; ordinary orientation and parity tools have related prior art. |

For the complete proof-to-code map, extract the full archive and read `COVERAGE.md` and `PROOF_DEPENDENCIES.md`. [Novelty screening](NOVELTY_AND_RELATED_WORK.md) records the literature boundary rather than certifying first priority.
