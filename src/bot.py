from telegram.ext import Updater, CommandHandler
from datetime import date, datetime as dt, timedelta as tdelta
from pytz import timezone
import logging
import os

STRF = "%H:%M"
PORT = int(os.environ.get('PORT', 5000))

def date_from(s):
    s = s.split(':') if s else ""
    if len(s) != 2 or any([x for x in s if not x.isnumeric()]):
        return None
    else:
        d = dt.now().replace(hour=int(s[0]), minute=int(s[1]))   
        return d

def sleep(update, context):
    sleep_at = date_from(update.message.text.split(' ')[-1])
    if not sleep_at:
        msg = "Nope. Can't do that. Example usage: /sleep 23:15" 
    else:
        msg = "Falling asleep at {}? If I were you, I'd choose one of these to wake up at:\n".format(sleep_at.strftime(STRF))
        for i in range(6):
            d = tdelta(minutes=90*(i+1))
            tm = (sleep_at + d).astimezone(timezone('America/Sao_Paulo'))
            msg += "* {}\n".format(tm.strftime(STRF))
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

def wake(update, context):
    wake_at = date_from(update.message.text.split(' ')[-1])
    if not wake_at:
        msg = "Nope. Can't do that. Example usage: /wake 8:15" 
    else:
        msg = "Wanna wake up at {}? Well, go to bed around one of these times:\n".format(wake_at.strftime(STRF))
        for i in reversed(range(6)):
            d = tdelta(minutes=-(15+90*(i+1)))
            tm = (wake_at + d).astimezone(timezone('America/Sao_Paulo'))
            msg += "* {}\n".format(tm.strftime(STRF))
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

def now(update, context):
    epoch = update.message.date
    msg = "Already going to bed? Good night! Try to wake up when the clock hits one of these:\n"
    for i in range(6):
        d = tdelta(minutes=15+90*(i+1))
        tm = (epoch + d).astimezone(timezone('America/Sao_Paulo'))
        msg += "* {}\n".format(tm.strftime(STRF))
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

def info(update, context):
    msg = "I imagine it takes you around 15 minutes to fall asleep and that a sleep cycle goes for 90ish minutes. A good night would be 5-6 complete cycles."
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

def start(update, context):
    msg = "Welcome! I'm here to help you decide when to go to bed and/or when to fall asleep. Run /info to find out more about me."
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)


if __name__ == "__main__":
    TOKEN = "your-token-here"
    HEROKU = "https://app-name.herokuapp.com/"

    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                         level=logging.INFO)

    start_handler = CommandHandler('start', start)
    info_handler = CommandHandler('info', info)
    now_handler = CommandHandler('now', now)
    sleep_handler = CommandHandler('sleep', sleep)
    wake_handler = CommandHandler('wake', wake)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(info_handler)
    dispatcher.add_handler(now_handler)
    dispatcher.add_handler(sleep_handler)
    dispatcher.add_handler(wake_handler)

    # updater.start_polling()
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook(HEROKU + TOKEN)
