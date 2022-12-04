from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import TemplateView


def hello_world(request):
    return HttpResponse('hello world')


def hello_china(request):
    raise
    print(reverse('hello_world'))
    return HttpResponse('hello china')


def hello_html(request):
    html = """
    <html>
        <body>
            <h1 style="color:#f00">hello html</h1>
        </body>
    </html>
    """
    return HttpResponse(html)


def article_list(request, month):
    return HttpResponse(f'article: {month}')


def search(request):
    name = request.GET.get('name', '')
    print(name)
    return HttpResponse('search success')


def render_str(request):
    templ_name = 'index.html'
    html = render_to_string(template_name=templ_name)
    return HttpResponse(html)


def render_html(request):
    return render(request, 'index.html')


def http_request(request):
    # print(request.method)
    # # headers = request.META
    # # print(headers)
    # ua = request.META.get('HTTP_USER_AGENT', None)
    # print(ua)
    # return HttpResponse('response')
    user_info = {
        'name': 'Sophia',
        'age': 34
    }
    return JsonResponse(user_info)


def no_data_404(request):
    return HttpResponse('404')


def article_detail(request, article_id):
    if article_id < 1000:
        # return HttpResponseRedirect(reverse('no_data_404'))
        return redirect('/hello/notfound')

    return HttpResponse(f'article {article_id}  content')


class HomeView(TemplateView):
    template_name = 'home.html'


class Cat(object):

    def msg(self):
        return 'this is a cute cat'


def index(request):
    username = 'Sophia'
    age = 25
    img_url = '/media/images/dog.png'
    user_list = [
        {'username': 'Sophia', 'age': 34},
        {'username': 'Kate', 'age': 23},
    ]
    cat = Cat()

    return render(request, 'index.html', {
        'username': username,
        'age': age,
        'img_url': img_url,
        'user_list': user_list,
        'cat': cat,

    })
