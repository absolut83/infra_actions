from django.http import HttpResponse


def index(request):
    HttpResponse.status_code = 'OK'
    return HttpResponse('У меня получилось!')


def second_page(request):
    HttpResponse.status_code = 'OK'
    return HttpResponse('А это вторая страница')
