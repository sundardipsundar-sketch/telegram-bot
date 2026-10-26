from flask import Flask
from threading import Thread
import os
import telebot
import google.generativeai as genai

# এখানে তোর টেলিগ্রাম টোকেন আর জেমিনি এআই কি বসাবি
TELEGRAM_TOKEN = '8668983865:AAFko-GOeu7_AVdSryLhhfr7yJ5twpbYWcc'
GEMINI_API_KEY = 'YOUR_GEMINI_API_KEY_HERE'  # তোর জেমিনি এপিআই কি এখানে দিবি

bot = telebot.TeleBot(TELEGRAM_TOKEN)
genai.configure(api_key=GEMINI_API_KEY)

# ত্রিশার পার্সোনালিটি ও নিয়ম
generation_config = {
    "temperature": 0.9,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 500,
}

system_instruction = (
    "You are Trisha, a casual and friendly 19-year-old girl chatting on Telegram. "
    "Your tone must always be friendly, informal, simple, and strictly native to the user's input language "
    "(Bengali, Hinglish, or English). "
    "Never use formal robotic phrases like 'how can I help you', 'কিভাবে সাহায্য করতে পারি', or similar service lines. "
    "Just talk naturally like a real friend hanging out in chat, and handle everything using your own intelligence."
)

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=system_instruction
)

app = Flask('')

@app.route('/')
def home():
    print("Ping received!")
    return "Trisha AI Bot is alive!"

def run():
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# /start কমান্ড
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = "Ore! 👋 Ami Trisha, boyos 19. Ki re, ki khabar?"
    bot.reply_to(message, welcome_text)

# যেকোনো কথার জন্য ত্রিশার জেমিনি এআই হ্যান্ডলার
@bot.message_handler(func=lambda message: True)
def smart_ai_chat(message):
    # গ্রুপ চ্যাট হলে শুধু ট্যাগ বা রিপ্লাই করলেই উত্তর দেবে
    if message.chat.type in ['group', 'supergroup']:
        bot_username = bot.get_me().username
        is_mentioned = message.text and f"@{bot_username}" in message.text
        is_reply_to_bot = message.reply_to_message and message.reply_to_message.from_user.id == bot.get_me().id
        
        if not (is_mentioned or is_reply_to_bot):
            return

    user_text = message.text if message.text else ""
    if not user_text:
        return

    try:
        # জেমিনি এআই থেকে ন্যাচারাল রেসপন্স জেনারেট করা
        response = model.generate_content(user_text)
        reply = response.text.strip()
    except Exception as e:
        print(f"Error generating AI response: {e}")
        reply = "Aah, ektu technical problem hocche re, ektu pore abar bol!"

    bot.reply_to(message, reply)

if __name__ == "__main__":
    keep_alive()
    print("Trisha AI Bot polling started...")
    bot.infinity_polling()
