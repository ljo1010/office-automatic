import os
from django.conf import settings
from django.core.mail import EmailMessage

def send_report_email(subject, recipients, attachments=None):
    email = EmailMessage(
        subject=subject,
        body="첨부된 오늘의 보고서를 확인하세요.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=recipients,
    )
    if attachments:
        for file in attachments:
            if os.path.exists(file):
                email.attach_file(file)

    email.send(fail_silently=False)
    return f"이메일 발송 완료 → {', '.join(recipients)}"

