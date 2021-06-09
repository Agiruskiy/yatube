from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Groups
from django.contrib.auth import get_user_model, get_user
from .forms import NewPost
from django.contrib.auth.decorators import login_required


# Create your views here.


def first(request):
    post_list = Post.objects.order_by('-pub_date').all()
    paginator = Paginator(post_list, 10)  # показывать по 10 записей на странице.

    page_number = request.GET.get('page')  # переменная в URL с номером запрошенной страницы
    page = paginator.get_page(page_number)  # получить записи с нужным смещением
    return render(request, 'index.html', {
        'page': page,
        'paginator': paginator
    }
                  )


def group_posts(request, slug):
    # функция get_object_or_404 получает по заданным критериям объект из базы данных
    # или возвращает сообщение об ошибке, если объект не найден
    group = get_object_or_404(Groups, slug=slug)
    post_list = Post.objects.filter(group=group).order_by('-pub_date').all()
    paginator = Paginator(post_list, 10)  # показывать по 10 записей на странице.

    page_number = request.GET.get('page')  # переменная в URL с номером запрошенной страницы
    page = paginator.get_page(page_number)  # получить записи с нужным смещением
    # Метод .filter позволяет ограничить поиск по критериям. Это аналог добавления
    # условия WHERE group_id = {group_id}
    return render(request, "group.html", {
        "group": group,
        'page': page,
        'paginator': paginator
    }
                  )


@login_required
def new_post(request):
    form = NewPost()
    return render(request, 'new_post.html', {
        'form': form
    })


def new_post_confirm(request):
    text = request.POST.get('text')
    group = request.POST.get('group')
    author = get_user(request)
    post = Post(text=text, group_id=group, author=author)
    post.save()
    return render(request, 'new_post_confirm.html')


def profile(request, username):
    users = get_object_or_404(get_user_model(), username=username)
    post_list = Post.objects.filter(author=users).order_by('-pub_date').all()
    posts = Post.objects.filter(author=users).latest('-pub_date')
    num = post_list.count()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(request, 'profile.html', {
        'users': users,
        'page': page,
        'paginator': paginator,
        'num': num,
        'posts': posts

    })


def post_view(request, username, post_id):
    get_object_or_404(get_user_model(), username=username)
    posts = get_object_or_404(Post, id=post_id)
    users = posts.author
    num = Post.objects.filter(author=users).count()

    return render(request, 'post.html', {
        'posts': posts,
        'users': users,
        'num': num
    })


@login_required
def post_edit(request, username, post_id):
    posts = Post.objects.get(id=post_id)
    if posts.author.username == username:
        form = NewPost()
        return render(request, 'post_edit.html', {
            'form': form,
            'post_id': post_id,
            'username': username
        })
    else:
        return redirect(to=request.path)
    # тут тело функции. Не забудьте проверить,
    # что текущий пользователь — это автор записи.
    # В качестве шаблона страницы редактирования укажите шаблон создания новой записи
    # который вы создали раньше (вы могли назвать шаблон иначе)


def edit_confirm(request, username, post_id):
    posts = Post.objects.get(id=post_id)
    posts.text = request.POST.get('text')
    posts.group_id = request.POST.get('group')
    posts.save()
    return redirect(to=f'../../profile/{username}')
