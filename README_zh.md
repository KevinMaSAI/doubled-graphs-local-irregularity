# 倍边图局部不规则二染色：论文与证明材料

**Qiyuan Ma · 上海交通大学**  
联系：[mqyqwerty@sjtu.edu.cn](mailto:mqyqwerty@sjtu.edu.cn)

这个仓库按“研究总览 → 结果目录 → 论文及源码 → 证明材料 → 更新记录”组织。目前为 **1 篇论文、1 个问题家族**。A1–E4 是研究记录编号，不代表相互独立的新论文数量或学术评级。

## 从哪里开始

1. **[两页研究总览](overview.pdf)**：先看问题、主结果、其他构造和检查边界。
2. **[完整英文论文](preprints/Locally-Irregular-Two-Edge-Colourings-of-Doubled-Graphs-October-28-2026/paper.pdf)**：64 页，包含证明和有限证书附录。
3. **[结果与材料目录](CONTENTS.md)**：按 A1、A2–A9、B、C、D、E 导航。
4. **[论文源码与构建说明](preprints/Locally-Irregular-Two-Edge-Colourings-of-Doubled-Graphs-October-28-2026/)**：TeX 源码已展开，可以在 GitHub 直接阅读。
5. **[有限证书和检查程序](proof_artifacts/)**：A1 的关键数据和程序已展开；全部 697 个文件保留在 [完整复现 ZIP](reproducibility.zip) 中。
6. **[验证范围](VERIFICATION.md)**、**[查新说明](NOVELTY_AND_RELATED_WORK.md)**、**[更新记录](history.md)**：分别说明检查了什么、新颖性结论的边界、版本如何变化。

## 运行检查

下载整个仓库（Code → Download ZIP）并解压，在仓库根目录执行：

```sh
python -I -B proof_artifacts/subcubic/verify.py
python -I -B verify_snapshot.py
```

需要 Python 3.10 或更新版本。有限证书检查不需要第三方库、求解器或联网。第二条命令会解压完整快照，保留检查目录和输出。

论文提出覆盖全部次三正则底图的计算机辅助证明，并给出若干无最大度上界的条件性构造。任意连通图的母猜想仍未解决。Python 证书检查与 Lean 形式化不同，独立专家审稿尚未获得。

论文/说明/证书采用 CC BY 4.0；Python 代码采用 MIT。AI 协助和经典工具的来源均有说明。Zenodo 尚未上传，日后得到真实 DOI 再补入引用信息。
