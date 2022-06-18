from django.db import models

# Create your models here.

class Belge(models.Model):
    belge_basligi = models.CharField(max_length=200)
    bagli_olunan_holding = models.CharField(max_length=200)
    firma_unvani = models.CharField(max_length=200)
    is_yeri_adresi = models.CharField(max_length=200)
    merkezi_adres = models.CharField(max_length=200)
    mersis_no = models.CharField(max_length=200)
    sanayi_sicil_no = models.CharField(max_length=200)
    tescilli_marka = models.CharField(max_length=200)
    ticaret_sicil_no = models.CharField(max_length=200)
    vergi_daire_no = models.CharField(max_length=200)
    guncelleme_tarihi = models.DateTimeField(auto_now_add=True)
	

    def __str__(self):
        return self.belge_basliği