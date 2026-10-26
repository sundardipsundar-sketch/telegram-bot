from flask import Flask
from threading import Thread
import os
import telebot

TELEGRAM_TOKEN = '8668983865:AAG_ppMVN7Zi_Ph6bWsfVGcFT3zHl-67FN0'
bot = telebot.TeleBot(TELEGRAM_TOKEN)

app = Flask('')

@app.route('/')
def home():
    print("Ping received!")
    return "Copy-cat Bot is alive!"

def run():
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        bot.reply_to(message, "Arre bhai! Ami copy-cat bot. Group e reply dile ba 'copy cat' bollei ami copy korbo! 😎")
    except Exception as e:
        bot.send_message(message.chat.id, "Arre bhai! Ami copy-cat bot. Group e reply dile ba 'copy cat' bollei ami copy korbo! 😎")

# Copy-cat handler
@bot.message_handler(func=lambda message: True)
def copy_cat(message):
    user_text = message.text if message.text else ""
    if not user_text:
        return

    # Jodi group chat hoy
    if message.chat.type in ['group', 'supergroup']:
        is_reply_to_bot = message.reply_to_message and message.reply_to_message.from_user.id == bot.get_me().id
        is_called_copycat = "copy cat" in user_text.lower() or "copycat" in user_text.lower()
        
        # Group e reply ba "copy cat" na thakle ignore korbe
        if not (is_reply_to_bot or is_called_copycat):
            return

    # Reply dite giye error asle o jeno crash na kore, tai try-except use kora holo
    try:
        bot.reply_to(message, user_text)
    except Exception as e:
        bot.send_message(message.chat.id, user_text)

if __name__ == "__main__":
    keep_alive()
    print("Copy-cat Bot polling started...")
    bot.infinity_polling()
    
