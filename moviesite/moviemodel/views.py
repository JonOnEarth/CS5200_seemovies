from django.http import Http404
from django.shortcuts import render
from django.shortcuts import render_to_response
#from django.http import HttpResponse
from moviemodel import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
#from django.template import Context, loader
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from omdb import OMDBClient

# Create your views here.
# homepage
def home(request):
    return render(request, 'homepage/login.html')
#log in

def signup(request):
    type = request.POST.get('type')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            group = Group.objects.get(name=type)
            user.groups.add(group)
            user.save()
            return HttpResponseRedirect('/tologin/')
    else:
        form = UserCreationForm()
    return render(request, 'signup/signup.html', {'form': form})

def acclogin(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    usercheck = authenticate(username=username, password=password)
    if usercheck is not None:
        login(request, usercheck)
        user = User.objects.get(username=username)
        dict_u = {'user': user}
        type = user.groups.all()
        dict_t = {'type': type}
        dict_all = dict(dict_u, **dict_t)
        return render(request, 'homepage/login.html', dict_all)
    else:
        return render(request, 'error/loginerror.html')

#show detail
def movieindex(request):
    allmovie = models.movie.objects.all()
    mc ={'allmovie': allmovie}
    return render(request,'movie/index.html', mc)

def membermovieindex(request,type_id,user_id):
    allmovie = models.movie.objects.all()
    dict_t ={'type_id':type_id}
    dict_m ={'allmovie': allmovie}
    dict_u ={'user_id':user_id}
    dictmerge =dict(dict_m,**dict_t)
    dictmerge2 =dict(dictmerge, **dict_u)
    return render(request,'movie/index.html', dictmerge2)


def moviedetail(request, movie_id):
    try:
        movie = models.movie.objects.get(id=movie_id)
        reviews = models.review.objects.filter(movie_id=movie_id)
    except movie.DoesNotExist:
        raise Http404("from movies does not exist")
    actorrelated = movie.actor.all()
    directorrelated = movie.director.all()
    moviecategory = movie.category.all()
    dict_m = {'movie': movie}
    dict_c = {'moviecategory': moviecategory}
    dict_a = {'actorrelated': actorrelated}
    dict_d = {'directorrelated': directorrelated}
    dict_r = {'reviews': reviews}
    dictmerge = dict(dict_m, **dict_a)
    dictmerge2 = dict(dictmerge, **dict_d)
    dictmerge3 = dict(dictmerge2, **dict_c)
    dictmerge4 = dict(dictmerge3, **dict_r)
    return render(request, 'movie/detail.html', dictmerge4)


def membermoviedetail(request, movie_id, type_id, user_id):
    try:
        movie = models.movie.objects.get(id=movie_id)
        reviews = models.review.objects.filter(movie_id=movie_id)
    except movie.DoesNotExist:
        raise Http404("from movies does not exist")
    actorrelated = movie.actor.all()
    directorrelated = movie.director.all()
    moviecategory = movie.category.all()
    dict_t = {'type_id':type_id}
    dict_m = {'movie': movie}
    dict_c = {'moviecategory': moviecategory}
    dict_a = {'actorrelated': actorrelated}
    dict_d = {'directorrelated': directorrelated}
    dict_u = {'user_id':user_id}
    dict_r = {'reviews':reviews}
    dictmerge = dict(dict_m, **dict_a)
    dictmerge2 = dict(dictmerge, **dict_d)
    dictmerge3 = dict(dictmerge2, **dict_c)
    dictmerge4 = dict(dictmerge3, **dict_t)
    dictmerge5 = dict(dictmerge4, **dict_u)
    dictmerge6 = dict(dictmerge5, **dict_r)
    return render(request, 'movie/detail.html', dictmerge6)


#create review
def createreviewpage(request,movie_id,type_id,user_id):
    dict_m ={'movie_id':movie_id}
    dict_t ={'type_id':type_id}
    dict_u ={'user_id':user_id}
    dictmerge =dict(dict_m,**dict_u)
    dictmerge1=dict(dictmerge, **dict_t)
    return render(request, 'create/createreview.html',dictmerge1)


def createreview(request, movie_id, type_id, user_id):
    content = request.GET.get('reviewcontent')
    #will be replaced by real user id later#
    newreview = models.review(movie_id=movie_id, user_id=user_id, content=content)
    newreview.save()
    return HttpResponseRedirect('/movie/'+str(movie_id)+'/type/'+str(type_id)+'/id/'+str(user_id)+'/')


#show actor
def actorindex(request):
    allactor = models.actor.objects.all()
    ac = {'allactor': allactor}
    return render(request, 'actor/index.html', ac)

def actordetail(request,actor_id):
    try:
        actor = models.actor.objects.get(id = actor_id)
    except actor.DoesNotExist:
        raise Http404("from actors does not exist")
    actmovie = actor.movie_set.all()
    dict_m= {'actmovie': actmovie}
    dict_a= {'actor': actor}
    dictmerge = dict(dict_m, **dict_a)
    return render(request, 'actor/detail.html', dictmerge)


def directorindex(request):
    alldirector = models.director.objects.all()
    dc = {'alldirector': alldirector}
    return render(request, 'director/index.html', dc)


def directordetail(request, director_id):
    try:
        director = models.director.objects.get(id = director_id)
    except director.DoesNotExist:
        raise Http404("from director does not exist")
    directmovie = director.movie_set.all()
    dict_m = {'directmovie': directmovie}
    dict_a = {'director': director}
    dictmerge = dict(dict_m, **dict_a)
    return render(request, 'director/detail.html', dictmerge)

def category(request):
    allcategory = models.category.objects.all()
    dc = {'allcategory': allcategory}
    return render(request, 'category/category_index.html', dc)


def categorydetail(request, category_id):
    try:
        category = models.category.objects.get(id=category_id)
    except category.DoesNotExist:
        raise Http404("from director does not exist")
    allmovie = category.movie_set.all()
    cd = {'allmovie': allmovie}
    return render(request, 'category/moviesInCategory.html', cd)


#movie search
def moviesearchpage(request):
    return render(request, 'search/searchmovie.html')


class Imdb_Movie:
    def __init__(self, title, poster, watchlink):
        self.title = title
        self.poster = poster
        self.watchlink = watchlink


def searchmovie(request):
    movietitle = request.GET.get('movietitle')
    if not movietitle:
        return render(request, 'error/error.html')
    movie = models.movie.objects.filter(title=movietitle)
    if not movie:
        API_KEY = '66a8c2f3'
        client = OMDBClient(apikey=API_KEY)
        movie_data = client.get(movietitle)
        allmovie = []
        for movie in movie_data:
            new_movie = Imdb_Movie(title=movie['title'], poster=movie['poster'], watchlink="https://www.imdb.com/title/"+movie['imdb_id'])
            allmovie.append(new_movie)
        cd = {'allmovie': allmovie}
        return render(request, 'error/error2.html', cd)
    else:
        moviefound = models.movie.objects.get(title=movietitle)
        return HttpResponseRedirect('/movie/'+str(moviefound.id)+'/type//id/')


#memovie search
def membermoviesearchpage(request,type_id,user_id):
    dict_t = {'type_id':type_id}
    dict_u = {'user_id':user_id}
    dictmerge= dict(dict_t,**dict_u)
    return render(request, 'search/searchmovie.html',dictmerge)


def membersearchmovie(request,type_id,user_id):
    movietitle = request.GET.get('movietitle')
    if not movietitle:
        return render(request, 'error/error.html')
    movie = models.movie.objects.filter(title=movietitle)
    if not movie:
        API_KEY = '66a8c2f3'
        client = OMDBClient(apikey=API_KEY)
        movie_data = client.get(movietitle)
        allmovie = []
        for movie in movie_data:
            new_movie = Imdb_Movie(title=movie['title'], poster=movie['poster'], watchlink="https://www.imdb.com/title/"+movie['imdb_id'])
            allmovie.append(new_movie)
        cd = {'allmovie': allmovie}
        return render(request, 'error/error2.html', cd)
    else:
        moviefound = models.movie.objects.get(title=movietitle)
        return HttpResponseRedirect('/movie/'+str(moviefound.id)+'/type/'+str(type_id)+'/id/'+str(user_id)+'/')


#actor search
def actorsearchpage(request):
    return render(request, 'search/searchactor.html')


def searchactor(request):
    actorname = request.GET.get('actorname')
    if not actorname:
        return render(request, 'error/error.html')
    actor = models.actor.objects.filter(firstname=actorname)
    if not actor:
        return render(request, 'error/error2.html')
    else:
        actorfound = models.actor.objects.get(firstname=actorname)
        return HttpResponseRedirect('/actor/'+str(actorfound.id)+'/')


def directorsearchpage(request):
    return render(request, 'search/searchdirector.html')


def searchdirector(request):
    directorname = request.GET.get('directorname')
    if not directorname:
        return render(request, 'error/error.html')
    director = models.director.objects.filter(firstname=directorname)
    if not director:
        return render(request, 'error/error2.html')
    else:
        directorfound = models.director.objects.get(firstname=directorname)
        return HttpResponseRedirect('/director/'+str(directorfound.id)+'/')

#create movie
def createmoviepage(request,user_id):
    return render(request, 'create/createmovie.html',{'user_id':user_id})


def createnewmoive(request, user_id):
    title = request.GET.get('title')
    description = request.GET.get('description')
    actorf = request.GET.get('actorf')
    actorl = request.GET.get('actorl')
    directorf = request.GET.get('directorf')
    directorl = request.GET.get('directorl')
    cate = request.GET.get('category')
    link = request.GET.get('link')
    # will be replaced by real user id later#
    if title:
        try:
            actor = models.actor.objects.get(firstname=actorf, lastname=actorl)
        except:
            actor = models.actor.objects.create(firstname=actorf, lastname=actorl)
        try:
            director = models.director.objects.get(firstname=directorf, lastname=directorl)
        except:
            director = models.director.objects.create(firstname=directorf, lastname=directorl)
        try:
            cate = models.category.objects.get(name=cate)
        except:
            cate = models.category.objects.create(name=cate)

        newmovie = models.movie.objects.create(title=title, description=description, watchlink=link)
        movie_id = newmovie.id
        newmovie.actor.add(actor)
        newmovie.director.add(director)
        newmovie.category.add(cate)
        newmovie.save()
        models.create.objects.create(movie_id=movie_id,user_id=user_id)
        return render(request, 'movie/detail.html', {'movie': newmovie})
    else:
        return HttpResponseRedirect('/login/'+str(user_id)+'/createmovie/')


def showurreview(request, user_id):
    try:
        reviews = models.review.objects.filter(user_id=user_id)
    except:
        raise Http404("from reviews does not exist")
    dict = {'reviews': reviews}
    return render(request, 'review/ownindex', dict)

def deletereview(request, review_id,user_id):
    review = models.review.objects.get(id=review_id)
    review.delete()
    return HttpResponseRedirect('/login/'+str(user_id)+'/managereview/')

def editordeletereview(request, review_id ):
    review = models.review.objects.get(id=review_id)
    review.delete()
    return HttpResponseRedirect('/login/editor/manageallreviews/')


def showurmovie(request, user_id):
    try:
        create = models.create.objects.filter(user_id=user_id)
    except:
        raise Http404("from reviews does not exist")
    dict = {'create': create}
    return render(request, 'movie/showurmovies.html', dict)


def showallreview(request):
    reviews = models.review.objects.all()
    dict = {'reviews':reviews}
    return render(request,'review/allreviews.html',dict)

def showallmovie(request):
     movies = models.movie.objects.all()
     dict = {'movies': movies}
     return render(request, 'movie/allmovies.html', dict)

def deleteurmovie(request,user_id,movie_id):
    movie = models.movie.objects.get(id=movie_id)
    movie.delete()
    return HttpResponseRedirect('/login/' + str(user_id) + '/manageurmovie/')

def editordeletemovie(request, movie_id ):
    review = models.movie.objects.get(id=movie_id)
    review.delete()
    return HttpResponseRedirect('/login/editor/manageallmovie/')



