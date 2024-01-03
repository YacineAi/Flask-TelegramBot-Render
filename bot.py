from flask import Flask, request
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler
import os
# Replace with your Telegram bot token
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

# Create Flask app
app = Flask(__name__)

# Create bot
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

# Define a command handler for '/start'
def start(update, context):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id, "Hello World!", reply_markup=ForceReply())

# Add the command handler to the dispatcher
dispatcher.add_handler(CommandHandler("start", start))

# Endpoint for the Telegram API to send updates to
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    updater.dispatcher.process_update(update)
    return 'OK'

# Start Flask app
if __name__ == "__main__":
    app.run(debug=True)
