#from django.contrib import admin
#from polls.models import Poll
#from polls.models import Choice


#class PollAdmin(admin.ModelAdmin):
#    #fields = ['pub_date', 'question']
#    fieldsets = [
#        (None,               {'fields': ['question']}),
#        ('Date information', {'fields': ['pub_date'],'classes': ['collapse']}),
#    ]

#admin.site.register(Poll, PollAdmin)
#admin.site.register(Choice)

from django.contrib import admin
from polls.models import Choice, Poll

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
	list_display = ('question', 'pub_date', 'was_published_recently')
	fieldsets = [
	    (None,               {'fields': ['question']}),
	    ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]
	list_filter = ['pub_date']
	search_fields = ['question']

admin.site.register(Poll, PollAdmin)