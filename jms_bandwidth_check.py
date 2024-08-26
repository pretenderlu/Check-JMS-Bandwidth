import os
import requests
import logging
from datetime import datetime

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_data_from_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"API请求失败: {e}")
        return None

def send_message_to_server_chan(title, desp, key):
    base_url = "https://sctapi.ftqq.com/"
    full_url = f"{base_url}{key}.send"
    data = {'title': title, 'desp': desp}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    try:
        response = requests.post(full_url, data=data, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"发送消息到Server酱失败: {e}")
        return None

def send_telegram_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"发送消息到Telegram失败: {e}")
        return None

def bytes_to_gb(bytes):
    return bytes / (2**30)

def main():
    # 从环境变量获取API URL、Server酱密钥和Telegram信息
    api_url = os.environ.get('JMS_API_URL')
    server_chan_key = os.environ.get('SERVER_CHAN_KEY')
    telegram_bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')
    telegram_chat_id = os.environ.get('TELEGRAM_CHAT_ID')

    if not api_url or not server_chan_key or not telegram_bot_token or not telegram_chat_id:
        logging.error("缺少必要的环境变量")
        return

    data = get_data_from_api(api_url)
    if not data:
        return

    used_bw_bytes = data['bw_counter_b']
    total_bw_bytes = data['monthly_bw_limit_b']
    bw_reset_day = data['bw_reset_day_of_month']

    used_bw_gb = bytes_to_gb(used_bw_bytes)
    total_bw_gb = bytes_to_gb(total_bw_bytes)
    used_percentage = (used_bw_bytes / total_bw_bytes) * 100

    message_content = f"JMS已使用流量: {used_bw_gb:.2f} GB ({used_percentage:.2f}%)\n总流量限制: {total_bw_gb:.2f} GB\n流量将在每月的第 {bw_reset_day} 日重置。"

    # 发送Server酱通知
    server_chan_response = send_message_to_server_chan("流量使用通知", message_content, server_chan_key)
    if server_chan_response:
        logging.info("Server酱消息发送成功")
    else:
        logging.error("Server酱消息发送失败")

    # 发送Telegram通知
    telegram_message = f"*JMS流量使用通知*\n\n{message_content}"
    telegram_response = send_telegram_message(telegram_bot_token, telegram_chat_id, telegram_message)
    if telegram_response:
        logging.info("Telegram消息发送成功")
    else:
        logging.error("Telegram消息发送失败")

if __name__ == "__main__":
    main()
