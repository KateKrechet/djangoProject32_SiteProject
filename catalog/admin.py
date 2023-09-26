from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Genre)
# admin.site.register(Director)
# admin.site.register(Actor)
admin.site.register(AgeRate)
# admin.site.register(Status)
# admin.site.register(Film)
admin.site.register(Country)


class Actoradmin(admin.ModelAdmin):
    # в названия столбиков в панели админа
    list_display = ('fname', 'lname', 'born')
    # работают как ссылки
    list_display_links = ('fname', 'lname')


# регистрируем модель актер
admin.site.register(Actor, Actoradmin)


class Directoradmin(admin.ModelAdmin):
    # в названия столбиков в панели админа
    list_display = ('fname', 'lname')
    # работают как ссылки
    list_display_links = ('fname', 'lname')


# регистрируем модель актер
admin.site.register(Director, Directoradmin)


class KinoAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'director', 'display_actors')
    list_filter = ('status', 'genre', 'rating')
    fieldsets = (
        ('О фильме', {'fields': ('title', 'summary', 'actor')}),
        (('Рейтинг'), {'fields': ('rating', 'ager', 'status')}),
        (('Остальное'), {'fields': ('genre', 'country', 'director', 'year')}))


admin.site.register(Film, KinoAdmin)


class Stinline(admin.TabularInline):
    model = Film


class StatusAdmin(admin.ModelAdmin):
    inlines = [Stinline]


admin.site.register(Status, StatusAdmin)
