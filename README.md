# Counso Docs

Counso 产品文档仓库，包含中英文正文、发布状态、兼容路由和 Mintlify 站点。

## 文档索引

- [English](en/SUMMARY.md)
- [简体中文](zh-cn/SUMMARY.md)
- [发布状态](PUBLICATION-STATUS.md)
- [页面映射](translations.json)
- [兼容跳转](redirects.json)

## 目录结构

```text
en/               英文文档
zh-cn/            中文文档
prepared/         待确认或待改写的双语底稿
source/           内部迁移与校对资料
mintlify-site/    可直接预览和部署的 Mintlify 站点
scripts/          生成与检查脚本
```

## 发布规则

| 状态 | 展示方式 |
| --- | --- |
| `publish` | 发布对应语言正文 |
| `updating` | 保留 URL，仅展示“文档更新中” |
| `exclude_upstream` | 不进入公开站点 |

包含旧品牌标识或尚未完成产品适配的内容会自动进入更新状态。历史路径通过 `redirects.json` 跳转到当前 Counso 路径。

## 本地检查

```bash
python3 scripts/check.py
python3 scripts/build_mintlify.py
python3 scripts/check_mintlify_navigation.py
```

## 本地预览

```bash
cd mintlify-site
npx mint dev --port 3333
```

打开：

- English: <http://localhost:3333/>
- 简体中文: <http://localhost:3333/zh-Hans/>

## 部署

将 Mintlify 项目的文档根目录设置为 `mintlify-site`。部署前运行检查脚本，确认导航、双语页面和兼容跳转均有效。
