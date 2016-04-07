from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<httm><body>It is now %s.</body></html>"%now
    return HttpResponse(html)
