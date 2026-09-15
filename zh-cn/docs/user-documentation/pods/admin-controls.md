# 工作区管理员的 Pod 政策设置

管理员可以在 **Admin settings > Capabilities** 中管理两项 Pod 政策：成员能否创建 Open Pod，以及能否手动向 Pod 添加文件。

## Pod 可见性

| 设置 | 效果 |
|---|---|
| **Private and open Pods**（默认） | 成员既可以创建 Restricted Pod，也可以创建 Open Pod。 |
| **Private Pods only** | 成员只能创建 Restricted Pod。Open 可见性开关会被禁用，并显示提示。 |

启用 **Private Pods only** 不会自动关闭已经存在的 Open Pod。Pod Editor 仍可手动将这些 Pod 改为 Restricted。

## Pod 文件

| 设置 | 效果 |
|---|---|
| **Manual updates allowed**（默认） | 成员可以上传文件，也可以将 Company Data 关联到 Pod。 |
| **Manual updates disabled** | 成员看不到 **Add** 按钮；智能体和自动连接器仍可向 Files 添加内容。 |

两项政策默认均采用限制较少的选项。更改政策会影响成员可用的相应控件；更改可见性政策时，还应单独检查已有 Pod。
