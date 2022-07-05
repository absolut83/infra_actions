from django.http import HttpResponse


def index(request):
    HttpResponse(status=200)
    return HttpResponse('У меня получилось!')


def second_page(request):
    HttpResponse(status=200)
    return HttpResponse('А это вторая страница')
