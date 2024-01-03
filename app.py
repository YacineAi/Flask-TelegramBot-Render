import logging
import telegram
from flask import Flask, request
from telegram.ext import Dispatcher, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Initial Flask app
app = Flask(__name__)

# Initial bot by Telegram access token
telegram_bot_token = "YOUR_TELEGRAM_BOT_TOKEN"
bot = telegram.Bot(token=telegram_bot_token)


@app.route('/callback', methods=['POST'])
def webhook_handler():
    """Set route /hook with POST method will trigger this method."""
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)

        # Update dispatcher process that handler to process this message
        dispatcher.process_update(update)
    return 'ok'


def reply_handler(bot, update):
    """Reply message."""
    update.message.reply_text("Hello World!")  # Respond with "Hello World" to any message received


# New a dispatcher for bot
dispatcher = Dispatcher(bot, None)

# Add handler for handling message, there are many kinds of message. For this handler, it particular handles text
# message.
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_handler))

if __name__ == "__main__":
    # Running server
    app.run(debug=True)
