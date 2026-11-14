import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# Sizning BotFather bergan tokeningiz
TOKEN = '8683747931:AAGYLfU4vt7F1Y9WM7GkdRZaudwZCf6HilY'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# /start buyrug'i kelganda ishlaydigan funksiya
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Salom! Men sizning shaxsiy AI yordamchingizman. Menga biror narsa yozing, men javob beraman.")

# Foydalanuvchi oddiy xabar yozganda ishlaydigan funksiya
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Hozircha faqat kelgan xabarni qaytaradi (Echo)
    user_text = update.message.text
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Siz yozdingiz: {user_text}")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    # Buyruqlarni va xabarlarni ushlab qolish (Handlerlar)
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    
    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    
    print("Bot ishga tushdi...")
    application.run_polling()
