"""moviesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from moviemodel import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^$', views.home, name='homepage'),

    url(r'^movie/$', views.movieindex, name='movie_index'),

    url(r'^movie/type/(?P<type_id>[0-9]+)/id/(?P<user_id>[0-9]+)/$', views.membermovieindex, name='member_movie_index'),

    url(r'^movie/(?P<movie_id>[0-9]+)/type/(?P<type_id>[0-9]+)/id/(?P<user_id>[0-9]+)/$', views.membermoviedetail, name='movie_detail'),

    url(r'^movie/(?P<movie_id>[0-9]+)/type//id/$', views.moviedetail, name='movie_detail'),

    url(r'^actor/$', views.actorindex, name='actor_index'),

    url(r'^actor/(?P<actor_id>[0-9]+)/$', views.actordetail, name='actor_detail'),

    url(r'^director/$', views.directorindex, name='director_index'),

    url(r'^director/(?P<director_id>[0-9]+)/$', views.directordetail, name='director_detail'),

    url(r'^category/$', views.category, name='category_index'),

    url(r'^category/(?P<category_id>[0-9]+)/$', views.categorydetail, name='category_detail'),

    url(r'^tologin/$', views.home, name='homepage'),

    url(r'^createmovie/$', views.createmoviepage, name='movie_create_page'),

    url(r'^createmovie/finish/$', views.createnewmoive, name='movie_create'),

    url(r'^searchmovie/type/(?P<type_id>[0-9]+)/id/(?P<user_id>[0-9]+)/$', views.membermoviesearchpage, name='movie_search_page'),

    url(r'^movieresult/type/(?P<type_id>[0-9]+)/id/(?P<user_id>[0-9]+)/$', views.membersearchmovie, name='movie_search'),

    url(r'^searchmovie/$', views.moviesearchpage, name='movie_search_page'),

    url(r'^movieresult/$', views.searchmovie, name='movie_search'),

    url(r'^searchactor/$', views.actorsearchpage, name='actor_search_page'),

    url(r'^actorresult/$', views.searchactor, name='actor_search'),

    url(r'^searchdirector/$', views.directorsearchpage, name='director_search_page'),

    url(r'^directorresult/$', views.searchdirector, name='director_search'),

    url(r'^movie/(?P<movie_id>[0-9]+)/type/(?P<type_id>[0-9]+)/id/(?P<user_id>[0-9]+)/createreview/$', views.createreviewpage, name='review_create_page'),

    url(r'^movie/(?P<movie_id>[0-9]+)/type/(?P<type_id>[0-9]+)/id/(?P<user_id>[0-9]+)/reviewcreated/$', views.createreview, name='review_create'),

    url(r'^login/(?P<user_id>[0-9]+)/createmovie/$', views.createmoviepage, name='movie_create_page'),

    url(r'^login/(?P<user_id>[0-9]+)/createmovie/finish/$', views.createnewmoive, name='movie_create'),

    url(r'^login/(?P<user_id>[0-9]+)/managereview/$', views.showurreview, name='ownreview_detail'),

    url(r'^login/(?P<user_id>[0-9]+)/managereview/delete/(?P<review_id>[0-9]+)/$', views.deletereview, name='review_delete'),

    url(r'^login/(?P<user_id>[0-9]+)/manageurmovie/$', views.showurmovie, name='ownmovie_detail'),

    url(r'^login/editor/manageallreviews/$', views.showallreview, name='review_manage'),

    url(r'^login/editor/manageallreviews/delete/(?P<review_id>[0-9]+)/$', views.editordeletereview, name='review_manage'),

    url(r'^login/(?P<user_id>[0-9]+)/manageurmovie/delete/(?P<movie_id>[0-9]+)/$', views.deleteurmovie, name='movie_manage'),

    url(r'^login/editor/manageallmovie/$', views.showallmovie, name='manage_all_movie'),

    url(r'^login/editor/manageallmovie/delete/(?P<movie_id>[0-9]+)/$', views.editordeletemovie, name='movie_manage'),

    url(r'^login/$', views.acclogin, name='login_try'),

    url(r'^signup/$', views.signup, name='sign_up'),
]
