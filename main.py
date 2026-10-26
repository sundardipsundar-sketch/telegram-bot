from flask import Flask
from threading import Thread
import os
import telebot

TELEGRAM_TOKEN = '8668983865:AAFko-GOeu7_AVdSryLhhfr7yJ5twpbYWcc'
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
    bot.reply_to(message, "Arre bhai! Main copy-cat bot hoon. Tu jo bhi bolega, main wahi same to same repeat karunga! 😎")

# Copy-cat handler
@bot.message_handler(func=lambda message: True)
def copy_cat(message):
    # Agar group chat hua toh sirf tag ya reply karne par hi kaam karega
    if message.chat.type in ['group', 'supergroup']:
        bot_username = bot.get_me().username
        is_mentioned = message.text and f"@{bot_username}" in message.text
        is_reply_to_bot = message.reply_to_message and message.reply_to_message.from_user.id == bot.get_me().id
        
        if not (is_mentioned or is_reply_to_bot):
            return

    user_text = message.text if message.text else ""
    if not user_text:
        return

    # Tu jo bhi likhega, wahi wapas bhej dega
    bot.reply_to(message, user_text)

if __name__ == "__main__":
    keep_alive()
    print("Copy-cat Bot polling started...")
    bot.infinity_polling()
    
