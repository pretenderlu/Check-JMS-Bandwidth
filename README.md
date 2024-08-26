# Check-JMS-Bandwidth
Check JMS Bandwidth with Github Action

# 说明:
name: 操作的名称，这里命名为 "Check JMS Bandwidth"。
on.schedule: 定义触发器，使用 cron 表达式设置每天早上 8 点运行。
jobs.check_bandwidth: 定义名为 "check_bandwidth" 的任务。
runs-on: 指定运行环境为 ubuntu-latest。
steps: 定义任务的执行步骤：
Checkout repository: 检出仓库代码，以便访问 Python 脚本。
Set up Python: 设置 Python 环境。
Install requests: 安装 requests 库，用于发送 HTTP 请求。

# Check JMS bandwidth and send notification:
设置 SERVER_CHAN_KEY 环境变量，从 GitHub Secrets 中获取值。
运行jms_bandwidth_check.py 脚本（请将此文件名替换为您实际保存 Python 代码的文件名）。

# 使用方法：
将上述 YAML 代码保存为 .github/workflows/check_jms_bandwidth.yml 文件，并提交到您的 GitHub 仓库。
在仓库的 "Settings" -> "Secrets and variables" -> "Actions" 中添加名为 SERVER_CHAN_KEY 的 Secret，并将值设置为您的 Server 酱密钥。
GitHub Action 将按照设定的时间表自动运行，检查 JMS 带宽并发送通知到您的 Server 酱。

# 请注意:
确保您已将 Python 代码保存为 jms_bandwidth_check.py 文件（或替换为您的实际文件名），并将其与 YAML 文件放在同一目录下。
如果您的 JMS API 详细信息或 Server 酱密钥发生更改，请相应地更新 Python 代码和 GitHub Secrets。
