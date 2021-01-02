# Sandbot for Telegram
Find out at what time to sleep or go to bed

## Deploying to heroku
### Adding a requirements.txt and Procfile
You'll need to add a few files to `src/`.

**Procfile**
```
web: python3 bot.py
```

**requirements.txt**
```
python-telegram-bot==13.1
```

### Creating an app and getting it's URL
* Install the Heroku CLI
* Run `heroku login` and `heroku create`. The latter will print your app's URL.

### Telling your bot about it
Change the variables TOKEN and HEROKU in `src/bot.py` to your bot's token and your heroku app's url, respectively.

### Deploy with `heroku-builds`
Using [heroku-builds](https://github.com/heroku/heroku-builds), we can deploy this without exposing the bot's token in Github.

Run
```
heroku plugins:install heroku-builds
cd src
heroku builds:create -a app-name
```
