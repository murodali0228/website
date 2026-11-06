from django.contrib import admin

from django.contrib import admin
from .models import Barchasi

@admin.register(Barchasi)
class BarchasiAdmin(admin.ModelAdmin):
    list_display = ('ism','yozuv','email','url','intejer','kichik','katta','qiziq',
                    'floa','deci','sana','vaqt','sana_vaqt','dura','bol','file')

