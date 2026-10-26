from flask import Flask
from threading import Thread
import os
import telebot

# আপনার টেলিগ্রাম বটের টোকেন
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

# /start কমান্ডের জন্য সুন্দর বহুভাষিক ওয়েলকাম মেসেজ
@bot.message_handler(commands=['start'])
def send_welcome(bot_message):
    welcome_text = (
        "Hello! Welcome! 🙏\n"
        "হ্যালো! আপনাকে স্বাগতম। 🎉\n"
        "Aapka swagat hai! Main aapka AI assistant bot hoon.\n\n"
        "You can talk to me in Bengali, English, or Hinglish!"
    )
    bot.reply_to(bot_message, welcome_text)

# বিভিন্ন ভাষার মেসেজের বুদ্ধিমান ও আকর্ষণীয় অটো-রিপ্লাই
@bot.message_handler(func=lambda message: True)
def smart_reply(message):
    user_text = message.text.lower()
    
    # বাংলা বা ইংরেজি বা হিংলিশ মিলিয়ে রেসপন্স তৈরি করা
    if "kemon acho" in user_text or "how are you" in user_text or "কেমন আছো" in user_text:
        reply = "Ami ekdom bhalo achi! Aap batao, aap kaise ho? (আমি একদম ভালো আছি!) 😊"
    elif "hello" in user_text or "hi" in user_text or "hlo" in user_text or "হ্যালো" in user_text:
        reply = "Hello there! Kemon cholche apnar din? How can I help you today? ✨"
    elif "ajker din" in user_text or "ajke" in user_text:
        reply = "Ajker din-ti khub shundor hok! Aapki kya plan hai aaj ki? 🌟"
    else:
        # ডিফল্ট বহুভাষিক রেসপন্স
        reply = (
            "Wah! Bahut badhiya baat boli aapne. 👍\n"
            "আপনার কথাটা দারুণ লেগেছে! I am here to chat with you in Bengali, English, and Hinglish. 🚀"
        )
        
    bot.reply_to(message, reply)

if __name__ == "__main__":
    keep_alive()
    print("Bot polling started...")
    bot.infinity_polling()
    
