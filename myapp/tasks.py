from celery import shared_task
from myapp.utils import export_to_files, export_to_pdf
from myapp.mailer import send_report_email

@shared_task
def daily_send_reports():
    export_to_files()
    export_to_pdf()
    return send_report_email()   # 인자 없이 호출해도 OK
