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

# /start কমান্ড
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "আরে ভাই! আমি কপি-ক্যাট বট। ইনবক্সে নরমাল কপি করব, আর গ্রুপে 'copy cat' বললে তবেই চটপট একটিভ হব! 😎")

# কপি-ক্যাট হ্যান্ডলার
@bot.message_handler(func=lambda message: True)
def copy_cat(message):
    user_text = message.text if message.text else ""
    if not user_text:
        return

    # যদি চ্যাটটি গ্রুপ বা সুপারগ্রুপ হয়
    if message.chat.type in ['group', 'supergroup']:
        is_called_copycat = "copy cat" in user_text.lower() or "copycat" in user_text.lower()
        
        # গ্রুপে "copy cat" না বললে বট ইগনোর করবে
        if not is_called_copycat:
            return

    # পার্সোনাল চ্যাট হলে নরমাল কপি করবে, আর গ্রুপে "copy cat" বললেও কপি করবে
    bot.reply_to(message, user_text)

if __name__ == "__main__":
    keep_alive()
    print("Copy-cat Bot polling started...")
    bot.infinity_polling()
    
