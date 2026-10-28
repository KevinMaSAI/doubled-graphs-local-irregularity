# 倍边图局部不规则二染色：论文与复现材料

作者：**Qiyuan Ma，上海交通大学**。英文署名和单位以论文为准。联系邮箱：[mqyqwerty@sjtu.edu.cn](mailto:mqyqwerty@sjtu.edu.cn)。

**[阅读英文论文](paper.pdf)** · **[下载完整代码、源码和证书](reproducibility.zip)** · **[查新与相关工作](NOVELTY_AND_RELATED_WORK.md)**

论文提出覆盖全部次三正则底图的计算机辅助证明，并整理若干无最大度上界的条件性构造、边界扩展和固定策略障碍。任意连通图的母猜想仍未解决。预印本尚未获得独立专家审稿或 Lean 等证明助手验证；有限枚举不替代论文中的一般论证。

## 第一次使用这个仓库

1. 只读论文：点击上面的 PDF 链接。
2. 获取全部材料：点击仓库绿色 **Code → Download ZIP**，解压后即可看到本页文件；完整 697 文件的复现快照另保存在 `reproducibility.zip` 中。
3. 检查有限证书：在本页文件所在目录运行 `python -I -B verify_snapshot.py`。需要 Python 3.10 或更新版本，不需要第三方依赖或联网。检查生成的工作目录保留在 `validation/`。
4. 修改证明或运行构造程序：解压 `reproducibility.zip`。`manuscript/` 是 TeX 源码，`artifact/` 含各图族代码和 JSON 证书，根目录的 `README.md` 提供完整运行方法。

论文和证书采用 CC BY 4.0；Python 代码采用 MIT。AI 协助、经典工具和查新的限制均公开说明。A1 等标签只是本项目追溯编号，不是数学界的评级。

本次已准备为 GitHub 公开存档；Zenodo 发布和 DOI 将另行办理。后续有 DOI 后可补入引用信息。
