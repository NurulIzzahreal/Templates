from django.db import models
from django.contrib.auth.models import User

class KategoriMenu(models.Model):
    nama = models.CharField(max_length=255, unique=True)
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama

class Menu(models.Model):
    nama = models.CharField(max_length=255)
    deskripsi = models.TextField()
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    kategori = models.ForeignKey(KategoriMenu, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama

class Pesanan(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    jumlah = models.PositiveIntegerField()
    total_harga = models.DecimalField(max_digits=10, decimal_places=2)
    tanggal_pesan = models.DateTimeField(auto_now_add=True)
    pelanggan = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.menu.nama} - {self.tanggal_pesan}"

class Pelanggan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alamat = models.TextField()
    nomor_telepon = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

class Pemesan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nomor_telepon = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username