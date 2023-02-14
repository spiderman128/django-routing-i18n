from django.urls import path, include, re_path

from myapp.views import page_list, news_list, news_detail

urlpatterns = [
    path('', page_list, name="page_list"),
    path('news', news_list, name="news_list"),
    path('news/<slug:slug>', news_detail, name="news_detail"),
    path('<slug>', page_list, name="page_tags"),
]