from django.shortcuts import render,render_to_response
# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from models import Post,Comment
from django.contrib.auth.models import User
def users(request, uname):
	print "###########"
	print uname
	context = {'uname':uname}
	return render(request, 'users/users.html', context)


def myview(request,uname):
  users = User.objects.get(username=uname)
  print "okokokook"  
  print users
  print users.id
  posts = Post.objects.filter(author_id=users.id)
  post_body_list = [post.title for post in posts]
  return render_to_response('users/mytemplate.html',{'post_list': post_body_list,'uname':uname})

def viewall(request):  
  print "viewallllll"
  posts = Post.objects.all()
  post_body_list = [post.title for post in posts]
  return render_to_response('users/alltemplate.html',{'post_list': post_body_list})

def blog(request,title):  
  print "blogg"
  post = Post.objects.get(title=title)
  comments = Comment.objects.filter(post__title=title)
  print comments

  post = get_object_or_404(Post, slug=title)
  form = CommentForm(request.POST or None)
  if form.is_valid():
      comment = form.save(commit=False)
      comment.post = post
      comment.save()
      request.session["name"] = comment.name
      request.session["email"] = comment.email
      request.session["website"] = comment.website
      return redirect(request.path)
  form.initial['name'] = request.session.get('name')
  form.initial['email'] = request.session.get('email')
  form.initial['website'] = request.session.get('website')


  
  return render_to_response('users/blogtemplate.html',{'post': post,'form':form,'comment_list':comments})

def showpost(request,user,title):  
  users = User.objects.get(username=user)
  #print "##@@@@@@@@@@@@@@@@@@"
  #print users.id
  #print dir(users)
  posts = Post.objects.filter(title=title,author_id=users.id)
  print "vfvffgggfggf"
  print posts
  post_body_list = [post.text for post in posts]
  print post_body_list
  return render_to_response('users/post.html',{'post_list': post_body_list,'uname':user,'title':title})

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext

from models import Post
from forms import PostForm, CommentForm

#@user_passes_test(lambda u: u.is_superuser)
def add_post(request):
    print "nmnnjkn"
    form = PostForm(request.POST or None)
    if form.is_valid():
        print "valid formmmmm"
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect(post)
    print "invalidddd"
    return render_to_response('users/add_post.html', 
                              { 'form': form },
                              context_instance=RequestContext(request))

def view_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        request.session["name"] = comment.name
        request.session["email"] = comment.email
        request.session["website"] = comment.website
        return redirect(request.path)
    form.initial['name'] = request.session.get('name')
    form.initial['email'] = request.session.get('email')
    form.initial['website'] = request.session.get('website')
    return render_to_response('users/blog_post.html',
                              {
                                  'post': post,
                                  'form': form,
                                  'uname':request.user
                              },
                              context_instance=RequestContext(request))