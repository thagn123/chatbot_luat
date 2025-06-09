from telegram import Update
from telegram.ext import ContextTypes
from telegram_bot.utils.pdf_generator import generate_deposit_sale_contract

async def soan_hop_dong_coc_mua_ban_nha_dat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    params = context.args
    # ví dụ: args = ["BênA","BênB","1000000","2025-06-01","Mô tả thửa đất"]
    doc = generate_deposit_sale_contract(params)
    await update.message.reply_document(open(doc, "rb"))
