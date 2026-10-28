# Novelty screening and related work

**Screening date:** 28 October 2026. **Manuscript:** *Locally Irregular Two-Edge-Colourings of Doubled Graphs: Constructions, Extensions, and Obstructions*, Qiyuan Ma. This note concerns the fixed manuscript snapshot through 10:25:33 CST on that date.

## Conclusion and limits

No earlier proof covering the manuscript's full A1 statement was identified in the sources screened. A1 is the strongest candidate for a new theorem: every finite connected simple subcubic graph other than K2 has a locally irregular two-edge-colouring after every edge is doubled. This is a literature-screening conclusion, conditional on the correctness of the submitted proof, not a certification of historical priority or mathematical validity. The unrestricted doubled-graph conjecture is not claimed to be solved.

The inventory labels are not a count of independent new theorems. Some smaller existence statements follow from A1 or from published results. Matching, factor, parity-join, interpolation, degree-choosability and jump-system tools are established mathematics. Any novelty in their use here lies in the particular reductions, interfaces, identities or constructions.

## The closest potentially confusing results

1. Grzelec and Woźniak posed the doubled-graph conjecture in [On decomposing multigraphs into locally irregular submultigraphs](https://arxiv.org/abs/2208.08809). The problem itself is not new. Their [cactus paper](https://arxiv.org/abs/2211.08270) already settles the cactus class.
2. Grzelec, Onderko and Woźniak's [2024 preprint / 2026 paper](https://arxiv.org/abs/2412.04200), [published version](https://doi.org/10.1016/j.amc.2025.129832), proves the conjecture for regular graphs and particular subcubic families, with a three-colour bound for general subcubic graphs. Those statements do not cover all of A1.
3. [Locally Irregular Total Colorings of Graphs](https://arxiv.org/abs/2603.13178) proves a two-colour statement for all subcubic graphs in a different model: vertices also receive colours, and their colour contributes one to the relevant total degree. A1 counts copies of edges only. This difference precludes identifying the two statements or treating the total-colouring theorem alone as a proof of A1; no reduction establishing such an implication was identified.
4. Baudon et al., [A general decomposition theory for the 1-2-3 Conjecture and locally irregular decompositions](https://dmtcs.episciences.org/5334/pdf), Theorem 5.7, proves standard (2,2)-colourability for nicer subcubic graphs. Each original edge has one coloured weight, either one or two. It is not a partition of exactly two copies of every edge into two complementary colour classes. Its conclusion alone does not supply the missing complementary copies in A1.
5. [The irregularity strength of dense graphs](https://arxiv.org/abs/2406.09584) studies one weighting with weights 1,2,3 and all vertex sums distinct. If w=x+1, its sum is R(v)+d(v), rather than R(v). On nonregular graphs, distinct such sums do not by themselves give both distinct R(v) and distinct 2d(v)-R(v). This is relevant prior art for D3, and it overlaps on suitable regular subclasses, but no implication covering D3 in its full nonregular, simultaneous form was identified.
6. Ben-Ameur, Glorieux and Neto, [On the most imbalanced orientation of a graph](https://doi.org/10.1007/s10878-017-0117-1), [author manuscript](https://hal.science/hal-01497902/document), Theorem 9 and its following refinement, already imply imbalance at least two when the ordinary simple graph has minimum degree four. Thus the ordinary simple-graph antisymmetric-incidence specialization of E1 is established prior art. The manuscript's arbitrary signed rows, variables with one or two occurrences, possible parallel incidences and colouring applications require a separate comparison. No full identical statement was located in this screening; that does not establish first priority for the general lemma.

## Assessment by inventory group

Here **candidate** means that the same full hypotheses and conclusion were not identified in the screened sources. It does not mean proven historically new.

| Group | Assessment |
|---|---|
| A1 | Strongest new-theorem candidate; directly extends the screened published subcubic results. |
| A2 | Candidate sparse branch-core criteria. Independent degree-three and other already covered subclasses do not count as separate discoveries. |
| A3 | Candidate degree-homogeneous core construction; prescribed interfaces matter in comparing scopes. |
| A4–A5 | Candidate balanced and preserved-colour subdivision statements. Euler and Hall arguments are classical. |
| A6 | Candidate particular parity/degree-gap criterion. Parity separation itself is known. |
| A7–A8 | Candidate arbitrary-root, outside-contribution and capacity bounds. Ordinary clique colourability is already known. |
| A9 | Auxiliary given-colouring gluing criterion; elementary sign choices alone are not a major new method. |
| B1 | Candidate exact endpoint tables, decorated saturation and sharp preserved-boundary thresholds. Bare path/tree existence is already known. |
| B2 | Classical general theory and problem-specific reductions. Do not describe the whole group as original theory. |
| B3 | Candidate particular polynomial/coefficient identities; interpolation, the Nullstellensatz and permanent methods are established. |
| B4 | Candidate problem-specific normal forms and counterexample restrictions; general elimination and dynamic programming are established. |
| C1–C5 | Candidate explicit examples and sharp restricted-strategy obstructions. They are not counterexamples to the conjecture, and the general observation that a local strategy can fail is not new. |
| D1 | Candidate explicit sufficient condition delta >= 8 chi (2 chi + 1) - 7 and its external-contribution version. The degree-constrained subgraph theorem it uses is attributed prior art. |
| D2 | Candidate specified multi-region and attachment extensions; weaker consequences should be folded into stronger statements. |
| D3 | Candidate simultaneous red/blue all-vertices distinction under 8 delta >= 7 n + 6. Dense irregularity-strength results are relevant and partly overlap, as explained above. |
| D4 | Candidate particular four-vertex complement lift and families, rather than novelty of all component graph classes. |
| D5 | Candidate forbidden-target and external-contribution dense criteria; Tutte's theorem is classical. |
| E1 | Candidate general signed lemma and its exact applications; an ordinary orientation specialization is known. |
| E2 | Candidate supplied path/cycle-versus-covering-matching construction. Binary constraint solving itself is known. |
| E3 | Candidate precise protected/fixed-interface feasibility conditions and examples; T-join theory is classical. |
| E4 | Candidate arbitrary-degree root-port capacity criterion. The parity-sum test is classical; the specified capacity/interface theorem is the contribution under comparison. |

## What was actually searched

The new saved web log contains 33 search queries, 10 explicit page opens, and further in-page finds, including direct reading of the central arXiv manuscripts, the DMTCS paper and the author manuscript on imbalanced orientations. A preceding four-query web batch was also executed, but its complete returned text was not retained in this log. Counts describe retrieval operations, not the number of papers read in full.

Fresh public Zenodo API queries, after correcting the unauthenticated page-size limit to 25, returned 5 records for the exact phrase "locally irregular", 14 for "local irregularity", and 0 for "2-multigraphs". All returned titles and descriptions were screened. The Imbalance Conjecture records concern whether the multiset of edge-degree differences is graphical; they do not state A1. The digraph software deposit concerns a different object. Search indexing, metadata coverage and unpublished work remain limitations.

Two Crossref searches returned 40 metadata items each. Their fuzzy total-hit counts were not treated as numbers of relevant papers or papers examined. Another Crossref request was rate-limited. The arXiv export API failed with a TLS error and a timeout; direct arXiv pages and indexed searches were used instead. No fresh exhaustive arXiv corpus crawl is claimed.

Domain-restricted searches included Annals of Mathematics, Acta Mathematica, Journal of the American Mathematical Society and Inventiones Mathematicae. No relevant duplicate was returned by the final four-domain query batch. This is an indexed-search observation, not a full-text audit of every article in those journals. The broader 27 October report is a historical screening record; its old corpus counts have not been relabelled as fresh searches.

The internal screening was AI-assisted. No external specialist review, plagiarism-database clearance, proof-assistant verification or absolute-priority certificate is represented by this note. A publication should say that no prior proof of the full statement was found in the screened literature, and should not say that every retained inventory item is unprecedented.
