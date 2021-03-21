from django.shortcuts import render
from django.http import HttpResponse
from django.db import connections
from django.db.utils import OperationalError

# Create your views here.
def index(request):
    db_conn = connections['default']
    try:
        c = db_conn.cursor()
    except OperationalError:
        return HttpResponse("Not connected")
    else:
        return HttpResponse("Connected")