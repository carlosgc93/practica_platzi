from django.contrib import admin
from polls.models import Question, Choice

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    fields= ["pub_date", "question_text"]
    list_display= ("question_text", "pub_date")
    list_filter= ["pub_date"]
    search_fields= ["question_text"]

class ChoiceAdmin(admin.ModelAdmin):
    list_filter= ["choice_text"]
    search_fields= ["choice_text"]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
