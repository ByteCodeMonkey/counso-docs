---
title: "模型访问层级"
---
如果工作区提供 **Models tier** 控制项，管理员可以限制成员能选择的模型和推理设置。这项控制设置的是模型选择上限，不是席位或积分额度。它可将较强的模型选项保留给确有需要的工作，同时让日常任务使用适合团队的模型。

## 了解模型层级

工作区可能会将模型和推理设置组合为 **Basic**、**Standard**、**Premium** 等递进层级。当前模型选择器及层级说明会显示每一层包含哪些组合。模型供应情况和工作区配置可能改变这些归类，因此请以当前界面显示为准，不要沿用静态模型清单。

层级可能针对“某个模型 + 某种推理设置”的组合。同一个模型在一种推理设置下可用，在另一种设置下则可能被限制。模型上限也可能同时作用于相应的自动模型选项，而不只是具体列出的模型。

## 各层级当前包含的选项

以下列表对应 2026 年 9 月 14 日的模型层级说明。供应商可用性和工作区配置可能使列表发生变化。带星号的选项可能取决于工作区配置或订阅资格；最终请以当前模型选择器为准。

### Basic

| 模型 | 此层级提供的推理强度 |
| --- | --- |
| Claude 4.5 Haiku | Light、Medium、High |
| Claude Sonnet 4.6 | Light |
| Claude Sonnet 5 | Light |
| DeepSeek V4.1 Flash (Fireworks) | None、Light、Medium、High |
| Gemini 3.1 Flash Lite | None、Light、Medium |
| Gemini 3.5 Flash Lite | None、Light、Medium |
| Mistral Codestral | None |
| Mistral Small | None |
| GPT-5.4 Mini | None、Light、Medium、High |
| GPT-5.4 Nano | None、Light、Medium、High |
| GPT 5.6 Luna | None、Light |
| GLM-5.3 Flash (Fireworks) | Light、Medium、High |

### Standard

| 模型 | 此层级提供的推理强度 |
| --- | --- |
| Claude Sonnet 4.6 | Medium |
| Claude Sonnet 5 | Medium |
| Inkling (Fireworks) | Light、Medium、High |
| Kimi K3 (Fireworks) | Light |
| GLM-5.3 (Fireworks) | Light、Medium、High |
| Gemini 3.1 Flash Lite | High |
| Gemini 3.1 Pro (Preview) | Light |
| Gemini 3.5 Flash Lite | High |
| Gemini 3.7 Flash | Light、Medium |
| Gemini 3.8 Flash | Light、Medium |
| Mistral Large | None |
| Mistral Medium 3.5 | None |
| GPT 5.6 Luna | Medium、High |
| GPT 5.6 Sol\* | None |
| GPT 5.6 Terra | None、Light、Medium、High |
| Grok 4.5\* | Light、Medium、High |
| Grok 4.6\* | Light、Medium |

### Premium

| 模型 | 此层级提供的推理强度 |
| --- | --- |
| Claude Opus 4.6 | Light、Medium、High |
| Claude Sonnet 4.6 | High |
| Claude Sonnet 5 | High |
| Kimi K3 (Fireworks) | Medium、High |
| Gemini 3.1 Pro (Preview) | Medium、High |
| Gemini 3.7 Flash | High |
| Gemini 3.8 Flash | High |
| Mistral Medium 3.5 | High |
| GPT 6 Astra\* | Light、Medium、High |
| GPT 5.6 Sol\* | Light、Medium、High |
| GPT 5.6 Terra (long context)\* | None、Light、Medium、High |
| Grok 4.6\* | High |

## 设置工作区上限

1. 打开 **Admin > Usage**；如果页面提供，找到 **Models tier**。
2. 在 **Workspace access** 中设置成员可选择的最高层级。
3. 群组或个人保留 **Inherit**，即可沿用下一层适用设置。

没有更具体覆盖设置的成员会遵循工作区设置。调整前先检查当前页面提供的选项；可用层级取决于现行订阅和模型配置。

## 设置群组或个人覆盖项

在同一页面的群组表格中，可为团队设置模型上限。**Inherited from workspace** 表示群组沿用工作区设置。成员表格可为个人设置上限；选择 **Inherit** 时，成员沿用所属群组的设置；如无适用群组，则沿用工作区设置。

系统按以下顺序确定成员的实际上限：

1. 优先采用个人覆盖设置。
2. 如果没有个人设置，成员所属群组中存在覆盖设置时，采用其中最高的层级。
3. 否则采用工作区上限。

群组覆盖项会授予成员相应层级，不会降低其所在其他高层级群组带来的权限。如果某位成员需要不同上限，可为其单独设置覆盖项。

## 已发布的 Agent

如果成员的模型层级低于某个 Agent 的配置，系统可能会阻止其运行该 Agent。如果页面提供并开启 **Published agents**，所有成员都可运行已发布的 Agent，即使其中配置的模型高于成员个人选择上限。成员仍不能自行选择该高层级模型；未发布或个人 Agent 仍受上限约束，创建或编辑使用更高层级模型的 Agent 也可能被阻止。

依赖此例外之前，应先核对谁有权发布 Agent，并确认已发布工作流适合其使用对象。

## 成员看到的提示与设置复核

高于成员上限的模型或推理设置可能会在选择器中显示为锁定状态。自动模型选项也可能被锁定，而不是悄悄改用较低层级。若尝试运行超出允许层级的 Agent，界面可能显示模型访问限制提示。

如果工作区启用了审计日志，工作区、群组和成员上限的更改可能会记录在日志中。更改后检查日志，并使用相关群组的一名成员测试受影响的模型选项。

模型层级限制的是成员可选模型，本身不会设置积分预算，也不保证用量一定下降。其他控制方式见[优化积分使用](/zh-Hans/docs/user-documentation/admins/usage-seats-and-credits/optimize-credit-consumption)。
