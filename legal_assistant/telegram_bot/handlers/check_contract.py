from telegram import Update
from telegram.ext import ContextTypes
from telegram_bot.utils.pdf_generator import generate_contract_report

async def check_contract(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.document:
        return await update.message.reply_text("❗ Vui lòng gửi file hợp đồng.")
    file = await update.message.document.get_file()
    path = await file.download_to_drive()
    report = generate_contract_report(path)
    await update.message.reply_text("✅ Hệ thống đã phân tích xong hợp đồng. Mời bạn xem báo cáo:")

