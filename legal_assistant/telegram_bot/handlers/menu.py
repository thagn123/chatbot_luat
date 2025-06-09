from telegram import Update
from telegram.ext import ContextTypes

COMMANDS = [
    ("/check_contract", "Kiểm tra & phân tích hợp đồng"),
    ("/search", "Tìm kiếm văn bản luật"),
    ("/template", "Tải mẫu hợp đồng"),
    ("/check_use_agreement", "Kiểm tra điều khoản sử dụng"),
    ("/soạn_hợp_đồng_cọc_mua_bán_nhà_đất", "Soạn HĐ cọc mua bán nhà đất"),
    ("/soạn_hợp_đồng_cọc_thuê_nhà", "Soạn HĐ cọc thuê nhà"),
    ("/soạn_hợp_đồng_mua_bán_nhà_đất", "Soạn HĐ mua bán nhà đất"),
    ("/check_sổ_đỏ", "Kiểm tra sổ đỏ thật/giả"),
    ("/soạn_uỷ_quyền_làm_giấy_tờ_mua_bán_cọc_đất", "Soạn giấy uỷ quyền"),
    ("/summary", "Tóm tắt văn bản luật"),
    ("/ocr", "OCR ảnh văn bản pháp lý"),
]

async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    cmd = query.data
    msg = f"🛠 Bạn đã chọn: *{cmd}*\nVui lòng gửi file hoặc tham số tương ứng."
    await query.message.reply_text(msg, parse_mode="Markdown")
    await update.message.reply_text("📝 Soạn hợp đồng cọc mua bán nhà đất\n👉 Gõ /hopdongcoc để bắt đầu")

