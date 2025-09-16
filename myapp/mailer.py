import os
from datetime import datetime
from pathlib import Path
from django.conf import settings
from django.core.mail import EmailMessage

BASE_DIR = Path(settings.BASE_DIR)

def today_report_paths():
    d = BASE_DIR / "reports" / datetime.now().strftime("%Y%m%d")
    return [p for p in (d / "employees.csv", d / "employees.xlsx", d / "employees.pdf") if p.exists()]

def send_report_email(
    subject: str = "📧 자동 발송: 오늘의 직원 보고서",
    recipients: list[str] | None = None,
    attachments: list[Path] | None = None,
    body: str = "첨부된 오늘의 보고서를 확인하세요."
):
    # 수신자 기본값: settings.REPORT_RECIPIENTS
    if recipients is None:
        recipients = getattr(settings, "REPORT_RECIPIENTS", [])
    if not recipients:
        raise ValueError("수신자 목록이 비어 있습니다. settings.REPORT_RECIPIENTS 를 설정하세요.")

    # 첨부 기본값: 오늘 생성된 보고서들
    if attachments is None:
        attachments = today_report_paths()

    email = EmailMessage(
        subject=subject,
        body=body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=recipients,
    )
    for f in attachments:
        email.attach_file(str(f))

    email.send(fail_silently=False)
    return f"이메일 발송 완료 → {', '.join(recipients)}"
