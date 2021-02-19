from django.shortcuts import render, redirect
from django import forms
from django.db import connection
from Libro.forms import InserimentoLibro
from Libro.models import *
from django.urls import reverse
from django.http import HttpResponseRedirect
from random import randrange

class objlist():
    def __Init__(self):
        self.CodLibro = ""
        self.NomeCo = ""
        self.Sede = ""
        self.NomeCa = ""
        self.NomeAu = ""                            #NomeAu è riferito alla tabella TradAutCur
        self.CognomeAu = ""
        self.NazioneAu = ""
        self.NomePo = ""
        self.CognomePo = ""
        self.NazionePo = ""
        self.NomePr = ""
        self.CognomePr = ""
        self.NazionePr = ""
        self.Straniero = False
        self.TitoloOrig = ""
        self.Titolo = ""
        self.Sottotitolo = ""
        self.AnnoEd = 0
        self.Illustrazioni = False
        self.ISBN_ISSN = ""
        self.Genere = ""
        self.NumPub = 0
        self.CopertinaRigida = False
        self.Ristampa = False
        self.nRistampa = 0
        self.Edizione = 0
        self.NumPagine = 0
        self.Curatore = False
        self.NomeTr = ""
        self.CognomeTr = ""
        self.NazioneTr = ""
        self.NomeCu = ""                            #NomeCu è riferito alla tabella TradAutCur
        self.CognomeCu = ""
        self.NazioneCu = ""
    
    def inserimento(CodLibro, NomeCo, Sede, NomeCa, NomeAu, CognomeAu, NazioneAu, NomePo, CognomePo, NazionePo, NomePr, CognomePr, NazionePr, Straniero, TitoloOrig, Titolo, Sottotitolo, AnnoEd, Illustrazioni, ISBN_ISSN, Genere, NumPub, CopertinaRigida, Ristampa, nRistampa, Edizione, NumPagine, Curatore, NomeTr, CognomeTr, NazioneTr, NomeCr, CognomeCr, NazioneCr)
        self.CodLibro = CodLibro
        self.NomeCo = NomeCo
        self.Sede = Sede
        self.NomeCa = NomeCa
        self.NomeAu = NomeAu
        self.CognomeAu = CognomeAu
        self.NazioneAu = NazioneAu
        self.NomePo = NomePo
        self.CognomePo = CognomePo
        self.NazionePo = NazionePo
        self.NomePr = NomePr
        self.CognomePr = CognomePr
        self.NazionePr = NazionePr
        self.Straniero = Straniero
        self.TitoloOrig = TitoloOrig
        self.Titolo = Titolo
        self.Sottotitolo = Sottotitolo
        self.AnnoEd = AnnoEd
        self.Illustrazioni = Illustrazioni
        self.ISBN_ISSN = ISBN_ISSN
        self.Genere = Genere
        self.NumPub = NumPub
        self.CopertinaRigida = CopertinaRigida
        self.Ristampa = Ristampa
        self.nRistampa = nRistampa
        self.Edizione = Edizione
        self.NumPagine = NumPagine
        self.Curatore = Curatore
        self.NomeTr = NomeTr
        self.CognomeTr = CognomeTr
        self.NazioneTr = NazioneTr
        self.NomeCu = NomeCu                  
        self.CognomeCu = CognomeCu
        self.NazioneCu = NazioneCu

def inserimentoHome(Titolo, Autore, Genere):
    self.Titolo = Titolo
    self.Autore = Autore
    self.Genere = Genere

def in_TradAutCur(self,dati):
    query="INSERT INTO libri_TradAutCur VALUES(%s,%s,%s,%s)"
    cod="A"+randrange(1000)
    cursor = connection.cursor()
    cursor.execute(query,[cod,dati.Nome,dati.Cognome,dati.Nazione])
    return cod


def in_PostfazionePre(self,dati):
    query="INSERT INTO libri_TradAutCur VALUES(%s,%s,%s)"
    cod="A"+randrange(1000)
    cursor = connection.cursor()
    cursor.execute(query,[cod,dati.autPostfazione,dati.autPrefazione])
    cursor.close()
    return cod

def in_Collana(self, dati):
    query="INSERT INTO libri_Collane VALUES(%s, %s)"
    cod = "C"+randrange(1000)
    cursor = connection.cursor()
    cursor.execute(query,[cod, dati.Nome,])
    cursor.close()
    return cod

