from flask import Flask, request
from telegram import Update
from telegram.ext import Dispatcher, CommandHandler, ContextTypes
import os

app = Flask(__name__)
dispatcher = Dispatcher(app, None, workers=0)
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

@app.route(f'/{TOKEN}', methods=['POST'])
def respond():
    update = Update.de_json(request.json, dispatcher.bot)
    dispatcher.process_update(update)
    return 'OK'

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

dispatcher.add_handler(CommandHandler("hello", hello))

if __name__ == '__main__':
    app.run(port=5000)
