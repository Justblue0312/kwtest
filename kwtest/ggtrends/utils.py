import json
from pytrends.request import TrendReq
import urllib.parse

pytrend = TrendReq()


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


def trendSearch(request):
    trending_df = pytrend.trending_searches(pn='vietnam')
    trend_table = trending_df.reset_index().to_json(orient='records')
    trend_data = []
    trend_data = json.loads(trend_table)

    for item in trend_data:
        item['index'] = item['index'] + 1

    return trend_data


def todayTrend(request):
    today_df = pytrend.today_searches(pn='VN')
    today_table = today_df.reset_index().to_json(orient='records')
    today_trend = []
    today_trend = json.loads(today_table)

    for item in today_trend:
        item['index'] = item['index'] + 1
        per = item['exploreLink'].find('%')
        if per > 0:
            item['exploreLink'] = urllib.parse.unquote(find_between(item['exploreLink'], "/trends/explore?q=",
                                                                    "&date=now+7-d&geo=VN").replace(
                "+", " "))

        else:
            item['exploreLink'] = find_between(item['exploreLink'], "/trends/explore?q=",
                                               "&date=now+7-d&geo=VN").replace(
                "+", " ")

    return today_trend


def todayTrendList(request):
    today_trends = todayTrend(request)
    titles_list = []
    for item in today_trends:
        title = item.get('exploreLink')
        titles_list.append(title)

    return titles_list


def getTheLastFiveYearsTrend(request, year):
    trendList = []
    for i in range(1, 7):
        year -= 1
        top_charts_df = pytrend.top_charts(year, hl='en-US', tz=300, geo='VN')
        top_charts_json = top_charts_df.reset_index().to_json(orient='records')
        trend_table = dict()
        trend_table[year] = json.loads(top_charts_json)
        trendList.append(trend_table)

    return trendList


def getTheLastFiveYearsTrendDict(request, year):
    trendList = []
    for i in range(1, 6):
        year -= 1
        top_charts_df = pytrend.top_charts(year, hl='en-US', tz=300, geo='VN')
        top_charts_json = top_charts_df.reset_index().to_json(orient='records')
        trend_table = dict()
        trend_table[year] = json.loads(top_charts_json)
        trendList.append(trend_table)

    for item in trendList:
        for key, value in item.items():
            for i in value:
                i['index'] = i['index'] + 1

    h_list = list()

    for item in trendList:
        for key, value in item.items():
            h = {
                'year_trend': key,
                'trends': list()
            }
            for i in value:
                h['trends'].append(i.get('title'))
        h_list.append(h)

    return h_list


def trendCategories(request):
    category = pytrend.categories()

    cate_dict = dict()
    for i in category['children']:
        title = i.get('name')
        sub_cate = dict()
        index = 1
        for j in i['children']:
            sub_cate[index] = j.get('name')
            index += 1

        cate_dict[title] = sub_cate

    return cate_dict
