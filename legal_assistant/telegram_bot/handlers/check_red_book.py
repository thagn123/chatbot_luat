from telegram import Update
from telegram.ext import ContextTypes
from telegram_bot.utils.ocr import check_red_book_authenticity

async def check_so_do(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Kiểm tra sổ đỏ: ưu tiên file document, nếu không thì ảnh
    if update.message.document:
        file = await update.message.document.get_file()
    elif update.message.photo:
        file = await update.message.photo[-1].get_file()
    else:
        return await update.message.reply_text("❗ Vui lòng gửi file hoặc ảnh sổ đỏ.")

    # Tải về và kiểm tra
    path = await file.download_to_drive()
    result = check_red_book_authenticity(path)
    await update.message.reply_text(result)
