from http import HTTPStatus

from django.http import HttpResponse


def index(request):
    HTTPStatus.OK
    return HttpResponse('У меня получилось!')


def second_page(request):
    HTTPStatus.OK
    return HttpResponse('А это вторая страница')
