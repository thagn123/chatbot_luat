from telegram import Update
from telegram.ext import ContextTypes
from telegram_bot.utils.pdf_generator import generate_use_agreement_report

async def check_use_agreement(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = " ".join(context.args) or None
    if not text:
        return await update.message.reply_text("❗ Vui lòng gửi nội dung điều khoản sử dụng hoặc text sau lệnh.")
    report = generate_use_agreement_report(text)
    await update.message.reply_document(open(report, "rb"))