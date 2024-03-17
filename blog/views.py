from django.shortcuts import render, redirect
from blog.models import Category, Post, Comment, Contact, Tag
from django.core.paginator import Paginator
from .validators import validate_contact_form


def home_view(request):
    data = request.GET
    cat = data.get('cat', None)
    page = data.get('page', 1)
    tags = Tag.objects.all()
    if cat:
        posts = Post.objects.filter(is_published=True, category_id=cat)
        d = {
            'posts': posts,
            'home': 'active',
            'tags': tags
        }
        return render(request, 'index.html', context=d)
    else:
        posts = Post.objects.filter(is_published=True)
        page_obj = Paginator(posts, 4)
        top_posts_main = Post.objects.filter(is_published=True).order_by('-views')[:3]
        top_posts = Post.objects.filter(is_published=True).order_by('-views')[3:8]
        newest_posts = Post.objects.filter(is_published=True).order_by('-created_at')[:8]
        latest_posts = Post.objects.filter(is_published=True).order_by('-created_at')[:3]
        categories = Category.objects.all()
        d = {
            'home': 'active',
            'posts': page_obj.get_page(page),
            'top_posts_main': top_posts_main,
            'categories': categories,
            'top_posts': top_posts,
            'newest_posts': newest_posts,
            'latest_posts': latest_posts,
            'tags': tags
        }
        return render(request, 'index.html', context=d)


def about_view(request):
    data = request.GET
    page = data.get('page', 1)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    latest_posts = Post.objects.filter(is_published=True).order_by('-created_at')[:3]
    top_posts = Post.objects.filter(is_published=True).order_by('-views')[2:8]
    posts = Post.objects.filter(is_published=True)
    page_obj = Paginator(posts, 4)
    newest_posts = Post.objects.filter(is_published=True).order_by('-created_at')[:6]

    d = {
        'about': 'active',
        'categories': categories,
        'latest_posts': latest_posts,
        'posts': page_obj.get_page(page),
        'top_posts': top_posts,
        'newest_posts': newest_posts,
        'tags': tags
    }
    return render(request, 'about.html', context=d)


def contact_view(request):
    latest_posts = Post.objects.filter(is_published=True).order_by('-created_at')[:3]
    categories = Category.objects.all()
    tags = Tag.objects.all()
    d = {
        'contact': 'active',
        'categories': categories,
        'latest_posts': latest_posts,
        'tags': tags
    }
    if request.method == 'POST':
        data = request.POST
        validate = validate_contact_form(data)
        if validate['Ok'] is True:
            obj = Contact.objects.create(name=data['name'],
                                         email=data['email'],
                                         phone=data['phone'],
                                         message=data['message'])
            obj.save()
            return redirect('/contact')
        d['Error'] = validate['Error']
        return render(request, 'contact.html', context=d)
    return render(request, 'contact.html', context=d)


def blog_detail_view(request, pk):
    if request.method == 'POST':
        data = request.POST
        comment = Comment.objects.create(post_id=pk, name=data["name"], email=data["email"], message=data["message"])
        comment.save()
        return redirect(f'/blog/{pk}/')
    tags = Tag.objects.all()
    top_posts_main = Post.objects.filter(is_published=True).order_by('-views')[:3]
    latest_posts = Post.objects.filter(is_published=True).order_by('-created_at')[:3]
    top_posts = Post.objects.filter(is_published=True).order_by('-views')[2:8]
    post = Post.objects.filter(id=pk).first()
    post.views += 1
    post.save(update_fields=['views'])
    comments = Comment.objects.filter(post_id=pk)
    categories = Category.objects.all()
    return render(request, 'blog-single.html',
                  {'post': post, 'comments': comments, 'categories': categories, 'latest_posts': latest_posts,
                   'top_posts': top_posts, 'tags': tags, 'top_posts_main': top_posts_main})


def category_view(request):
    latest_posts = Post.objects.filter(is_published=True).order_by('-created_at')[:3]
    categories = Category.objects.all()
    cat = request.GET.get('cat')
    tags = Tag.objects.all()
    top_posts = Post.objects.filter(is_published=True).order_by('-views')[3:8]
    if cat:
        cat_name = categories.filter(id=cat).first()
        posts = Post.objects.filter(is_published=True, category_id=cat)
        return render(request, 'category.html',
                      {'posts': posts, 'categories': categories, 'cat_name': cat_name, 'latest_posts': latest_posts,
                       'tags': tags,'top_posts':top_posts})
    else:
        posts = Post.objects.filter(is_published=True)
    return render(request, 'category.html',
                  context={'posts': posts, 'categories': categories, 'tags': tags, 'latest_posts': latest_posts,'top_posts':top_posts})


def search_view(request):
    tags = Tag.objects.all()
    latest_posts = Post.objects.filter(is_published=True).order_by('-created_at')[:3]
    newest_posts = Post.objects.filter(is_published=True).order_by('-created_at')[:6]
    if request.method == 'POST':
        query = request.POST.get('query')
        return redirect(f'/search?q={query}')
    query = request.GET.get('q')
    if query is not None and len(query) >= 1:
        posts = Post.objects.filter(is_published=True, title__icontains=query)
    else:
        posts = Post.objects.filter(is_published=True)
    return render(request, 'category.html',
                  {'latest_posts': latest_posts, 'newest_posts': newest_posts,'tags': tags, 'posts': posts,
                   'categories': Category.objects.all()})


def tag_posts_view(request, pk):
    tags = Tag.objects.all()
    latest_posts = Post.objects.filter(is_published=True).order_by('-created_at')[:3]
    categories = Category.objects.all()
    tag = Tag.objects.get(pk=pk)
    newest_posts = Post.objects.filter(is_published=True).order_by('-created_at')[:6]

    tag_posts = Post.objects.filter(tags=tag)
    return render(request, 'index.html', {'tag': tag, 'posts': tag_posts, 'categories': categories, 'tags': tags,
                                          'latest_posts': latest_posts, 'newest_posts': newest_posts})
