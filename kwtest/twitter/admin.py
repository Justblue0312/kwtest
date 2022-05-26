from django.contrib import admin
from .models import VietNamTwitterTrend, WorldwideTwitterTrend, LongestTrend, TopHashtagTrend

admin.site.register(VietNamTwitterTrend)
admin.site.register(WorldwideTwitterTrend)
admin.site.register(TopHashtagTrend)
admin.site.register(LongestTrend)
