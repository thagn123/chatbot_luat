# telegram_bot/handlers/ocr.py
from telegram import Update
from telegram.ext import ContextTypes
from telegram_bot.utils.ocr import do_ocr as ocr_util


async def do_ocr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Ưu tiên document, nếu không có dùng ảnh
    if update.message.document:
        file = await update.message.document.get_file()
    elif update.message.photo:
        file = await update.message.photo[-1].get_file()
    else:
        return await update.message.reply_text("❗ Vui lòng gửi ảnh hoặc document để OCR.")

    # Tải file về
    path = await file.download_to_drive()
    # Chạy OCR
    text = ocr_util(path)
    # Trả kết quả
    await update.message.reply_text(f"📄 Kết quả OCR:\n{text}")
