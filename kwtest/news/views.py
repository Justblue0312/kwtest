from django.http import HttpResponse
from django.shortcuts import redirect, render
from keyword_proj.const import MSN_URL
from .utils import get_keyword_rake, get_msn_content_from_url, get_msn_url_from_body_html, get_news_posts, convert_datetime
from .models import SliceNews, ArticleNews, Comment
from others.models import Keyword
from .forms import CommentForm
from django.contrib import messages


def home(request):
#     next_page_url, articles, weathers, slices = get_news_posts(MSN_URL)

#     for slice in slices:
#         publish_date = slice['publishedDateTime']
#         for item in slice['slides']:
#             slice_obj, _ = SliceNews.objects.get_or_create(title=slice['title'], body_html=item['body'])
#             slice_obj.title = item['title']
#             slice_obj.body_html = item['body']
#             slice_obj.url = get_msn_url_from_body_html(item['body'])
#             slice_obj.image_url = item['image'].get('url', '')
#             slice_obj.image_name = item['image'].get('title', '')
#             slice_obj.image_caption = item['image'].get('caption', '')
#             slice_obj.attribution = item['image'].get('attribution', '')
#             slice_obj.source = item['image'].get('source', '')
#             slice_obj.publish_date = convert_datetime(publish_date)
#             slice_obj.save()

#     lastSeenId = str('inf')
#     slice_rows = SliceNews.objects.all().order_by('title')
#     for row in slice_rows:
#         if row.title == lastSeenId:
#             row.delete()
#         else:
#             lastSeenId = row.title

#     for article in articles:
#         article_obj, _ = ArticleNews.objects.get_or_create(
#             title=article['title'])
#         article_obj.title = article['title']
#         article_obj.abstract = article['abstract']
#         article_obj.url = article['url']
#         article_obj.publish_date = convert_datetime(
#             article['publishedDateTime'])
#         article_obj.content = get_msn_content_from_url(article['url'])
#         article_obj.image_url = article['images'][0]['url']
#         article_obj.attribution = article['images'][0]['attribution']
#         article_obj.image_name = article['images'][0]['title']
#         article_obj.image_caption = article['images'][0]['caption'] if article['images'][0].get(
#             'caption') else ''
#         article_obj.source = article['images'][0]['source']
#         article_obj.reaction_count = article['reactionSummary']['totalCount']
#         article_obj.save()

#     lastSeenId = str('inf')
#     article_rows = ArticleNews.objects.all().order_by('title')
#     for row in article_rows:
#         if row.title == lastSeenId:
#             row.delete()
#         else:
#             lastSeenId = row.title

    # slice_object = SliceNews.objects.all()
    # article_object = ArticleNews.objects.all()

    # context = {'slices': slice_object, 'articles': article_object}
    # return render(request, 'news/home.html', context)
    return HttpResponse('Hello world')


def getArticleNews(request, pk):
    # TODO: Get spectific article
    artist_obj = ArticleNews.objects.get(id=pk)

    # TODO: Use rake to extract keyword.
    lastSeenId = str('inf')
    slice_rows = Keyword.objects.all().order_by('keyword')
    for row in slice_rows:
        if row.keyword == lastSeenId:
            row.delete()
        else:
            lastSeenId = row.keyword

    paragraph = artist_obj.content
    keywords, _ = get_keyword_rake(request, paragraph)
    for keyword in keywords:
        data = {
            'keyword': keyword,
            'source': artist_obj.url
        }
        keyword_obj = Keyword(**data)
        keyword_obj.save()

    # TODO: Handle a review form
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = artist_obj
            comment.active = True
            comment.save()
            print(comment)
            messages.success(
                request, 'Your comment was successfully submitted!')
            return redirect('article', pk=artist_obj.id)

    comment_obj = Comment.objects.filter(post=artist_obj)
    comment_length = len(comment_obj)

    context = {'article': artist_obj, 'keywords': keywords,
               'comments': comment_obj, 'len': comment_length, 'form': form}
    return render(request, 'news/single_article_news.html', context)
