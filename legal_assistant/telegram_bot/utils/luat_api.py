# telegram_bot/utils/luat_api.py
"""
Module chứa các hàm gọi API để tìm kiếm và tóm tắt văn bản luật.
"""

def search_luat_bo_mon(keyword: str):
    """
    Tìm kiếm văn bản luật theo từ khoá.
    Trả về danh sách object có thuộc tính: title, id, date, effective, summary, url
    """
    # TODO: implement logic gọi API hoặc tra DB
    class Law:
        def __init__(self, title, id, date, effective, summary, url):
            self.title = title
            self.id = id
            self.date = date
            self.effective = effective
            self.summary = summary
            self.url = url

    # Ví dụ dummy
    return [Law(
        "Luật Ví Dụ",
        "01/2020/QH14",
        "2020-06-01",
        "2020-07-01",
        "Đây là ví dụ luật mẫu tóm tắt nội dung.",
        "http://example.com/luat.pdf"
    )]


def get_templates(keyword: str):
    """
    Lấy danh sách mẫu hợp đồng theo từ khoá.
    Trả về danh sách object có thuộc tính: name, desc, link
    """
    class Template:
        def __init__(self, name, desc, link):
            self.name = name
            self.desc = desc
            self.link = link

    # TODO: tra cơ sở dữ liệu hoặc file lưu mẫu
    return [
        Template(
            "Mẫu hợp đồng A",
            "Hợp đồng A dành cho thuê/mua bán tài sản mẫu.",
            "http://example.com/a.pdf"
        )
    ]


def get_luat_summary(title: str) -> str:
    """
    Lấy tóm tắt văn bản luật.
    Trả về markdown string tóm tắt.
    """
    # TODO: implement logic
    return f"**Tóm tắt văn bản luật '{title}':** Nội dung chính, mục đích và quy định chính..."


# telegram_bot/utils/pdf_generator.py
"""
Module chứa các hàm tạo các file PDF/Word dựa trên đầu vào.
"""

def generate_contract_report(doc_path: str) -> str:
    """
    Phân tích hợp đồng, generate báo cáo PDF.
    Trả về đường dẫn file PDF.
    """
    out = "/tmp/report_contract.pdf"
    # TODO: đọc doc_path, parse, generate PDF
    return out


def generate_use_agreement_report(text: str) -> str:
    """
    Tạo báo cáo phân tích điều khoản sử dụng.
    Trả về đường dẫn file PDF báo cáo.
    """
    out = "/tmp/report_use_agreement.pdf"
    # TODO: generate báo cáo dựa trên text
    return out


def generate_deposit_sale_contract(params: list) -> str:
    """
    Soạn hợp đồng cọc mua bán nhà đất.
    params: ["BênA", "BênB", "số_tiền_cọc", "hạn_thanh_toán", "thông_tin_đất"]
    Trả về đường dẫn file PDF.
    """
    out = "/tmp/contract_deposit_sale.pdf"
    # TODO: fill template và generate
    return out


def generate_deposit_rent_contract(params: list) -> str:
    """
    Soạn hợp đồng cọc thuê nhà.
    params: ["BênThuê", "BênChoThuê", "số_tiền_cọc", "hạn_thanh_toán"]
    Trả về đường dẫn file PDF.
    """
    out = "/tmp/contract_deposit_rent.pdf"
    # TODO: fill template và generate
    return out


def generate_sale_contract(params: list) -> str:
    """
    Soạn hợp đồng mua bán nhà đất.
    params: ["BênMua", "BênBán", "giá_trị", "phương_thức", "thông_tin_đất"]
    Trả về đường dẫn file PDF.
    """
    out = "/tmp/contract_sale.pdf"
    # TODO: fill template và generate
    return out


def generate_proxy_authorization(params: list) -> str:
    """
    Soạn giấy uỷ quyền làm giấy tờ mua bán cọc đất.
    params: ["BênỦy", "BênNhậnỦy", "nội_dung_ủy_quyền"]
    Trả về đường dẫn file PDF.
    """
    out = "/tmp/proxy_authorization.pdf"
    # TODO: fill template và generate
    return out
