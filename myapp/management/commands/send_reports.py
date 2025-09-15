from django.core.management.base import BaseCommand
from myapp.utils import export_to_files, export_to_pdf
from myapp.mailer import send_report_email

class Command(BaseCommand):
    help = "보고서 파일 생성 후 이메일 발송"

    def handle(self, *args, **kwargs):
        # 보고서 생성
        msg1 = export_to_files()
        msg2 = export_to_pdf()
        self.stdout.write(self.style.NOTICE(msg1))
        self.stdout.write(self.style.NOTICE(msg2))

        # 이메일 발송
        attachments = [
            "reports/employees.csv",
            "reports/employees.xlsx",
            "reports/employees.pdf",
        ]
        result = send_report_email(
            subject="📧 자동 발송: 오늘의 직원 보고서",
            recipients=["ljo111004@naver.com"],  # 수신자 수정
            attachments=attachments,
        )
        self.stdout.write(self.style.SUCCESS(result))

