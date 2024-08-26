# Check-JMS-Bandwidth
Check JMS Bandwidth with Github Action

# 说明:
之前让ChatGPT出了一个python代码扔服务器里跑来着，不知道怎么估计被我误删除了，这几天都没效果了，索性让Claude帮忙出个新的，扔Github Action吧~~  
蛮好玩的~~

# Check JMS bandwidth and send notification:
在 GitHub 仓库的 Settings > Secrets and variables > Actions 中添加两个key：   
JMS_API_URL: 设置为你的 API URL  
SERVER_CHAN_KEY: 设置为你的 Server 酱 API 密钥  
TELEGRAM_BOT_TOKEN: 设置为你的 Telegram Bot Token  
TELEGRAM_CHAT_ID: 设置为你的 Telegram Chat ID
