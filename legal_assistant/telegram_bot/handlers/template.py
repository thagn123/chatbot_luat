from telegram import Update
from telegram.ext import ContextTypes
from telegram_bot.utils.luat_api import get_templates

async def template_contract(update: Update, context: ContextTypes.DEFAULT_TYPE):
    key = " ".join(context.args)
    if not key:
        return await update.message.reply_text("❗ Vui lòng nhập từ khoá sau /template")
    templates = get_templates(key)
    md = "|Tên mẫu|Mô tả|Link|\n|---|---|---|\n"
    for tpl in templates:
        md += f"|{tpl.name}|{tpl.desc}|[Tải về]({tpl.link})|\n"
    await update.message.reply_text(md, parse_mode="Markdown")