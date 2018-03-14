from django.conf.urls import url
import views


urlpatterns = [
    # url(r'^$', views.admin),
    url(r'^$', views.cattery_home, name="cattery_home"),
    url(r'^cats/$', views.cattery_cats, name="cattery_cats"),
    url(r'^cat/(?P<cat_id>[0-9]+)/$', views.cattery_cat, name="cattery_cat"),
    url(r'^welcome/$', views.cattery_welcome, name="cattery_welcome"),
    url(r'^photo/$', views.cattery_photo, name="cattery_photo"),

    # /polls/
    url(r'^polls/$', views.IndexView.as_view(), name="cattery_polls_index"),
    # /polls/5/
    url(r'^polls/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="cattery_polls_detail"),
    # /polls/5/results/
    url(r'^polls/(?P<pk>[0-9]+)/results/$', views.ResultView.as_view(), name="cattery_polls_results"),
    # /polls/5/vote/
    url(r'^polls/(?P<question_id>[0-9]+)/vote/$', views.vote, name="cattery_polls_vote"),
]