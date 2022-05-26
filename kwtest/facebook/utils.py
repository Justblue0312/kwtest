# from facebook_page_scraper import Facebook_scraper
# import ast
import facebook_crawler
from datetime import date


# def getFbPostList(request, page_name, count=5, browser="chrome"):
#     facebook_ai = Facebook_scraper(page_name, count, browser)
#     json_data = facebook_ai.scrap_to_json()
#     json_data = ast.literal_eval(json_data)
#     fb_posts = list()
#     for key, value in json_data.items():
#         value['likes'] = value['reactions']['likes']
#         value['loves'] = value['reactions']['loves']
#         value['wow'] = value['reactions']['wow']
#         value['sad'] = value['reactions']['sad']
#         value['angry'] = value['reactions']['angry']
#         value['haha'] = value['reactions']['haha']
#         value['cares'] = value['reactions']['cares']
#         del (value['reactions'])
#         if len(value['image']) >= 1:
#             value['image'] = value['image'][0]

#         fb_posts.append(value)

#     return fb_posts


def get_post_from_facebook_url(request, url):
    until_date = date.today().strftime("%Y-%m-%d")
    data_in_csv = facebook_crawler.Crawl_PagePosts(
        pageurl=url, until_date=str(until_date))
    data_in_dict = data_in_csv.to_dict('records')
    fb_posts = list()
    for post in data_in_dict:
        post_dict = {
            'name': post['NAME'],
            'shares': post['SHARE_COUNT'],
            'reaction_count': post['REACTION_COUNT'],
            'comments': post['COMMENT_COUNT'],
            'content': post['MESSAGE'],
            'posted_on': post['TIME'],
            'updated_on': post['UPDATETIME'],
            'video': '',
            'image': '',
            'post_url': 'https://www.facebook.com/' + post['POSTID'],
            'likes': post['LIKE'],
            'loves': post['LOVE'],
            'wow': post['WOW'],
            'sad': post['SAD'],
            'angry': post['ANGRY'],
            'haha': post['HAHA'],
            'cares': post['CARE'],
            'post_id': post['POSTID'],
            'page_id': post['PAGEID'],
            'cursor': post['CURSOR']
        }
        fb_posts.append(post_dict)
    return fb_posts
