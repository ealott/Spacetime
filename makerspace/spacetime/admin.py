from django.contrib import admin

from .models import Room, Tool, Committee, Category, Contact, Event

# Register your models here.

admin.site.register(Room)
admin.site.register(Tool)
admin.site.register(Category)
admin.site.register(Committee)
admin.site.register(Contact)
admin.site.register(Event)
