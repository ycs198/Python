import boto3
from botocore.exceptions import ClientError
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta

def lamdba_handler():
    print datetime.today().date()


lamdba_handler()
