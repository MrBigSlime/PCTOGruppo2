from django.db import models

# Create your models here.
class Collane(models.Model):
    CodCollane = models.CharField(max_length=4, primary_key=True)
    Nome = models.CharField(max_length=256)

class CasaEditrice(models.Model):
    CodCasaEd = models.CharField(max_length=4, primary_key=True)
    Sede = models.CharField(max_length=256)
    Nome = models.CharField(max_length=256)

class TradAutCur(models.Model):
    CodAutore = models.CharField(max_length=4,primary_key=True)
    Nome = models.CharField(max_length=256)
    Cognome = models.CharField(max_length=256)
    Nazione = models.CharField(max_length=256)

class PostfazionePre(models.Model):
    CodPostfazione = models.CharField(max_length=4,primary_key=True)
    autPostfazione = models.ForeignKey(TradAutCur,related_name='AutPost',on_delete = models.RESTRICT, blank=True, null=True)
    autPrefazione = models.ForeignKey(TradAutCur,related_name='AutPre',on_delete = models.RESTRICT, blank=True, null=True)

class Seriale(models.Model):
    CodLibro = models.CharField(max_length=4, primary_key=True)
    IDCollana = models.ForeignKey(Collane,on_delete=models.RESTRICT, blank=True, null=True)
    IDCasaEd = models.ForeignKey(CasaEditrice,on_delete=models.RESTRICT)
    IDAutoreCuratore = models.ForeignKey(TradAutCur,on_delete=models.RESTRICT)
    IDPostPrefazione = models.ForeignKey(PostfazionePre,on_delete=models.RESTRICT, blank=True, null=True)
    Straniero = models.BooleanField(default=False)
    TitoloOrig = models.CharField(max_length=256, blank=True, null=True)
    Titolo = models.CharField(max_length=256)
    Sottotitolo = models.CharField(max_length=256, blank=True, null=True)
    AnnoEd = models.IntegerField()
    Illustrazioni = models.BooleanField(default=False)
    ISSN = models.CharField(max_length=8)
    Genere = models.CharField(max_length=256)
    NumPub = models.IntegerField(blank=True, null=True)
    CopertinaRigida = models.BooleanField(default=False)
    Ristampa = models.BooleanField(default=False)
    nRistampa = models.IntegerField(blank=True, null=True)
    Edizione = models.IntegerField()
    NumPagine = models.IntegerField()
    Curatore = models.BooleanField(default=False)
    Traduttore = models.ForeignKey(TradAutCur,related_name='traduttoreS',on_delete = models.RESTRICT, blank=True, null=True)
    Critico = models.ForeignKey(TradAutCur,related_name='criticoS',on_delete = models.RESTRICT, blank=True, null=True)

class NonSeriale(models.Model):
    CodLibro = models.CharField(max_length=4, primary_key=True)
    IDCollana = models.ForeignKey(Collane,on_delete=models.RESTRICT, blank=True, null=True)
    IDCasaEd = models.ForeignKey(CasaEditrice,on_delete=models.RESTRICT)
    IDAutoreCuratore = models.ForeignKey(TradAutCur,on_delete=models.RESTRICT)
    IDPostPrefazione = models.ForeignKey(PostfazionePre,on_delete=models.RESTRICT, blank=True, null=True)
    Straniero = models.BooleanField(default=False)
    TitoloOrig = models.CharField(max_length=256, blank=True, null=True)
    Titolo = models.CharField(max_length=256)
    Sottotitolo = models.CharField(max_length=256, blank=True, null=True)
    AnnoEd = models.IntegerField()
    Illustrazioni = models.BooleanField(default=False)
    ISBN = models.CharField(max_length=13)
    Genere = models.CharField(max_length=256)
    NumPub = models.IntegerField(blank=True, null=True)
    CopertinaRigida = models.BooleanField(default=False)
    Ristampa = models.BooleanField(default=False)
    nRistampa = models.IntegerField(blank=True, null=True)
    Edizione = models.IntegerField()
    NumPagine = models.IntegerField()
    Curatore = models.BooleanField(default=False)
    Traduttore = models.ForeignKey(TradAutCur,related_name='traduttoreN',on_delete = models.RESTRICT, blank=True, null=True)
    Critico = models.ForeignKey(TradAutCur,related_name='criticoN',on_delete = models.RESTRICT, blank=True, null=True)

class SingoliLibri(models.Model):
    CodLibro = models.CharField(max_length = 4, primary_key = True)
    IDSeriale = models.ForeignKey(Seriale, on_delete = models.RESTRICT, null=True)
    IDNonseriale = models.ForeignKey(NonSeriale, on_delete = models.RESTRICT, null=True)

class Utenti(models.Model):
    CodUser = models.CharField(max_length = 4, primary_key = True)
    Nome = models.CharField(max_length = 256)
    Cognome = models.CharField(max_length = 256)
    Nazione = models.CharField(max_length = 256)

class Scaffale(models.Model):
    CodScaffale = models.CharField(max_length = 4, primary_key = True)
    CatScaffale = models.CharField(max_length = 256)

class Prestito(models.Model):
    CodPrestito = models.CharField(max_length = 4, primary_key = True)
    IDLibro = models.ForeignKey(SingoliLibri, on_delete = models.RESTRICT)
    IDUtente = models.ForeignKey(Utenti, on_delete = models.RESTRICT)
    Dateinizio = models.DateField()
    DataFine = models.DateField()
    Ritardo = models.BooleanField(default = False)

class Posizione(models.Model):
    CodPosizione = models.CharField(max_length = 4, primary_key = True)
    IDScaffale = models.ForeignKey(Scaffale, on_delete = models.RESTRICT)
    IDLibro = models.ForeignKey(SingoliLibri, on_delete = models.RESTRICT)