from django.shortcuts import render


def index(request):
    return render(request, 'learning_logs_app/index.html')
