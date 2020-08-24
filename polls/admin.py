from django.contrib import admin
from . import models


class QuestionAdmin(admin.ModelAdmin):
    # 필드 순서 변경
    # fields = ['pub_date', 'question_text']

    # 필드 분리
    fieldsets = [
        ('Question Statement', {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'],
                              'classes': ['collapse'],  # 필드 접기
                              }),
    ]


admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Choice)
