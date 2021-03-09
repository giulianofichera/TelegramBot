import sys
sys.path.insert(0, '/Users/giulianofichera/Documents/Python Projects/CryptoBot')
from btc_usdc import info_btc_usdc
from usdc_ars import info_usdc_ars
from telegram.ext import Updater, CommandHandler, MessageHandler
import threading

menu = """--- Menu ---
/btc
/usdc"""

# --- Read credentials ---
try:
    f = open("/Users/giulianofichera/Documents/Python Projects/TelegramBotCredentials.txt", 'r')
except OSError:
    print ("Could not open/read file:", f)
    sys.exit()

bot_credentials = f.read().splitlines()
f.close

bot_token = bot_credentials[0]
chat_id = bot_credentials[1]
print(f'Bot Token: {bot_token}')
print(f'Chat ID: {chat_id}')

#----- Bot  Code -----
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=chat_id, text=menu)

def btc(update, context):
    context.bot.send_message(chat_id=chat_id, text="Parsing information...")
    context.bot.send_message(chat_id=chat_id, text=info_btc_usdc())

def usdc(update, context):
    context.bot.send_message(chat_id=chat_id, text="Parsing information...")
    context.bot.send_message(chat_id=chat_id, text=info_usdc_ars())

def stop(update, context):
    threading.Thread(target=shutdown).start()

def shutdown():
    updater.stop()
    updater.is_idle = False

# /start
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
# /btc
btc_handler = CommandHandler('btc', btc)
dispatcher.add_handler(btc_handler)
# /usdc
usdc_handler = CommandHandler('usdc', usdc)
dispatcher.add_handler(usdc_handler)
# /stop
stop_handler = CommandHandler('stop', stop)
dispatcher.add_handler(stop_handler)


updater.start_polling()
updater.dispatcher.bot.sendMessage(chat_id=chat_id, text=menu)
print('Bot Active...')

exit()