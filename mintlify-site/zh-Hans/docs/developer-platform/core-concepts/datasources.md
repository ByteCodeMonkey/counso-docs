---
title: "数据源"
---
数据源是由 Counso 管理并用于语义搜索的文档集合。在 Counso 界面创建时，需要填写简短名称，可选填描述。名称只能包含小写字母、数字和连字符；新建数据源时内容为空。可在 Settings 中修改描述或删除数据源，但不能重命名。

文档可通过界面或 API 添加。导入时，Counso 会清理重复空格，按配置的 `max_chunk_size` 将文本切块、生成向量，并将向量与文档元数据和原始文本一起编入索引。默认嵌入模型为 `text-embedding-3-large`；工作区支持时也可使用其他模型。

插入或更新文档时，请使用稳定的 `document_id`。将 `baseUrl` 设为 `https://app.counso.ai` 后，upsert 路由为 `POST {baseUrl}/api/v1/w/{wId}/spaces/{spaceId}/data_sources/{dsId}/documents/{documentId}`，JSON 请求体包含 `text`。新 ID 会创建文档；已存在的 ID 会替换旧版本及其索引文本块。搜索路由为 `GET {baseUrl}/api/v1/w/{wId}/spaces/{spaceId}/data_sources/{dsId}/search`。删除文档会移除关联文本块；删除数据源会移除其中所有文档和文本块。执行删除前请确认目标。

批量导入目录时，可用脚本读取 PDF、TXT 和 Markdown 文件，并逐份 upsert。下面的示例使用 Python、`requests` 和 `pdftotext`；工作区、Space、数据源和凭据通过环境变量提供。示例以文件的相对路径生成文档 ID，因此不同文件夹里的同名文件仍有各自的标识。

```python
import os
import pathlib
import sys
from urllib.parse import quote
import requests
import pdftotext

base_url = os.getenv("COUNSO_BASE_URL", "https://app.counso.ai")
workspace_id = os.environ["COUNSO_WORKSPACE_ID"]
space_id = os.environ["COUNSO_SPACE_ID"]
data_source_id = os.environ["COUNSO_DATA_SOURCE_ID"]
api_key = os.environ["COUNSO_API_KEY"]

def upload(text, file):
    document_id = file.relative_to(directory).as_posix()
    url = (f"{base_url}/api/v1/w/{workspace_id}/spaces/{space_id}"
           f"/data_sources/{data_source_id}/documents/{quote(document_id, safe='')}")
    return requests.post(
        url,
        headers={"Authorization": f"Bearer {api_key}"},
        json={"text": text},
    )

directory = pathlib.Path(sys.argv[1])
for file in directory.rglob("*"):
    if not file.is_file():
        continue
    if file.suffix.lower() == ".pdf":
        with file.open("rb") as source:
            text = "\n\n".join(pdftotext.PDF(source))
    elif file.suffix.lower() in {".txt", ".md"}:
        text = file.read_text()
    else:
        continue
    response = upload(text, file)
    if response.status_code != 200:
        print("导入失败：", file, response.status_code, response.text)
    else:
        print("已导入：", file)
```

将脚本保存为 `upload.py`，安装 `requests` 和 `pdftotext`，设置上述环境变量，然后运行 `python upload.py <待导入目录>`。

逐份检查响应，并在 Counso 中抽查索引内容。默认 `baseUrl` 为 `https://app.counso.ai`，其他环境请替换为相应基础地址。

Agent 搜索数据源时，Counso 会将查询向量化并检索相关文本块。结果按原始文档归组，让 Agent 可以使用相关段落，而不用将所有完整文档都放入上下文。这种检索方式称为检索增强生成（RAG）。分块和结果排序方式见[文本块与文档](/zh-Hans/docs/developer-platform/core-concepts/chunks-and-documents)。
