# 贡献指南

## 加入 OPC Hub

### 第一步：准备档案

1. Fork 本项目
2. 复制 `TEMPLATE.md` 到 `directory/members/你的handle.md`
3. 按模板填写信息，注意：
   - `handle` 使用小写英文 + 数字 + 短横线，全局唯一
   - `skills` 和 `industries` 使用常见的中文标签
   - `available: true` 表示当前可接受合作
   - `registered_company` 选填，填写后有助于加速确权审核

### 第二步：提交 PR

1. 创建 Pull Request
2. 在 PR 描述中按照 PR 模板填写信息
3. 附上确权证明材料（见 [VERIFICATION.md](VERIFICATION.md)）

### 第三步：等待审核

审核委员会将在 7 个工作日内完成审核。

## 档案规范

### 文件命名

- 文件名 = handle + `.md`
- 仅允许：小写字母、数字、短横线
- 示例：`zhang-san.md`、`dev-john.md`

### 标签规范

为了便于检索，请使用已有的常用标签。查看 `directory/index.yaml` 中已使用的标签作为参考。

常见技能标签示例：
`React开发` `Vue开发` `Node.js` `Python` `UI设计` `品牌设计` `产品经理` `独立咨询` `内容创作` `视频制作` `SEO优化` `数据分析` `AI开发` `小程序开发` `运营增长`

常见行业标签示例：
`SaaS` `电商` `教育` `医疗` `金融` `新能源` `文创` `MCN` `企业服务` `跨境` `本地生活`

### 内容要求

- "关于我" 控制在 200 字以内
- 代表项目至少 1 个，建议 2-3 个
- 不得包含违法违规内容
- 不得包含纯广告或虚假信息

## 提交其他贡献

- **Bug 修复 / 功能建议**：提交 Issue
- **文档改进**：直接提 PR
- **索引工具优化**：修改 `scripts/` 下的脚本后提 PR
