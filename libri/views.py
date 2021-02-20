from django.shortcuts import render, redirect
from django import forms
from django.db import connection
from libri.forms import InserimentoLibro
from libri.models import *
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
    
    def inserimento(self,CodLibro, NomeCo, Sede, NomeCa, NomeAu, CognomeAu, NazioneAu, NomePo, CognomePo, NazionePo, NomePr, CognomePr, NazionePr, Straniero, TitoloOrig, Titolo, Sottotitolo, AnnoEd, Illustrazioni, ISBN_ISSN, Genere, NumPub, CopertinaRigida, Ristampa, nRistampa, Edizione, NumPagine, Curatore, NomeTr, CognomeTr, NazioneTr, NomeCr, CognomeCr, NazioneCr):
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

    def inserimentoHome(self,Titolo, Autore, Genere):
        self.Titolo = Titolo
        self.Autore = Autore
        self.Genere = Genere

def in_TradAutCur(self,dati):
    query="INSERT INTO libri_TradAutCur VALUES(%s,%s,%s,%s)"
    cod="A"+randrange(1000)
    cursor = connection.cursor()
    cursor.execute(query,[cod,dati.NomeTr,dati.CognomeTr,dati.NazioneTr])
    return cod


def in_PostfazionePre(self,dati):
    cursor = connection.cursor()

    ris=cursor.excute("SELECT A.CodAutore FROM libri_TradAutCur A WHERE A.NomeTr=%s AND A.CognomeTr=%s AND A.Nazione=%s",[dati.NomePre,dati.CognomePre,dati.NazionePre])
    if ris.rowcount==0:
       autPrefazione=in_TradAutCur({"Nome":dati.NomePre,"Cognome":dati.CognomePre,"Nazione":dati.NazionePre})

    ris=cursor.excute("SELECT A.CodAutore FROM libri_TradAutCur A WHERE A.NomeTr=%s AND A.CognomeTr=%s AND A.Nazione=%s",[dati.NomePost,dati.CognomePost,dati.NazionePost])
    if ris.rowcount==0:
        autPostfazione=in_TradAutCur({"Nome":dati.NomePre,"Cognome":dati.CognomePre,"Nazione":dati.NazionePre})
    

    query="INSERT INTO libri_TradAutCur VALUES(%s,%s,%s)"
    cod="P"+randrange(1000)
    cursor.execute(query,[cod,autPostfazione,autPrefazione])
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

