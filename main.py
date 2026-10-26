from flask import Flask
from threading import Thread
import os
import telebot  # টেলিগ্রাম লাইব্রেরি ইমপোর্ট করা হলো

# সরাসরি আপনার টেলিগ্রাম বটের টোকেন এখানে বসিয়ে দেওয়া হলো
API_TOKEN = '8668983865:AAFko-GOeu7_AVdSryLhhfr7yJ5twpbYWcc'
bot = telebot.TeleBot(API_TOKEN)

app = Flask('')

@app.route('/')
def home():
    print("Ping received!")
    return "Bot is alive!"

def run():
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# বটের সাধারণ কমান্ড (যেমন /start দিলেই বট রিপ্লাই দেবে)
@bot.message_handler(commands=['start'])
def send_welcome(bot_message):
    bot.reply_to(bot_message, "হ্যালো! আপনার টেলিগ্রাম বট এখন সফলভাবে সচল আছে। 🎉")

# যেকোনো সাধারণ মেসেজের উত্তর দেওয়ার জন্য
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "আপনার মেসেজটি আমি পেয়েছি!")

if __name__ == "__main__":
    # প্রথমে ফ্লাস্ক সার্ভার চালু হবে যাতে রেন্ডার পোর্ট পেয়ে যায়
    keep_alive()
    
    # এরপর টেলিগ্রাম বট পোলিং শুরু করবে যাতে মেসেজ রিসিভ করতে পারে
    print("Bot polling started...")
    bot.infinity_polling()
    
