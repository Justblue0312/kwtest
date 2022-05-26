import requests
from bs4 import BeautifulSoup
import json
from goose3 import Goose
import dateutil.parser

from keyword_proj.const import STOPWORD_LIST
import yake
from rake_nltk import Rake
from underthesea import word_tokenize, classify


def get_news_posts(url):
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    response = json.loads(response.text)
    next_page_url = response['nextPageUrl']

    article_list = list()
    weather_list = list()
    slide_list = list()

    card_list = list()
    for section in response['sections']:
        cards = section['cards']
        for card in cards:
            if card['type'] == 'infopane':
                card_list.append(card)
            if card['type'] == 'article':
                article_list.append(card)
            if card['type'] == 'WeatherSummary':
                weather_list.append(card)
            if card['type'] == 'slideshow':
                slide_list.append(card)

    if card_list:
        for subCard in card_list[0]['subCards']:
            if subCard['type'] == 'article':
                article_list.append(subCard)

    return next_page_url, article_list, weather_list, slide_list


def get_msn_infos_from_url(url):
    g = Goose()
    article = g.extract(url=url)

    infos = article.infos
    return infos


def get_msn_content_from_url(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')

    paragraphs = soup.find_all('p')

    paragraph = ''
    for para in paragraphs[:-1]:
        paragraph += '\n' + para.text + '\n'

    return paragraph


def get_msn_url_from_body_html(body_html):
    soup = BeautifulSoup(str(body_html), 'html.parser')
    url = soup.find('a').get('href')
    return url


def convert_datetime(datetime_string):
    if datetime_string:
        convert = dateutil.parser.parse(str(datetime_string))
        return convert
    else:
        return None


def get_keyword_yake(request, text):
    stopwords = STOPWORD_LIST
    kw_extractor = yake.KeywordExtractor(lan='vi', n=2, stopwords=stopwords)
    keywords = kw_extractor.extract_keywords(text)

    kw_list = list()
    for kw in keywords:
        kw_list.append(kw)

    return kw_list


def get_keyword_rake(request, text):
    stopwords = STOPWORD_LIST
    punctuations = ".,;:?!()'\""
    r = Rake(stopwords, punctuations)
    r.extract_keywords_from_text(text)
    keywords = r.get_ranked_phrases_with_scores()
    keyword_str = str(keywords[0][1]).strip().split('-')

    return keyword_str, keywords


def get_word_tokenize(request, text):
    return word_tokenize(text, format='text')


def get_classify(request, text):
    return str(classify(text)[0])
