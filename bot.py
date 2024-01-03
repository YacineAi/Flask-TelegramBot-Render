from flask import Flask, request
from telegram import Update, ForceReply
from telegram.ext import Updater, MessageHandler, Filters
import os

# Replace with your Telegram bot token
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

# Create Flask app
app = Flask(__name__)

# Update handler for Telegram
updater = Updater(token=TOKEN)

# Handle `/start` command and reply with "Hello World!"
@updater.message_handler(commands=["start"])
def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id, "Hello World!", reply_markup=ForceReply())

# Handle any message with "Hello back!"
@updater.message_handler(filters=Filters.text)
def echo(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id, f"Hello back, {update.message.text}!")

# Connect Flask app with Telegram updates
@app.route("/webhook", methods=["POST"])
def webhook():
    update = Update.from_json(request.get_json())
    updater.dispatcher.process_update(update)
    return "OK"

# Start Flask app and Telegram bot
if __name__ == "__main__":
    updater.start_polling()
    app.run(debug=True)