def in_CasaEd(self, dati):
    query="INSERT INTO libri_CasaEditrice VALUES(%s, %s, %s)"
    cod = "E"+randrange(1000)
    cursor = connection.cursor()
    cursor.execute(query,[cod, dati.Sede, dati.Nome,])
    cursor.close()
    return cod

def inspector(dati,identificatore):
    queryes={
    "A":{"Q":"SELECT A.CodAutore FROM libri_TradAutCur A WHERE A.NomeTr=%s AND A.CognomeTr=%s AND A.Nazione=%s","D":[dati.NomeTR,dati.CognomeTR,dati.NazioneTr]},
    "P":{"Q":"SELECT A.CodAutore FROM libri_TradAutCur A WHERE A.NomeTr=%s AND A.CognomeTr=%s AND A.Nazione=%s","D":[dati.NomePre,dati.CognomePre,dati.NazionePre]},
    "E":{"Q":"SELECT E.CodCasaEd FROM CasaEditrice E WHERE E.Sede=%s AND E.NomeCa=%s","D":[dati.Sede,dati.NomeCa]}
    "O":{"Q":"SELECT O.CodCollane FROM Collane O WHERE O.NomeCo=%s","D":[dati.NomeCo,]}
    }
    query=queryes[identificatore]
    cursor = connection.cursor()
    cursor.execute(query["Q"],query["D"])
    ris=cursor.fetchone()
    if(ris.rowcount==0):
        
        if(identificatore=="A"):
            cod=in_TradAutCur(dati)
        
            elif(identificatore=="P"):
                cod=in_PostfazionePre(dati)

                elif(identificatore=="E"):
                    cod=in_CasaEd(dati)
                    
                    elif(identificatore=="O"):
                        cod=in_Collana(dati)
        return cod

    else:

        return ris[0]

    cursor.close()


def inserimento(request):
    if request.method =='GET':
        form = InserimentoLibro()
        nomiautori=[]
        cognomiautori=[]
        casaed=[]
        sedeed=[]
        for ris in libro.objects.raw("SELECT A.NomeTr,A.CognomeTr FROM libro_TradAutCur A"):
            nomiautori.append(ris.NomeAut)
            cognomiautori.append(ris.CognomeTr)

        for ris in libro.objects.raw("SELECT C.NomeCa,C.SedeCa FROM libro_CasaEd C"):
            casaed.append(ris.NomeCa)
            sedeEd.append(ris.SedeCa)
    return(render(request,"#",{'form':form,'NomiAu':nomiautori,'cognomiAu':cognomiautori,'casaEd':casaed,'sede':sedeed}))

    else:
        form = InserimentoLibro(request.POST)
        obj=objlist()

            if form.is_valid():
                NomeCo=request.POST.get("NomeCo")
                NomeCa=request.POST.get("NomeCa")
                SedeCa =request.POST.get("SedeCa")
                NomeAu=request.POST.get("NomeAu")
                CognomeAu=request.POST.get("CognomeAu")
                NazioneAu=request.POST.get("NazioneAu")
                autPostfazione=request.POST.get("autPostfazione")
                NomePost=request.POST.get("NomeAu")
                CognomPost=request.POST.get("CognomeAu")
                NazionePost=request.POST.get("NazioneAu")
                autPrefazione=request.POST.get("autPrefazione")
                NomePre=request.POST.get("NomeAu")
                CognomePre=request.POST.get("CognomeAu")
                NazionePre=request.POST.get("NazioneAu") 
                Straniero=request.POST.get("Straniero")
                TitoloOrig=request.POST.get("TitoloOrig")
                Titolo=request.POST.get("Titolo")
                Sottotitolo=request.POST.get("Sottotitolo")
                AnnoEd=request.POST.get("AnnoEd")
                Illustrazioni=request.POST.get("Illustrazioni")
                ISBN_ISSN=request.POST.get("ISBN_ISSN")
                Genere=request.POST.get("Genere")
                NumPub=request.POST.get("NumPub")
                CopertinaRigida=request.POST.get("CopertinaRigida")
                Ristampa=request.POST.get("Ristampa")
                nRistampa=request.POST.get("nRistampa")
                Edizione=request.POST.get("Edizione")
                NumPagine=request.POST.get("NumPagine")
                Curatore=request.POST.get("Curatore")
                Traduttore=request.POST.get("Traduttore")
                NomeTr=request.POST.get("NomeAu")
                CognomeTr=request.POST.get("CognomeAu")
                NazioneTr=request.POST.get("NazioneAu") 
                Critico=request.POST.get("Critico") 
                NomeC=request.POST.get("NomeAu")
                CognomeC=request.POST.get("CognomeC")
                NazioneC=request.POST.get("NazioneC")

                CodCollane=inspector({'NomeCo':NomeCo},"O")
                Cod
                







