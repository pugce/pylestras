# -*- coding:utf-8 -*-
from django.contrib import admin
from blog.models import Postagem


class PostagemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Postagem, PostagemAdmin)