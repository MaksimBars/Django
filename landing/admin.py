from django.contrib import admin
from landing.models import *

# Register your models here.


class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'tagline')


class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'name_second', 'text_second')


class AboutSiteAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'name_one', 'text_one', 'name_two',
                    'text_two', 'name_three', 'text_three', 'name_four', 'text_four')


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('line_one', 'line_two', 'line_three')


admin.site.register(Home, HomeAdmin),
admin.site.register(AboutMe, AboutMeAdmin),
admin.site.register(AboutSite, AboutSiteAdmin),
admin.site.register(Feedback, FeedbackAdmin),

