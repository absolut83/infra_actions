from django.http import HttpResponse


def index(request):
    HttpResponse.status_code = 'OK'
    return HttpResponse('У меня получилось!'), HttpResponse.status_code


def second_page(request):
    HttpResponse.status_code = 'OK'
    return HttpResponse('А это вторая страница'), HttpResponse.status_code
