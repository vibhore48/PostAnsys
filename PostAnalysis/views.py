from django.shortcuts import render

# Create your views here.


def postanalysis(request):
    return render(request, 'PostAnalysis/PostAnsys.html', {})