def inspector(self,dati,identificatore):
    queryes={
    "A":{"Q":"SELECT A.CodAutore FROM libri_TradAutCur A WHERE A.NomeTr=%s AND A.CognomeTr=%s AND A.Nazione=%s","D":[dati.NomeTR,dati.CognomeTR,dati.NazioneTr]},
    "P":{"Q":"SELECT A.CodAutore FROM libri_TradAutCur A WHERE A.NomeTr=%s AND A.CognomeTr=%s AND A.Nazione=%s","D":[dati.NomePre,dati.CognomePre,dati.NazionePre]},
    "PP":{"Q":"SELECT A.CodAutore FROM libri_TradAutCur A WHERE A.NomeTr=%s AND A.CognomeTr=%s AND A.Nazione=%s","D":[dati.NomePost,dati.CognomePost,dati.NazionePost]},
    "E":{"Q":"SELECT E.CodCasaEd FROM CasaEditrice E WHERE E.Sede=%s AND E.NomeCa=%s","D":[dati.Sede,dati.NomeCa]},
    "O":{"Q":"SELECT O.CodCollane FROM Collane O WHERE O.NomeCo=%s","D":[dati.NomeCo,]}
    }
    query=queryes[identificatore]
    cursor = connection.cursor()
    cursor.execute(query["Q"],query["D"])
    ris=cursor.fetchone()
    if(ris.rowcount==0):
        
        if(identificatore=="A"):
            cod=in_TradAutCur(dati)
        
        if(identificatore=="P"):
            cod=in_PostfazionePre(dati)

        if(identificatore=="E"):
            cod=in_CasaEd(dati)
                    
        if(identificatore=="O"):
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
        for ris in TradAutCur.objects.raw("SELECT A.NomeTr,A.CognomeTr,A.CodAutore FROM libri_TradAutCur A"):
            nomiautori.append(ris.NomeAut)
            cognomiautori.append(ris.CognomeTr)

        for ris in CasaEditrice.objects.raw("SELECT C.NomeCa,C.Sede,C.CodCasaEd FROM libri_CasaEditrice C"):
            casaed.append(ris.NomeCa)
            sedeed.append(ris.SedeCa)
        return(render(request,"inserimento.html",{'form':form,'NomiAu':nomiautori,'cognomiAu':cognomiautori,'casaEd':casaed,'sede':sedeed}))

    else:
        form = InserimentoLibro(request.POST)
        obj=objlist()

        if form.is_valid():
            identificatore=request.POST.get("IsSerial")
            NomeCo=request.POST.get("NomeCo")
            NomeCa=request.POST.get("NomeCa")
            SedeCa =request.POST.get("SedeCa")

            NomeAu=request.POST.get("NomeAu")
            CognomeAu=request.POST.get("CognomeAu")
            NazioneAu=request.POST.get("NazioneAu")

            NomePost=request.POST.get("NomePost")
            CognomePost=request.POST.get("CognomePost")
            NazionePost=request.POST.get("NazionePost")

            NomePre=request.POST.get("NomePre")
            CognomePre=request.POST.get("CognomePre")
            NazionePre=request.POST.get("NazionePre") 

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

            #Dati Critico
            NomeTr=request.POST.get("NomeTr")
            CognomeTr=request.POST.get("CognomeTr")
            NazioneTr=request.POST.get("NazioneTr") 

            #Dati Critico
            NomeC=request.POST.get("NomeC")
            CognomeC=request.POST.get("CognomeC")
            NazioneC=request.POST.get("NazioneC")

            CodCollane=inspector({'NomeCo':NomeCo},"O")
            CodCasaEd=inspector({'Sede':SedeCa,'NomeCa':NomeCa},"E")
            CodAutore=inspector({'NomeTr':NomeAu ,',CognomeTr':CognomeAu ,'NazioneTr':NazioneAu},"A")
            CodPost=inspector({'NomePost':NomePost ,',CognomePost':CognomePost ,'NazionePost':NazionePost,'NomePre':NomePre ,',CognomePre':CognomePre ,'NazionePre':NazionePre},"P")
            CodTrad=inspector({'NomeTr':NomeTr ,',CognomeTr':CognomeTr,'NazioneTr':NazioneTr},"A")
            CodCri=inspector({'NomeTr':NomeC ,',CognomeTr':CognomeC,'NazioneTr':NazioneC},"A")

            if identificatore==False:
                query="INSERT INTO NonSeriale VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cod="N"+randrange(1000)
                Dati=[cod,CodCollane,CodCasaEd,CodAutore,CodPost,Straniero,TitoloOrig,Titolo,Sottotitolo,AnnoEd,Illustrazioni,ISBN_ISSN,Genere,NumPub,CopertinaRigida,Ristampa,nRistampa,Edizione,NumPagine,Curatore,CodTrad,CodCri]
                cursor = connection.cursor()
                cursor.execute(query,Dati)
                
            if identificatore==True:
                query="INSERT INTO Seriale VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cod="N"+randrange(1000)
                Dati=[cod,CodCollane,CodCasaEd,CodAutore,CodPost,Straniero,TitoloOrig,Titolo,Sottotitolo,AnnoEd,Illustrazioni,ISBN_ISSN,Genere,NumPub,CopertinaRigida,Ristampa,nRistampa,Edizione,NumPagine,Curatore,CodTrad,CodCri]
                cursor = connection.cursor()
                cursor.execute(query,Dati)
        return HttpResponseRedirect(reverse('base'))



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
            for record in libri.objects.raw("SELECT * FROM libri_TradAutCur WHERE CodAutore=%s", [Traduttore]):
                NomeTr = record.NomeTr
                CognomeTr = record.CognomeTr
                NazioneTr = record.NazioneTr
            for record in libri.objects.raw("SELECT * FROM libri_TradAutCur WHERE CodAutore=%s", [Critico]):
                NomeCu = record.NomeTr
                CognomeCu = record.CognomeTr
                NazioneCu = record.NazioneTr
            for record in libri.objecrs.raw("SELECT n.NomeTr, n.CognomeTr, n.NazioneTr FROM libri_TradAutCur t, libri_PostfazionePre p, libri_NonSeriale n JOIN libri_PostfazionePre ON p.autPostfazione = t.CodAutore JOIN libri_NonSeriale ON p.CodAutore = n.IDPostPrefazione ")
                NomePo = record.NomeTr
                CognomePo = record.CognomeTr
                NazionePo = record.NazioneTr 
            for record in libri.objecrs.raw("SELECT n.NomeTr, n.CognomeTr, n.NazioneTr FROM libri_TradAutCur t, libri_PostfazionePre p, libri_NonSeriale n JOIN libri_PostfazionePre ON p.autPrefazione = t.CodAutore JOIN libri_NonSeriale ON p.CodAutore = n.IDPostPrefazione ")
                NomePr = record.NomeTr
                CognomePr = record.CognomeTr
                NazionePr = record.NazioneTr    



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
            for record in libri.objects.raw("SELECT * FROM libri_TradAutCur WHERE CodAutore=%s", [Traduttore]):
                NomeTr = record.NomeTr
                CognomeTr = record.CognomeTr
                NazioneTr = record.NazioneTr
            for record in libri.objects.raw("SELECT * FROM libri_TradAutCur WHERE CodAutore=%s", [Critico]):
                NomeCu = record.NomeTr
                CognomeCu = record.CognomeTr
                NazioneCu = record.NazioneTr
            for record in libri.objecrs.raw("SELECT n.NomeTr, n.CognomeTr, n.NazioneTr FROM libri_TradAutCur t, libri_PostfazionePre p, libri_NonSeriale n JOIN libri_TradAutCur ON p.autPostfazione = t.CodAutore JOIN libri_NonSeriale ON t.CodAutore = n.IDPostPrefazione ")
                NomePo = record.NomeTr
                CognomePo = record.CognomeTr
                NazionePo = record.NazioneTr
            for record in libri.objecrs.raw("SELECT n.NomeTr, n.CognomeTr, n.NazioneTr FROM libri_TradAutCur t, libri_PostfazionePre p, libri_NonSeriale n JOIN libri_TradAutCur ON p.autPrefazione = t.CodAutore JOIN libri_NonSeriale ON t.CodAutore = n.IDPostPrefazione ")
                NomePr = record.NomeTr
                CognomePr = record.CognomeTr
                NazionePr = record.NazioneTr 



                elemento = objlist()
                elemento.inserimento(record.CodLibro, record.NomeCo, record.Sede, record.NomeCa, record.NomeAu, record.CognomeAu, record.NazioneAu, record.NomePo, record.CognomePo, record.NazionePo, record.NomePr, record.CognomePr, record.NazionePr, record.Straniero, record.TitoloOrig, record.Titolo, record.Sottotitolo, record.AnnoEd, record.Illustrazioni, record.ISSN, record.Genere, record.NumPub, record.CopertinaRigida, record.Ristampa, record.nRistampa, record.Edizione, record.NumPagine, record.Curatore, record.NomeTr, record.CognomeTr, record.NazioneTr, record.NomeCr, record.CognomeCr, record.NazioneCr)
            return render(request, 'dettaglio.html', {'context':elemento})
    else:
        print("Errore")


