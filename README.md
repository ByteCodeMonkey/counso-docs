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
components/       构建时复制到站点 snippets 的交互组件
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

## 同步上游文档

同步规则集中在 `sync-policy.json`。标准流程由 `scripts/sync_upstream.py` 编排：

```bash
python3 scripts/sync_upstream.py prepare
python3 scripts/sync_upstream.py verify
python3 scripts/sync_upstream.py preview
python3 scripts/sync_upstream.py finalize --reviewed
```

`prepare` 会将增删改报告写入被 Git 忽略的 `.sync/upstream-report.md`。`finalize`
不会推送远端；如需推送 main 和 Tag，需另外明确执行。

必须从干净的 `main` 分支执行 `prepare`。最后一条 `finalize` 命令只能在人工
Review 明确通过后执行，它会生成唯一同步提交、快进 `main` 并打 Tag。

## 部署

将 Mintlify 项目的文档根目录设置为 `mintlify-site`。部署前运行检查脚本，确认导航、双语页面和兼容跳转均有效。

## 教程视频

教程使用 `components/tutorial-video.jsx`，由构建脚本复制到站点的
`snippets/tutorial-video.jsx`。正文中导入 `TutorialVideo` 并传入视频 ID、标题和
语言；嵌入位置只展示播放器，保留原有文字步骤，不另加视频标题、外链或解释。页面打开后自动
连接并加载播放器，就绪时显示 YouTube 原生封面，用户点击播放；不自动播放。
检测期间显示本地加载提示；脚本加载失败、播放器返回错误或 15 秒内未就绪时，
显示对应提示卡片和重试按钮。此检测确认播放器能否就绪，不保证后续视频流始终可达。

不要只修改 `mintlify-site/`，该目录在每次构建时会重建。Counso 自编指南登记在
`translations.json` 的 `local_pages`，并加入中英文 `SUMMARY.md`；它们不需要
伪造上游来源。正文修改后先运行 `python3 scripts/check.py --update-hashes`，
再构建与检查导航。同步上游后复核视频小节和自编指南仍在对应位置。
