from django.contrib import admin

# Register your models here.

from .models import Question, Choice, Category

# admin.site.register(Question)
# admin.site.register(Choice)
# admin.site.register(Category)
#
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'slug', 'id')
    filter_horizontal = ('categories',)

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'votes')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
