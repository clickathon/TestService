from django.contrib import admin
from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,               {'fields': ['question_text']}),
            ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
            ('Image information', {'fields': ['image']})
                ]
    inlines = [ChoiceInline]
    #fields = ['image_tag']
    #readonly_fields = ['image_tag']

admin.site.register(Question, QuestionAdmin)
