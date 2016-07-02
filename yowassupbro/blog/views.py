from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Post, Comment
from .forms import CommentForm, LoginForm, EmailPostForm

def post_list(request):
    all_posts = Post.publication.all()
    paginator = Paginator(all_posts, 4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,'post/list.html', {'page': page, 'posts': all_posts})

def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post, slug=post,
                                    status='publish',
                                    published__year=year,
                                    published__month=month,
                                    published__day=day)
    comments = post.comments.filter(active=True)
    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        new_comment = comment_form.save(commit=False)
        new_comment.post = post
        new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'post/detail.html', { 'post': post, 'comments': comments, 'comment_form': comment_form })

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Account disabled')
            else:
                return HttpResponse('No such user or password')
    else:
        form = LoginForm()
        return render(request, 'account/login.html', { 'form': form })

def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='publish')
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = forms.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'admin@mars.yowassupbro.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()

    return render(request, 'post/share.html', { 'post': post, 'form': form, 'sent': sent })

