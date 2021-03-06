from django.contrib import admin
from .models import Assesment, Question, Result, Answer
# Register your models here.

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    #readonly_fields = ['user', 'transaction_type', 'transaction_date']
    #verbose_name = 'Staff'
    #verbose_name_plural = 'Staffs'
    
    
class AssesmentAdmin(admin.ModelAdmin):
    #fieldsets = [ (None, {'fields': ['title'}) ]
    inlines = [ QuestionInline ]
    

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1
    
    
class ResultAdmin(admin.ModelAdmin):
    #fieldsets = [ (None, {'fields': ['title'}) ]
    inlines = [ AnswerInline ]
    
    
#admin.site.unregister(Assesment)
admin.site.register(Assesment, AssesmentAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(Answer)
admin.site.register(Question)