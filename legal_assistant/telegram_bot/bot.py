import os
import django

# Thiết lập Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "legal_assistant.settings")
django.setup()

from django.conf import settings
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

# Lấy token
TOKEN = getattr(settings, "BOT_TOKEN", os.getenv("BOT_TOKEN"))
if not TOKEN:
    raise RuntimeError("BOT_TOKEN chưa được cấu hình trong settings hoặc biến môi trường")

# Import các handler
from telegram_bot.handlers.start import start
from telegram_bot.handlers.menu import menu_handler
from telegram_bot.handlers.check_contract import check_contract
from telegram_bot.handlers.search import search_luat
from telegram_bot.handlers.template import template_contract
from telegram_bot.handlers.check_use_agreement import check_use_agreement
from telegram_bot.handlers.deposit_sale import soan_hop_dong_coc_mua_ban_nha_dat
from telegram_bot.handlers.deposit_rent import soan_hop_dong_coc_thue_nha
from telegram_bot.handlers.sale import soan_hop_dong_mua_ban_nha_dat
from telegram_bot.handlers.check_red_book import check_so_do
from telegram_bot.handlers.proxy_authorization import soan_uy_quyen
from telegram_bot.handlers.summary import summary_luat
from telegram_bot.handlers.ocr import do_ocr


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Handler cơ bản
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(menu_handler))

    # Đăng ký 11 command
    app.add_handler(CommandHandler("check_contract", check_contract))
    app.add_handler(CommandHandler("search", search_luat))
    app.add_handler(CommandHandler("template", template_contract))
    app.add_handler(CommandHandler("check_use_agreement", check_use_agreement))
    app.add_handler(CommandHandler("soạn_hợp_đồng_cọc_mua_bán_nhà_đất", soan_hop_dong_coc_mua_ban_nha_dat))
    app.add_handler(CommandHandler("soạn_hợp_đồng_cọc_thuê_nhà", soan_hop_dong_coc_thue_nha))
    app.add_handler(CommandHandler("soạn_hợp_đồng_mua_bán_nhà_đất", soan_hop_dong_mua_ban_nha_dat))
    app.add_handler(CommandHandler("check_sổ_đỏ", check_so_do))
    app.add_handler(CommandHandler("soạn_uỷ_quyền_làm_giấy_tờ_mua_bán_cọc_đất", soan_uy_quyen))
    app.add_handler(CommandHandler("summary", summary_luat))
    app.add_handler(CommandHandler("ocr", do_ocr))

    print("🚀 Telegram Bot đang chạy…")
    app.run_polling()


if __name__ == "__main__":
    main()
