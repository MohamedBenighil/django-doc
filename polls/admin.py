from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline): # admin.StackedInline
    model = Choice
    extra = 3   

class QuestionAdmin(admin.ModelAdmin):
    # fields = ["pub_date", "question_text"] ==> to change the order
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]   
    list_per_page = 1

# admin.site.register(Question)
admin.site.register(Question ,QuestionAdmin)





# admin.site.register(Choice)
