from config import TELE_API_KEY
import telegram

# chat = telegram.Bot(token = TELE_API_KEY)
# updates = chat.getUpdates()
# for u in updates:
#     print(u.message['chat']['id'])

bot = telegram.Bot(token = TELE_API_KEY)
text = '안녕하세요'
bot.sendMessage(chat_id = "-1001660821686", text=text)