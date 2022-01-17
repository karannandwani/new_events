from firstapp.models import registration
import django
from django.db.models.functions import TruncDay
from datetime import datetime, timedelta

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yif_form.settings')
django.setup()


past_7_days = datetime.today() - timedelta(days=7)
returnn
