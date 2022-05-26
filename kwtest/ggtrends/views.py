from django.shortcuts import render
from .utils import (trendSearch, todayTrend,
                    getTheLastFiveYearsTrend,
                    trendCategories, getTheLastFiveYearsTrendDict,
                    todayTrendList)
import pandas as pd
import json
import datetime
from google_searching import ggl
from .models import YearTrend, TodayTrends, TrendPosts
from pytrends.request import TrendReq

pytrends = TrendReq()


def trends_home(request):
    titles_list = todayTrendList(request)

    TodayTrends.objects.all().delete()
    TrendPosts.objects.all().delete()
    for title in titles_list:
        todaytrend_obj = TodayTrends(trend_name=title)
        todaytrend_obj.save()
        req = ggl(title, lang='vi', max_results=3)
        for item in req:
            trendpost_obj = TrendPosts(
                trend_name=TodayTrends.objects.get(trend_name=title),
                title=item.get('title').replace('...', ''),
                link=item.get('href'),
                body=item.get('body'),
            )
            trendpost_obj.save()

    todaytrend_Obj = TodayTrends.objects.all()
    trendpost_Obj = TrendPosts.objects.all()

    context = {'todaytrends': todaytrend_Obj,
               'trendposts': trendpost_Obj}

    return render(request, 'ggtrends/trends_home.html', context)


def trend_index(request):
    date = datetime.date.today()
    year = date.strftime("%Y")

    trend_data = trendSearch(request)

    today_trend = todayTrend(request)

    fy_trend = getTheLastFiveYearsTrend(request, int(year))

    year_trends = getTheLastFiveYearsTrendDict(request, int(year))

    YearTrend.objects.all().delete()
    for year_trend in year_trends:
        yt_model = YearTrend(**year_trend)
        yt_model.save()

    cate_trend = trendCategories(request)

    context = {'trend_data': trend_data,
               'today_trend': today_trend, 'fy_trend': fy_trend, 'cate_trend': cate_trend}

    return render(request, 'ggtrends/hot_search.html', context=context)


def search(request):
    if request.method == 'POST':
        search_query = request.POST['search_query']
        keyword = pytrends.suggestions(search_query)

        df = pd.DataFrame(keyword)
        keytable = df.reset_index().to_json(orient='records')
        suggestions = []
        suggestions = json.loads(keytable)

        for item in suggestions:
            item['index'] = item['index'] + 1

        context = {'search_query': search_query, 'suggestions': suggestions}
        return render(request, 'ggtrends/search.html', context)
    else:
        context = {}
        return render(request, 'ggtrends/search.html', context)
