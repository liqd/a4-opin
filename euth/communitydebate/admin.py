from django.contrib import admin

from euth.communitydebate import models


class TopicAdmin(admin.ModelAdmin):
    list_filter = ('module__project', 'module')


admin.site.register(models.Topic, TopicAdmin)
admin.site.register(models.TopicFileUpload)
