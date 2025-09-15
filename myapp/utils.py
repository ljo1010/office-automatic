import pandas as pd
from myapp.models import Employee
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # manage.py 있는 폴더
font_path = BASE_DIR / "fonts" / "NotoSansKR-VariableFont_wght.ttf"

pdfmetrics.registerFont(TTFont("NotoSansKR", str(font_path)))

def export_to_files():
    qs = Employee.objects.all().values('name','email','department')
    df = pd.DataFrame(list(qs))
    # 빈 DB 대비
    if df.empty:
        df = pd.DataFrame(columns=['name','email','department'])

    df.to_csv('employees.csv', index=False, encoding='utf-8-sig')
    df.to_excel('employees.xlsx', index=False)
    return "CSV/Excel 생성 완료"

def export_to_pdf():
    qs = Employee.objects.all().values('name','email','department')
    c = canvas.Canvas('employees.pdf', pagesize=A4)
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
