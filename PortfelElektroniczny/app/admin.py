from django.contrib import admin
from .models import Post, Wallet, Dochod, DochodCategory, WydatekCategory, Wydatek

admin.site.register(Post)
admin.site.register(Wallet)
admin.site.register(Dochod)
admin.site.register(DochodCategory)
admin.site.register(WydatekCategory)
admin.site.register(Wydatek)