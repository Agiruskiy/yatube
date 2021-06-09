from django.contrib import admin
from .models import Post, Groups


class PostAdmin(admin.ModelAdmin):
    # перечисляем поля, которые должны отображаться в админке
    list_display = ("text", "pub_date", "author")
    # добавляем интерфейс для поиска по тексту постов
    search_fields = ("text",)
    # добавляем возможность фильтрации по дате
    list_filter = ("pub_date",)
# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Groups)