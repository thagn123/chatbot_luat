from telegram import Update
from telegram.ext import ContextTypes
from telegram_bot.utils.pdf_generator import generate_proxy_authorization

async def soan_uy_quyen(update: Update, context: ContextTypes.DEFAULT_TYPE):
    params = context.args
    doc = generate_proxy_authorization(params)
    await update.message.reply_document(open(doc, "rb"))
