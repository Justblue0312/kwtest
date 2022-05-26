from bs4 import BeautifulSoup
import requests


def getVietNamTwitterTrends(request):
    url = 'https://trends24.in/vietnam/'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')

    trend_card = soup.find_all('ol', attrs={'class': 'trend-card__list'})
    cards = trend_card[0].find_all_next('li')

    trend_list = list()
    for line in cards[0:10]:
        trend_name = line.find_next('a').text
        link = line.find_next('a').get('href')
        data_dict = {
            'trend_name': trend_name,
            'link': link
        }
        trend_list.append(data_dict)

    return trend_list


def getWorldwideTwitterTrend(request):
    url = "https://getdaytrends.com/"

    payload = {}
    headers = {
        'Cookie': 'sessionid=fuoutpgtuixobxrkzi2drltmcb9zvyuv',
        'User-Agent': 'PostmanRuntime/7.29.0'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    soup = BeautifulSoup(response.text, 'html.parser')

    sections = soup.find_all('section', attrs={'class': 'card'})
    divs_data = sections[0].find_all_next('div', attrs={'class': 'inset'})
    trend_list_raw = divs_data[0].find_all_next('td', attrs={'class': 'main'})

    twitter_list = list()
    pos = 0
    for item in trend_list_raw[0:50]:
        trend_name = item.find_next('a').text
        link = 'https://twitter.com/search?q=' + \
            item.find_next('a').get('href').replace(
                'trend', '').replace('/', '')
        count = item.find_next('span').text
        pos = pos + 1
        twitter_data = {
            'pos': pos,
            'trend_name': trend_name,
            'link': link,
            'count': count,
        }
        twitter_list.append(twitter_data)
    return twitter_list


def getOthereTrendList(request):
    url = "https://getdaytrends.com/"

    payload = {}
    headers = {
        'Cookie': 'sessionid=fuoutpgtuixobxrkzi2drltmcb9zvyuv',
        'User-Agent': 'PostmanRuntime/7.29.0'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    soup = BeautifulSoup(response.text, 'html.parser')

    sections = soup.find_all('section', attrs={'class': 'card'})
    divs_data = sections[0].find_all_next('div', attrs={'class': 'inset'})
    top_hashtag_list = divs_data[1].find_all_next(
        'td', attrs={'class': 'main'})

    top_list = list()
    num = 0
    for item in top_hashtag_list[0:10]:
        trend_name = item.find_next('a').text
        link = 'https://twitter.com/search?q=' + \
            item.find_next('a').get('href').replace(
                'trend', '').replace('/', '')
        num = num + 1
        tweets = item.find_next('td').text

        twitter_data = {
            'pos': num,
            'trend_name': trend_name,
            'link': link,
            'tweets': tweets
        }
        top_list.append(twitter_data)

    longest_list = list()

    index = 0
    for item in top_hashtag_list[10:]:
        trend_name = item.find_next('a').text
        link = 'https://twitter.com/search?q=' + \
            item.find_next('a').get('href').replace(
                'trend', '').replace('/', '')
        index = index + 1
        tweets = item.find_next('td').tex
        twitter_data = {
            'pos': index,
            'trend_name': trend_name,
            'link': link,
            'tweets': tweets
        }
        longest_list.append(twitter_data)

    return top_list, longest_list
