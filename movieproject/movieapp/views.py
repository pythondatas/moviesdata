from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import movie
from .forms import movieform

# Create your views here.
def function(request):
    movies=movie.objects.all()
    context={
        'moviedetail':movies
    }
    return render(request,"home.html",context)
def detail(request,movie_id):
    #return HttpResponse("This movie number is %s" % movie_id)
    data=movie.objects.get(id=movie_id)
    return render(request,"details.html",{'result':data})
def movie_add(request):
    if request.method=="POST":
        name=request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        movies=movie(name=name,desc=desc,year=year,img=img)
        movies.save()
    return render(request,"add.html")
def update(request,id):
    movies= movie.objects.get(id=id)
    form=movieform(request.POST or None, request.FILES,instance=movies)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movies})
def delete(request,id):
    if request.method=='POST':
        movies=movie.objects.get(id=id)
        movies.delete()
        return redirect('/')
    return render(request,'delete.html')
