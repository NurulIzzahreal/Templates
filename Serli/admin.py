from django.contrib import admin
from .models import KategoriMenu
from .models import Menu
from .models import Pesanan
from .models import Pelanggan
from .models import Pemesan
# Register your models here.
admin.site.register(KategoriMenu)
admin.site.register(Menu)
admin.site.register(Pesanan)
admin.site.register(Pelanggan)
admin.site.register(Pemesan)
