from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template.context import RequestContext
#from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth
import pymongo


# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
    
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

#@login_required
def home(request):
    uri = 'mongodb://instore2:123abc@ds159050.mlab.com:59050/in-store'
    client = pymongo.MongoClient(uri)
    db = client.get_default_database()
    products = db['products']
    b = []
    a='beef'
    b = products.find({'$text': {'$search': a}})
    # print(type(b))
    for doc in b:
        doc_1 = {doc['store']}  # , doc['price'], doc['description']}

    context = {
            'doc_1': doc_1

        }

    return render(request, 'blog/home.html',{'context':context})

def search_result(request):

    if request.method == 'GET':  # If the form is submitted
        a = "a"
        search_query = request.GET.get('search_box', None)

        uri = 'mongodb://instore2:123abc@ds159050.mlab.com:59050/in-store'
        client = pymongo.MongoClient(uri)
        db = client.get_default_database()
        products = db['products']
        b = []

        b = products.find({'$text': {'$search': 'beef'}})
        # print(type(b))

        for doc in b:
            doc_1 = {doc['store']}  # , doc['price'], doc['description']}

    context = {
             'a':a,
            'doc_1': doc_1,
            'search_query':search_query
        }

    return render(request, 'templates/result.html', context)


    #webpage of detail of your hashtag
#def hashdet(request, hashtag_name):
  #  hash = get_object_or_404(Hashtag, name = hashtag_name)
   # return render(request, 'main/hashdet.html', {'hash': hash})
