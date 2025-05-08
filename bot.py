import os
import logging
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot token from environment variable
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    user = update.effective_user
    welcome_message = (
        f"Привет, {user.first_name}! 👋\n\n"
        "Добро пожаловать в онлайн школу русского языка!\n\n"
        "Я помогу вам в изучении русского языка. Вот что я умею:\n"
        "• Определить ваш уровень языка\n"
        "• Записаться на урок\n"
        "• Выполнять упражнения\n"
        "• Получать домашние задания\n\n"
        "Используйте /help для получения списка команд."
    )
    await update.message.reply_text(welcome_message)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /help is issued."""
    help_text = (
        "Доступные команды:\n\n"
        "/start - Начать работу с ботом\n"
        "/help - Показать это сообщение\n"
        "/level - Определить уровень языка\n"
        "/schedule - Записаться на урок\n"
        "/exercise - Получить упражнение\n"
        "/homework - Получить домашнее задание"
    )
    await update.message.reply_text(help_text)

async def level_assessment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start the language level assessment process."""
    keyboard = [
        [
            InlineKeyboardButton("Начинающий (A1)", callback_data='level_A1'),
            InlineKeyboardButton("Базовый (A2)", callback_data='level_A2'),
        ],
        [
            InlineKeyboardButton("Средний (B1)", callback_data='level_B1'),
            InlineKeyboardButton("Продвинутый (B2)", callback_data='level_B2'),
        ],
        [
            InlineKeyboardButton("Свободный (C1)", callback_data='level_C1'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Выберите ваш текущий уровень русского языка:",
        reply_markup=reply_markup
    )

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button callbacks."""
    query = update.callback_query
    await query.answer()
    
    if query.data.startswith('level_'):
        level = query.data.split('_')[1]
        await query.edit_message_text(
            f"Вы выбрали уровень {level}. "
            "Наш преподаватель свяжется с вами для подтверждения уровня."
        )

async def schedule_lesson(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle lesson scheduling."""
    keyboard = [
        [
            InlineKeyboardButton("Понедельник", callback_data='day_1'),
            InlineKeyboardButton("Вторник", callback_data='day_2'),
        ],
        [
            InlineKeyboardButton("Среда", callback_data='day_3'),
            InlineKeyboardButton("Четверг", callback_data='day_4'),
        ],
        [
            InlineKeyboardButton("Пятница", callback_data='day_5'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Выберите день для урока:",
        reply_markup=reply_markup
    )

def main():
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("level", level_assessment))
    application.add_handler(CommandHandler("schedule", schedule_lesson))
    application.add_handler(CallbackQueryHandler(button_callback))

    # Start the Bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main() 