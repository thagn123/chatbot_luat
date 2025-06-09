from telegram import Update
from telegram.ext import ContextTypes
from telegram_bot.utils.pdf_generator import generate_deposit_rent_contract

async def soan_hop_dong_coc_thue_nha(update: Update, context: ContextTypes.DEFAULT_TYPE):
    params = context.args
    doc = generate_deposit_rent_contract(params)
    await update.message.reply_document(open(doc, "rb"))