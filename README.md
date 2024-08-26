# Check-JMS-Bandwidth
Check JMS Bandwidth with Github Action

# 说明:
之前让ChatGPT出了一个python代码扔服务器里跑来着，不知道怎么估计被我误删除了，这几天都没效果了，索性让Claude帮忙出个新的，扔Github Action吧~~  
蛮好玩的~~

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
