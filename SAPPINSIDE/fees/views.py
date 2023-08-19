from django.shortcuts import render

# Create your views here.
def fee_django(request):
    return render(request, 'fees/feeone.html', {'title':'Django Fee', 'cname': 'Django', 'charge': 5000})
