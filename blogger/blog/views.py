# blog/views.py
from django.shortcuts import get_object_or_404, render, redirect
from .models import BlogPost
from .forms import BlogPostForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create a new blog post
def create_blog(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, user=request.user)  # Pass the logged-in user
        if form.is_valid():
            form.save()
            return redirect('list_blog')
    else:
        form = BlogPostForm(user=request.user)  # Pass the logged-in user
    return render(request, 'blog/create_blog.html', {'form': form})



@login_required
@csrf_exempt
def list_blog(request):
    blogs = BlogPost.objects.all()    
    # Pagination
    paginator = Paginator(blogs, 20)  # Show 10 items per page
    page_number = request.GET.get('page')  # Get the current page number
    page_obj = paginator.get_page(page_number)  # Get the page object for the current page

    context = {
        'title' : 'List of Users',
        'page_obj' : page_obj
    }

    return render(request, 'blog/list_blog.html', context=context)


@login_required
def delete_blog(request, blog_id):
    context = {
        'title' : 'Delete',
        'message' : 'Successfully deleted the blog',
    }

    try:
        blog = BlogPost.objects.get(id=blog_id)
        blog.delete()
    except:
        context['message'] = 'Could not delete the blog'

    return render(request, 'blog/delete_blog.html', context=context)
