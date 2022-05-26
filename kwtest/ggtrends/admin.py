from django.contrib import admin
from .models import YearTrend, TodayTrends, TrendPosts

admin.site.register(YearTrend)
admin.site.register(TodayTrends)
admin.site.register(TrendPosts)
