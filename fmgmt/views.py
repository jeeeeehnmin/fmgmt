from django.shortcuts import render

def journal(request):
    return render(request,'journal/index.html')