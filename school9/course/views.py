from django.shortcuts import render
from datetime import datetime

# Create your views here.
def learn_django(request):
    # d = datetime.now()
    return render(request, 'course/courseone.html', {'p1': 56.24321, 'p2':56.00000, 'p3':56.37000})
