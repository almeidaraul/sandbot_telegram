from telegram.ext import Updater, CommandHandler
from datetime import date, datetime as dt, timedelta as tdelta
from pytz import timezone
import logging

def go_now(update, context):
    epoch = update.message.date
    msg = "If you go to bed now, you should wake up at one of those times:\n"
    for i in range(6):
        #tm = dt.fromtimestamp(add_minutes(epoch, tdelta(minutes=90*(i+1)))).astimezone(timezone('Etc/GMT-3'))
        d = tdelta(minutes=90*(i+1))
        tm = (epoch + d).astimezone(timezone('America/Sao_Paulo'))
        msg += "* {}:{}\n".format(tm.hour, "0{}".format(tm.minute) if tm.minute < 10 else tm.minute)
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

def info(update, context):
    msg = "It takes the average person 15-ish minutes to fall asleep and a sleep cycle takes about 90 minutes. A good night consists of 5-6 complete cycles."
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Get info with /info or find out when to wake up if you go to bed now with /go_now")

TOKEN = input()

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

start_handler = CommandHandler('start', start)
info_handler = CommandHandler('info', info)
go_now_handler = CommandHandler('go_now', go_now)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(go_now_handler)

updater.start_polling()
