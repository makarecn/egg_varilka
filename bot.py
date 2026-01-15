import os
import logging
from telegram import Update, WebAppInfo, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Bot token
BOT_TOKEN = os.environ.get('BOT_TOKEN', '8306259492:AAHaRzqs4UWy0vHq_HFsDL6y2pUznFcpjIw')
WEB_APP_URL = 'https://egg-varilka.onrender.com'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    keyboard = [
        [KeyboardButton(text="Открыть Варилку Яиц 🥚", web_app=WebAppInfo(url=WEB_APP_URL))]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(
        "Привет! 🥚\n\n"
        "Добро пожаловать в Варилку Яиц!\n"
        "Нажми кнопку ниже, чтобы открыть приложение:",
        reply_markup=reply_markup
    )

def main():
    """Запуск бота"""
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    
    logger.info('Бот запущен!')
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
