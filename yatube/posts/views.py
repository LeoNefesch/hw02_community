from django.shortcuts import get_object_or_404, render

from .models import Group, Post

NUMBER_OF_ROWS: int = 10


def index(request):
    posts = Post.objects.select_related('group')[:NUMBER_OF_ROWS]
    title = 'Последние обновления на сайте'
    context = {'posts': posts, 'title': title}
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:NUMBER_OF_ROWS]
    title = 'Записи сообщества'
    context = {'group': group, 'posts': posts, 'title': title}
    return render(request, 'posts/group_list.html', context)
