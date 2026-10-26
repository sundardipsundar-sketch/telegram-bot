from flask import Flask
from threading import Thread
import os

app = Flask('')

@app.route('/')
def home():
    print("Ping received!")
    return "Bot is alive!"

def run():
    # রেন্ডার থেকে পাওয়া পোর্ট ব্যবহার করবে অথবা ডিফল্ট ৮০০০ পোর্ট ধরবে
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# আপনার মূল টেলিগ্রাম বট কোড শুরু হওয়ার আগে এটি কল করে দেবেন
if __name__ == "__main__":
    keep_alive()
    # এখানে আপনার টেলিগ্রাম বটের পোলিং কোড থাকবে (যেমন bot.infinity_polling())
    
