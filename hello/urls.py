from django.urls import path, re_path

from hello.views import hello_world, hello_china, hello_html, article_list, search, render_str, render_html, \
    http_request, no_data_404, article_detail, HomeView, index

urlpatterns = [
    path('python/', hello_world, name='hello_world'),
    path('china/', hello_china, name='hello_china'),
    path('html/', hello_html, name='hello_html'),
    # path('article/<int:month>/', article_list, name='article_list'),
    re_path(r'^article/(?P<month>0?[1-9]|1[012])/$', article_list, name='article_list'),
    path('search/', search, name='search'),
    path('render/str/', render_str, name='render_str'),
    path('render/html/', render_html, name='render_html'),
    path('notfound/', no_data_404, name='no_data_404'),
    path('article/<int:article_id>/', article_detail, name='article_detail'),
    path('home/', HomeView.as_view(), name='home'),
    path('index/', index, name='index'),



]
