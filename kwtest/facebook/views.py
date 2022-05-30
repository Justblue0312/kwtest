from django.shortcuts import render, redirect
from django.contrib import messages

from keyword_proj.const import BEATVN_URL, THEANH28_URL, VNEX_URL
from .models import Post
from others.models import Keyword
from news.utils import get_keyword_rake
from news.forms import CommentForm
from news.models import Comment
from .utils import get_post_from_facebook_url


def getPosts(request):
    # posts = get_post_from_facebook_url(request, BEATVN_URL)
    # posts = get_post_from_facebook_url(request, THEANH28_URL)
    # posts = get_post_from_facebook_url(request, VNEX_URL)
    # for post in posts:
    #     post_model = Post(**post)
    #     post_model.save()

    lastSeenId = str('inf')
    rows = Post.objects.all().order_by('content')
    for row in rows:
        if row.content == lastSeenId:
            row.delete()
        else:
            lastSeenId = row.content

    posts = Post.objects.order_by('posted_on')[:10]

    post_kw = list()

    context = {'posts': posts, 'keywords': post_kw}

    return render(request, 'facebook/posts.html', context)


def getPost(request, pk):
    # TODO: Get spectific post
    post_obj = Post.objects.get(id=pk)

    # TODO: Use rake to extract keyword.
    lastSeenId = str('inf')
    slice_rows = Keyword.objects.all().order_by('keyword')
    for row in slice_rows:
        if row.keyword == lastSeenId:
            row.delete()
        else:
            lastSeenId = row.keyword

    paragraph = post_obj.content
    _, keywords = get_keyword_rake(request, paragraph)
    keyword_list = list()
    for keyword in keywords:
        keyword_list.append(keyword[1])
        data = {
            'keyword': keyword[1],
            'source': post_obj.post_url
        }
        keyword_obj = Keyword(**data)
        keyword_obj.save()

    # TODO: Handle a review form
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post_obj
            comment.active = True
            comment.save()
            print(comment)
            messages.success(
                request, 'Your comment was successfully submitted!')
            return redirect('article', pk=post_obj.id)

    # comment_obj = Comment.objects.get(post=post_obj)
    # comment_length = len(comment_obj)
    context = {
        'post': post_obj,
        'keywords': keyword_list[:5],
        # 'comments': comment_obj,
        # 'len': comment_length
    }
    return render(request, 'facebook/post.html', context)
