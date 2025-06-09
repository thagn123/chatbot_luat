from telegram import Update
from telegram.ext import ContextTypes
from telegram_bot.utils.pdf_generator import generate_sale_contract

async def soan_hop_dong_mua_ban_nha_dat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    params = context.args
    doc = generate_sale_contract(params)
    await update.message.reply_document(open(doc, "rb"))