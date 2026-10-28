# Locally Irregular Two-Edge-Colourings of Doubled Graphs: Constructions, Extensions, and Obstructions

**Qiyuan Ma · Shanghai Jiao Tong University**  
28 October 2026 · [mqyqwerty@sjtu.edu.cn](mailto:mqyqwerty@sjtu.edu.cn)

**[Read the manuscript](paper.pdf)** · **[Editable main source](main.tex)** · **[BibTeX](CITATION.bib)** · **[Finite proof artifacts](../../proof_artifacts/)**

## Abstract and scope

The manuscript presents a computer-assisted proof of the doubled-graph local-irregularity conjecture for all finite connected simple subcubic underlying graphs other than K2, together with further conditional constructions of unbounded maximum degree. It treats short-path interfaces, sparse branch cores, clique capacities, high-minimum-degree and dense regions, prescribed targets, signed-gap constructions and explicit restricted-strategy obstructions. The conjecture for arbitrary connected graphs remains unproved.

## Files and build

`paper.pdf` is the unchanged 64-page manuscript from the initial public deposit. All sixteen TeX source files sit in this directory; `main.tex` includes the sections in order, and `references.bib` records its bibliography. Build from this directory:

```sh
tectonic main.tex
```

Or run `pdflatex main.tex` twice. No shell escape or bibliography processor is required. Building needs an installed TeX distribution and its packages; certificate checking does not.

## Verification and provenance

The finite interfaces have executable checkers and supplied certificates. [Verification status](../../VERIFICATION.md) distinguishes complete finite domains from sampled constructor checks and the universal arguments in the paper. No Lean formalisation or independent expert peer review is claimed. [Novelty screening](../../NOVELTY_AND_RELATED_WORK.md) records related work and the limits of priority claims.

The mathematical source snapshot is fixed at 10:25:33 CST on 28 October 2026. This publication-layout update does not alter the manuscript or its hypotheses. Original versions remain available in [repository history](../../history.md).

## Citation

```bibtex
@misc{Ma2026DoubledGraphs,
  author       = {Qiyuan Ma},
  title        = {Locally Irregular Two-Edge-Colourings of Doubled Graphs:
                  Constructions, Extensions, and Obstructions},
  year         = {2026},
  month        = {October},
  howpublished = {Research preprint},
  url          = {https://github.com/KevinMaSAI/doubled-graphs-local-irregularity/blob/main/preprints/Locally-Irregular-Two-Edge-Colourings-of-Doubled-Graphs-October-28-2026/paper.pdf}
}
```

Manuscript, TeX and documentation: CC BY 4.0. Python code: MIT. Full licence scopes are in [LICENSES.md](../../LICENSES.md). Extensive AI assistance is disclosed in [AI_ASSISTANCE.md](../../AI_ASSISTANCE.md).
