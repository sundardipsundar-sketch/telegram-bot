import telebot

# আপনার বটের টোকেন এখানে বসানো আছে
TOKEN = '8668983865:AAFko-GOeu7_AVdSryLhhfr7yJ5twpbYWcc'

bot = telebot.TeleBot(TOKEN)

# গ্রুপে যে যা লিখবে, বট হুবহু সেটাই কপি করে পাঠিয়ে দেবে
@bot.message_handler(func=lambda message: True)
def group_everyone_copy_bot(message):
    if message.text and not message.text.startswith('/'):
        chat_id = message.chat.id
        user_text = message.text
        
        bot.send_message(chat_id, user_text)

print("Everyone Copy Bot is running 24/7...")
bot.infinity_polling()
