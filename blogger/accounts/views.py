from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib.auth import login, authenticate
from .forms import CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt

@login_required
@csrf_exempt
def user_list(request):
    users = User.objects.all().order_by('username')
    
    # Pagination
    paginator = Paginator(users, 20)  # Show 10 items per page
    page_number = request.GET.get('page')  # Get the current page number
    page_obj = paginator.get_page(page_number)  # Get the page object for the current page

    context = {
        'title' : 'List of Users',
        'page_obj' : page_obj
    }

    return render(request, 'accounts/list_user.html', context=context)


@login_required
def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            form.save_m2m()
            return redirect('user-list')
    else:
        form = UserForm()
    return render(request, 'accounts/create_user.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth.models import User


@csrf_exempt
def login_view(request):

    if request.session.get('_auth_user_id'):
        return redirect('dashboard') 

    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to dashboard
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})



@login_required
def delete_user(request, user_id):
    context = {
        'title' : 'Delete',
        'message' : 'Successfully deleted the user',
    }
    try:
        blog = User.objects.get(id=user_id)
        blog.delete()
    except:
        context['message'] = 'Could not delete the user'

    return render(request, 'accounts/delete_user.html', context=context)


@login_required
@csrf_exempt
def dashboard_view(request):
    context = {
        'heading' : 'Blogs',
        'message' : 'Select the Menu from the Menu Panel'
    }

    return render(request, 'common/dashboard.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('login')