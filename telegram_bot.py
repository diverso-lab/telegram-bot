import telegram
import os

token = os.environ['TELEGRAM_BOT_TOKEN']
chat_id = os.environ['TELEGRAM_BOT_CHAT_ID']

bot = telegram.Bot(token=token)


def send_telegram_notification(notification):

    bot.send_message(text=notification, chat_id=chat_id,
                     parse_mode='Markdown', disable_web_page_preview=True)
