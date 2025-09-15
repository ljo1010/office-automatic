from django.core.management.base import BaseCommand
from myapp.utils import export_to_files, export_to_pdf

class Command(BaseCommand):
    help = "직원 데이터를 CSV, Excel, PDF로 내보내기"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.NOTICE(export_to_files()))
        self.stdout.write(self.style.NOTICE(export_to_pdf()))
        self.stdout.write(self.style.SUCCESS("보고서 파일 생성 완료"))