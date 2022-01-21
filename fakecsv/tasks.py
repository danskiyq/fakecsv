from planeks.celery import app
from celery_progress.backend import ProgressRecorder
from .owner import gen_fake_csv


@app.task(bind=True)
def generate_fake_data(self, owner, rows):
    gen_fake_csv(owner, rows)
