from telegram import Update
from telegram.ext import ContextTypes
from telegram_bot.utils.luat_api import get_luat_summary

async def summary_luat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    title = " ".join(context.args)
    if not title:
        return await update.message.reply_text("❗ Vui lòng nhập tên văn bản luật sau /summary")
    report = get_luat_summary(title)
    await update.message.reply_text(report, parse_mode="Markdown")