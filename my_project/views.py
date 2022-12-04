from django.http import HttpResponse


def page_500(request):
    return HttpResponse('the server is not working now, please visit later')