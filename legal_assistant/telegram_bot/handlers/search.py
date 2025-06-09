from telegram import Update
from telegram.ext import ContextTypes
from telegram_bot.utils.luat_api import search_luat_bo_mon

async def search_luat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyword = " ".join(context.args)
    if not keyword:
        return await update.message.reply_text("❗ Vui lòng nhập từ khoá sau /search")
    results = search_luat_bo_mon(keyword)
    md = "|Tên|Số hiệu|Ngày ban hành|Hiệu lực|Tóm tắt|Link|\n|---|---|---|---|---|---|\n"
    for r in results:
        md += f"|{r.title}|{r.id}|{r.date}|{r.effective}|{r.summary}|[Link]({r.url})|\n"
    await update.message.reply_text(md, parse_mode="Markdown")
