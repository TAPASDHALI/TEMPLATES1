from django.shortcuts import render

# Create your views here.
def fee_django(request):
    return render(request, 'fees/feesone.html', {'title':'Django Fees', 'cname':'Django', 'Charge':300})
