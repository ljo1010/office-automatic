import pandas as pd
from myapp.models import Employee
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # manage.py 있는 폴더
font_path = BASE_DIR / "fonts" / "NotoSansKR-VariableFont_wght.ttf"
REPORT_DIR = BASE_DIR / "reports"
REPORT_DIR.mkdir(exist_ok=True)

pdfmetrics.registerFont(TTFont("NotoSansKR", str(font_path)))

def export_to_files():
    qs = Employee.objects.all().values('name','email','department')
    df = pd.DataFrame(list(qs))
    if df.empty:
        df = pd.DataFrame(columns=['name','email','department'])

    out_dir = _report_dir()
    csv_path = out_dir / "employees.csv"
    xlsx_path = out_dir / "employees.xlsx"

    df.to_csv(csv_path, index=False, encoding='utf-8-sig')
    df.to_excel(xlsx_path, index=False)
    return f"CSV/Excel 생성 완료 → {csv_path}, {xlsx_path}"

def export_to_pdf():
    qs = Employee.objects.all().values('name','email','department')
    out_dir = _report_dir()
    pdf_path = out_dir / "employees.pdf"

    c = canvas.Canvas(str(pdf_path), pagesize=A4)
    width, height = A4

    c.setFont("NotoSansKR", 16)
    c.drawString(50, height-50, "직원 목록 (Employee List)")
    c.setFont("NotoSansKR", 12)

    y = height - 90
    line_height = 18
    for e in qs:
        line = f"{e['name']} | {e['email']} | {e['department']}"
        c.drawString(50, y, line)
        y -= line_height
        # 페이지 넘어가면 새 페이지
        if y < 50:
            c.showPage()
            c.setFont("NotoSansKR", 12)
            y = height - 50
    c.save()
    return "PDF 생성 완료"

from datetime import datetime

def _report_dir():
    today = datetime.now().strftime("%Y%m%d")
    d = REPORT_DIR / today
    d.mkdir(parents=True, exist_ok=True)
    return d




