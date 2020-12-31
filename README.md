# Sandbot for Telegram
Find out at what time to sleep or go to bed

## Deploying to heroku
You'll need to add a few files to `src/`.

First, create a **Procfile** that looks like this (change the value of TOKEN to your bot's token and HEROKU to your heroku app's URL with a trailing `/`):
```
web: echo -e "TOKEN\nHEROKU" | python3 bot.py
```

Then, a **requirements.txt** file:
```
python-telegram-bot==13.1
```
