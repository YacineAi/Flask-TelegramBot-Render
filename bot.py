from flask import Flask, request
from telegram import Update, ForceReply
from telegram.ext import Dispatcher, CommandHandler
from telegram import Bot

# Replace with your Telegram bot token
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

# Create Flask app
app = Flask(__name__)

# Create bot
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot, None, workers=0)

# Define a command handler for '/start'
def start(update, context):
    chat_id = update.message.chat_id
    bot.send_message(chat_id, "Hello World!", reply_markup=ForceReply())

# Add the command handler to the dispatcher
dispatcher.add_handler(CommandHandler("start", start))

# Endpoint for the Telegram API to send updates to
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'OK'

# Start Flask app
if __name__ == "__main__":
    app.run(debug=True)
