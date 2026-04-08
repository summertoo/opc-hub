# OPC Hub 🌐

**开源一人公司（OPC）协作网络** — 让百万超级个体互相发现、互相成就。

## 什么是 OPC？

OPC（One Person Company）= 一人公司 / 超级个体。一个人就是一家公司，拥有独立的专业能力、客户资源和商业模式。

## 这个项目做什么？

OPC Hub 是一个**开源的 OPC 目录**：

- 🔍 **找人** — 按技能、行业、地区发现合适的 OPC 合作伙伴
- 📋 **找项目** — OPC 发布能力和需求，促进项目对接
- 🤝 **组队** — 多个 OPC 临时组队，承接更大的项目
- 🌱 **成长** — 在社区中交流经验，共同成长

## 如何加入？

### 1. Fork 本项目

### 2. 创建你的档案

复制 `TEMPLATE.md`，在 `directory/members/` 下创建以你的 handle 命名的文件：

```bash
cp TEMPLATE.md directory/members/你的handle.md
```

按照模板填写你的信息。

### 3. 提交 PR

提交 Pull Request，等待审核通过即可上线。

### 4. 企业确权

为确保目录质量，所有 PR 需经过**企业确权审核**流程：

- 审核由项目创建者及联合创始人组成的审核委员会执行
- 需验证申请人的真实经营状态
- 详见 [VERIFICATION.md](VERIFICATION.md)

## 目录浏览

浏览 [`directory/members/`](directory/members/) 查看所有已入驻的 OPC。

使用 [`directory/index.yaml`](directory/index.yaml) 进行结构化检索。

## 项目结构

```
opc-hub/
├── README.md                        # 本文件
├── TEMPLATE.md                      # OPC 档案模板
├── VERIFICATION.md                  # 企业确权审核规范
├── CONTRIBUTING.md                  # 贡献指南
├── directory/
│   ├── index.yaml                   # 全量索引（手动构建）
│   └── members/                     # OPC 档案目录
│       └── example.md               # 示例档案
├── scripts/
│   └── build_index.py               # 索引构建脚本
└── .github/
    └── PULL_REQUEST_TEMPLATE.md     # PR 模板
```

## 构建索引

索引采用**手动构建**，确保每次变更经过人工确认：

```bash
python scripts/build_index.py
```

## 许可证

[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) — 开放共享，署名相同方式分享。

## 联系我们

- 提交 Issue 或 PR
- 加入社区讨论

---

*让每一个超级个体都被看见。*
