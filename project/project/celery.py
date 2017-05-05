from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
import jsonrpclib
logger = get_task_logger(__name__)

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
app = Celery('project')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task()
def forecastDisease(disease_id):
    server = jsonrpclib.Server(settings.JSON_RPC_SERVER)
    server.launchDiseaseForecasting(disease_id)
    logger.info("Running Predictor")

@app.task()
def trueNegatives(disease_id):
    server = jsonrpclib.Server(settings.JSON_RPC_SERVER)
    server.launchDiseaseForecasting(disease_id)
    logger.info("Running Predictor")