def HomePageViewSeriale(request):
    if request.method == 'GET':
        context=[]
        for record in Seriale.object.raw("SELECT Titolo, Autore, Genere FROM Biblioteca_Seriale"):
            elemento = objlist()
            elemento.inserimentoHome(record.Titolo, record.Autore, record.Genere)
            context.append(elemento)
        return render(request, 'Serial.html',{'context_list':context}) 
    else:
        print("Errore")


def HomePageViewNonSeriale(request):
    if request.method == 'GET':
        context=[]
        for record in Seriale.object.raw("SELECT Titolo, Autore, Genere FROM Biblioteca_NonSeriale"):
            elemento = objlist()
            elemento.inserimentoHome(record.Titolo, record.Autore, record.Genere)
            context.append(elemento)
            
        return render(request, 'notSerial.html',{'context_list':context}) 
    else:
        print("Errore")
"""

def HomePageView(request):
    if request.method == 'GET':
        context=[]
        for record in Seriale.objects.raw("SELECT N.Titolo, N.Autore, N.Genere FROM libri_NonSeriale N "):
            elemento = objlist()
            elemento.inserimentoHome(record.Titolo, record.Autore, record.Genere)
            context.append(elemento)
        
        for record in Seriale.objects.raw("SELECT S.Titolo, S.Autore, S.Genere FROM libri_Seriale S libri_WHERE "):
            elemento = objlist()
            elemento.inserimentoHome(record.Titolo, record.Autore, record.Genere)
            context.append(elemento)


        return render(request, 'base.html',{'context_list':context}) 
    else:
        print("Errore")


