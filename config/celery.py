import os
from celery import Celery

# Django 기본 설정 지정
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# Celery 앱 생성
app = Celery("config")

# settings.py에서 "CELERY_" 접두어 설정 불러오기
app.config_from_object("django.conf:settings", namespace="CELERY")

# Django의 INSTALLED_APPS 안의 tasks.py 자동 검색
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")

