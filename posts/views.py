from django.http import request
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .models import Post

# this is our create post view
@login_required
def post_create_view(request):
    if request.method == "POST":
        context = {}
        title = request.POST['title']
        content = request.POST['content']

        if title and content:
            # if create form is valid 
             user = request.user
             post = Post.objects.create(title = title, content = content, author = user)
             return redirect('posts:detail', id = post.id)
        else:
             context['error'] = "Your title and content can't be empty"
             return render(request, 'posts/create.html', context = context)

    else:
        return render(request, 'posts/create.html')



# this is to view one specific blog post
def post_detail_view(request, id):
    post = Post.objects.filter(id = id).first()
    context = {'post': post}
    return render(request, 'posts/detail.html', context = context)

# this will be to view all of our blog posts
def post_list_view(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/list.html', context = context)


# this will be to update one specific post
@login_required
def post_update_view(request, id):
    context = {}
    post = Post.objects.filter(id = id).first()
    context['post'] = post
    if request.user == post.author:
     
        if request.method == "POST":
            title = request.POST['title']
            content = request.POST['content']

            if title and content:
                # if update form is valid 
                post.title = title
                post.content = context
                post.save() 
                context['success'] = "Updated"
                return render(request, 'posts/update.html', context = context)
            else:
                context['error'] = "Your title and content can't be empty"
                return render(request, 'posts/update.html', context = context)
        else:
            return render(request, 'posts/update.html', context = context)
        
    else:
        return redirect('posts:list')


# this will be to delete one specific post
@login_required
def post_delete_view(request, id):
    post = Post.objects.filter(id=id).first()
    if request.user == post.author:
        if request.method == "POST":
            post.delete()
            return redirect('posts:list')
        else:   
            return render(request, 'posts/delete.html')
    else:
        return redirect('posts:list')