"""
def del_libro(request, Cod):

cursor = connection.cursor()

if request.method =='GET':
    cursor.execute("DELETE FROM Biblioteca_SingoliLibri WHERE CodLibro=%s", [Cod,])
    return HttpResponseRedirect(reverse('base'))
    cursor.close()
else:
    print("Errore")

def LibroDetailView(request, Cod)
    if request.method == 'GET':             #controllo seriale o non seriale
        cursor.execute("SELECT IDSeriale, IDNonseriale FROM Biblioteca_SingoliLibri WHERE CodLibro=%s", [Cod,])
        ris = cursor.fetchall()
        for record in ris:
            IDSeriale = record.IDSeriale
            IDNonseriale = record.IDNonseriale
    else:
        print("Errore")


    if request.method == 'GET':
        if IDSeriale is None:           #non seriale
            for record in libri.objects.raw("SELECT * FROM libri_NonSeriale WHERE IDNonseriale=%s", [IDNonseriale,]"):
                CodLibro = record.CodLibro
                IDCollana = record.IDCollana
                IDCasaEd = record.IDCasaEd
                IDAutoreCuratore = record.IDAutoreCuratore
                IDPostPrefazione = record.IDPostPrefazione
                Straniero = record.Straniero
                TitoloOrig = record.TitoloOrig
                Titolo = record.Titolo
                Sottotitolo = record.Sottotitolo
                AnnoEd = record.AnnoEd
                Illustrazioni = record.Illustrazioni
                ISBN = record.ISBN
                Genere = record.Genere
                NumPub = record.NumPub
                CopertinaRigida = record.CopertinaRigida
                Ristampa = record.Ristampa
                nRistampa = record.nRistampa
                Edizione = record.Edizione
                NumPagine = record.NumPagine
                Curatore = record.Curatore
                Traduttore = record.Traduttore
                Critico = record.Critico
            for record in libri.objects.raw("SELECT * FROM libri_Collane WHERE CodCollane=%s", [IDCollana]):
                NomeCo = record.NomeCo
            for record in libri.objects.raw("SELECT * FROM libri_CasaEditrice WHERE CodCasaEd=%s", [IDCasaEd]):
                Sede = record.Sede
                NomeCa = record.NomeCa
            for record in libri.objects.raw("SELECT * FROM libri_TradAutCur WHERE CodAutore=%s", [IDAutoreCuratore]):
                NomeAu = record.NomeTr
                CognomeAu = record.CognomeTr
                NazioneAu = record.CognomeTr
            for record in libri.objects.raw("SELECT * FROM libri_PostfazionePre WHERE CodPostfazione=%s", [IDPostPrefazione]):
                autPostfazione = record.autPostfazione
                autPrefazione = record.autPrefazione
            for record in libri.objects.raw("SELECT * FROM libri_TradAutCur WHERE CodAutore=%s", [Traduttore]):
                NomeTr = record.NomeTr
                CognomeTr = record.CognomeTr
                NazioneTr = record.NazioneTr
            for record in libri.objects.raw("SELECT * FROM libri_TradAutCur WHERE CodAutore=%s", [Critico]):
                NomeCu = record.NomeTr
                CognomeCu = record.CognomeTr
                NazioneCu = record.NazioneTr
            for record in libri.objecrs.raw("")

                

                elemento = objlist()
                elemento.inserimento(record.CodLibro, record.NomeCo, record.Sede, record.NomeCa, record.NomeAu, record.CognomeAu, record.NazioneAu, record.NomePo, record.CognomePo, record.NazionePo, record.NomePr, record.CognomePr, record.NazionePr, record.Straniero, record.TitoloOrig, record.Titolo, record.Sottotitolo, record.AnnoEd, record.Illustrazioni, record.ISBN, record.Genere, record.NumPub, record.CopertinaRigida, record.Ristampa, record.nRistampa, record.Edizione, record.NumPagine, record.Curatore, record.NomeTr, record.CognomeTr, record.NazioneTr, record.NomeCr, record.CognomeCr, record.NazioneCr)
            return render(request, 'dettaglio.html', {'context':elemento})
        else:                       #seriale
            for record in libri.objects.raw("SELECT * FROM libri_NonSeriale WHERE IDNonseriale=%s", [IDNonseriale,]"):
                CodLibro = record.CodLibro
                IDCollana = record.IDCollana
                IDCasaEd = record.IDCasaEd
                IDAutoreCuratore = record.IDAutoreCuratore
                IDPostPrefazione = record.IDPostPrefazione
                Straniero = record.Straniero
                TitoloOrig = record.TitoloOrig
                Titolo = record.Titolo
                Sottotitolo = record.Sottotitolo
                AnnoEd = record.AnnoEd
                Illustrazioni = record.Illustrazioni
                ISSN = record.ISSN
                Genere = record.Genere
                NumPub = record.NumPub
                CopertinaRigida = record.CopertinaRigida
                Ristampa = record.Ristampa
                nRistampa = record.nRistampa
                Edizione = record.Edizione
                NumPagine = record.NumPagine
                Curatore = record.Curatore
                Traduttore = record.Traduttore
                Critico = record.Critico
            for record in libri.objects.raw("SELECT * FROM libri_Collane WHERE CodCollane=%s", [IDCollana]):
                NomeCo = record.NomeCo
            for record in libri.objects.raw("SELECT * FROM libri_CasaEditrice WHERE CodCasaEd=%s", [IDCasaEd]):
                Sede = record.Sede
                NomeCa = record.NomeCa
            for record in libri.objects.raw("SELECT * FROM libri_TradAutCur WHERE CodAutore=%s", [IDAutoreCuratore]):
                NomeAu = record.NomeTr
                CognomeAu = record.CognomeTr
                NazioneAu = record.CognomeTr
            for record in libri.objects.raw("SELECT * FROM libri_PostfazionePre WHERE CodPostfazione=%s", [IDPostPrefazione]):
                autPostfazione = record.autPostfazione
                autPrefazione = record.autPrefazione
            
            for record in libri.objects.raw("SELECT * FROM libri_TradAutCur WHERE CodAutore=%s", [Traduttore]):
                NomeTr = record.NomeTr
                CognomeTr = record.CognomeTr
                NazioneTr = record.NazioneTr
            for record in libri.objects.raw("SELECT * FROM libri_TradAutCur WHERE CodAutore=%s", [Critico]):
                NomeCu = record.NomeTr
                CognomeCu = record.CognomeTr
                NazioneCu = record.NazioneTr




                elemento = objlist()
                elemento.inserimento(record.CodLibro, record.NomeCo, record.Sede, record.NomeCa, record.NomeAu, record.CognomeAu, record.NazioneAu, record.NomePo, record.CognomePo, record.NazionePo, record.NomePr, record.CognomePr, record.NazionePr, record.Straniero, record.TitoloOrig, record.Titolo, record.Sottotitolo, record.AnnoEd, record.Illustrazioni, record.ISSN, record.Genere, record.NumPub, record.CopertinaRigida, record.Ristampa, record.nRistampa, record.Edizione, record.NumPagine, record.Curatore, record.NomeTr, record.CognomeTr, record.NazioneTr, record.NomeCr, record.CognomeCr, record.NazioneCr)
            return render(request, 'dettaglio.html', {'context':elemento})
    else:
        print("Errore")


def HomePageViewSeriale(request):
if request.method = 'GET':
    context[]
    for record in Seriale.object.raw("SELECT Titolo, Autore, Genere FROM Biblioteca_Seriale")
        elemento = objlist()
        elemento.inserimentoHome(record.Titolo, record.Autore, record.Genere)
        context.append(elemento)
    return render(request, 'Serial.html',{'context_list':context}) 
else:
    print("Errore")


def HomePageViewNonSeriale(request):
if request.method = 'GET':
    context[]
    for record in Seriale.object.raw("SELECT Titolo, Autore, Genere FROM Biblioteca_NonSeriale")
        elemento = objlist()
        elemento.inserimentoHome(record.Titolo, record.Autore, record.Genere)
        context.append(elemento)
    return render(request, 'notSerial.html',{'context_list':context}) 
else:
    print("Errore")

"""
