from flask import Flask, request
from telegram import Update, ForceReply
import os

from telegram import Bot

# Replace with your Telegram bot token
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

# Create Flask app
app = Flask(__name__)

# Create bot
bot = Bot(token=TOKEN)

# Handle `/start` command and reply with "Hello World!"
@app.route("/webhook", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(), bot)
    if update.message.text == '/start':
        chat_id = update.message.chat_id
        bot.send_message(chat_id, "Hello World!", reply_markup=ForceReply())
    return "OK"

# Start Flask app
if __name__ == "__main__":
    app.run(debug=True)
