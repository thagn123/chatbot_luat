# telegram_bot/utils/pdf_generator.py
"""
Module chứa các hàm tạo các file PDF/Word dựa trên đầu vào.
"""

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os
import requests

# Thư mục lưu file tạm
OUTPUT_DIR = os.path.join(os.getcwd(), 'media', 'reports')
os.makedirs(OUTPUT_DIR, exist_ok=True)


def generate_contract_report(doc_path: str) -> str:
    """
    Phân tích hợp đồng, extract điều khoản, build PDF.
    Trả về đường dẫn file PDF.
    """
    """
        Gửi hợp đồng tới Flask API để phân tích và nhận lại báo cáo PDF.
        """
    url = "http://localhost:5000/api/check_contract"
    with open(doc_path, 'rb') as f:
        files = {'file': f}
        response = requests.post(url, files=files)

    if response.status_code == 200:
        output_path = "pdfs/contract_report.pdf"
        with open(output_path, "wb") as f:
            f.write(response.content)
        return output_path
    else:
        raise Exception(f"Lỗi từ server: {response.text}")
    filename = 'report_contract.pdf'
    output_path = os.path.join(OUTPUT_DIR, filename)
    c = canvas.Canvas(output_path, pagesize=A4)
    c.drawString(50, 800, 'Báo cáo phân tích hợp đồng')
    c.drawString(50, 780, f'Nguồn: {doc_path}')
    # TODO: Thêm nội dung tóm tắt và phân tích điều khoản
    c.showPage()
    c.save()
    return output_path


def generate_use_agreement_report(text: str) -> str:
    """
    Tạo báo cáo phân tích điều khoản sử dụng.
    Trả về đường dẫn file PDF báo cáo.
    """
    filename = 'report_use_agreement.pdf'
    output_path = os.path.join(OUTPUT_DIR, filename)
    c = canvas.Canvas(output_path, pagesize=A4)
    c.drawString(50, 800, 'Báo cáo điều khoản sử dụng')
    c.drawString(50, 780, f'Nội dung: {text[:100]}...')
    # TODO: Thêm phân tích điều khoản chính, rủi ro, đề xuất
    c.showPage()
    c.save()
    return output_path


def generate_deposit_sale_contract(params: list) -> str:
    """
    Soạn hợp đồng cọc mua bán nhà đất.
    params = [BenA, BenB, so_tien_coc, han_thanh_toan, thong_tin_dat]
    Trả về đường dẫn file PDF.
    """
    filename = 'contract_deposit_sale.pdf'
    output_path = os.path.join(OUTPUT_DIR, filename)
    c = canvas.Canvas(output_path, pagesize=A4)
    c.drawString(50, 800, 'Hợp đồng đặt cọc mua bán nhà đất')
    fields = ['Bên A', 'Bên B', 'Tiền cọc', 'Hạn thanh toán', 'Thông tin thửa đất']
    y = 780
    for label, value in zip(fields, params):
        c.drawString(50, y, f'{label}: {value}')
        y -= 20
    c.showPage()
    c.save()
    return output_path


def generate_deposit_rent_contract(params: list) -> str:
    """
    Soạn hợp đồng cọc thuê nhà.
    params = [BenThue, BenChoThue, so_tien_coc, han_thanh_toan]
    Trả về đường dẫn file PDF.
    """
    filename = 'contract_deposit_rent.pdf'
    output_path = os.path.join(OUTPUT_DIR, filename)
    c = canvas.Canvas(output_path, pagesize=A4)
    c.drawString(50, 800, 'Hợp đồng đặt cọc thuê nhà')
    fields = ['Bên thuê', 'Bên cho thuê', 'Tiền cọc', 'Hạn thanh toán']
    y = 780
    for label, value in zip(fields, params):
        c.drawString(50, y, f'{label}: {value}')
        y -= 20
    c.showPage()
    c.save()
    return output_path


def generate_sale_contract(params: list) -> str:
    """
    Soạn hợp đồng mua bán nhà đất.
    params = [BenMua, BenBan, gia_tri, phuong_thuc, thong_tin_dat]
    Trả về đường dẫn file PDF.
    """
    filename = 'contract_sale.pdf'
    output_path = os.path.join(OUTPUT_DIR, filename)
    c = canvas.Canvas(output_path, pagesize=A4)
    c.drawString(50, 800, 'Hợp đồng mua bán nhà đất')
    fields = ['Bên mua', 'Bên bán', 'Giá trị hợp đồng', 'Phương thức thanh toán', 'Thông tin thửa đất']
    y = 780
    for label, value in zip(fields, params):
        c.drawString(50, y, f'{label}: {value}')
        y -= 20
    c.showPage()
    c.save()
    return output_path


def generate_proxy_authorization(params: list) -> str:
    """
    Soạn giấy uỷ quyền làm giấy tờ mua bán cọc đất.
    params = [BenUy, BenNhanUy, noi_dung]
    Trả về đường dẫn file PDF.
    """
    filename = 'proxy_authorization.pdf'
    output_path = os.path.join(OUTPUT_DIR, filename)
    c = canvas.Canvas(output_path, pagesize=A4)
    c.drawString(50, 800, 'Giấy uỷ quyền làm giấy tờ mua bán cọc đất')
    fields = ['Bên uỷ quyền', 'Bên nhận uỷ quyền', 'Nội dung uỷ quyền']
    y = 780
    for label, value in zip(fields, params):
        c.drawString(50, y, f'{label}: {value}')
        y -= 20
    c.showPage()
    c.save()
    return output_path
