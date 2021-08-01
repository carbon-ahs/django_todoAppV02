from django.contrib import admin
from .models import Question, Choice
'''
from .models import NewTableName

admin.site.register(NewTableName)
'''
admin.site.register(Question)
admin.site.register(Choice)