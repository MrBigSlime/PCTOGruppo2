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

def in_TradAutCur(dati):
    
    query="INSERT INTO libri_TradAutCur VALUES(%s,%s,%s,%s)"
    cod="A"+str(randrange(1000))
    cursor = connection.cursor()
    cursor.execute(query,[cod,dati["NazioneTr"],dati["CognomeTr"],dati["NomeTr"]])
    return cod


def in_PostfazionePre(dati):
    cursor = connection.cursor()
    
    cursor.execute("SELECT A.CodAutore FROM libri_TradAutCur A WHERE A.NomeTr=%s AND A.CognomeTr=%s AND A.NazioneTr=%s",[dati["NomePre"],dati["CognomePre"],dati["NazionePre"]])
    ris=cursor.fetchone()

    
    if ris is None:
        
        autPrefazione=in_TradAutCur({"NomeTr":dati["NomePre"],"CognomeTr":dati["CognomePre"],"NazioneTr":dati["NazionePre"]})
    else:
        autPrefazione=ris[0]

    cursor.execute("SELECT A.CodAutore FROM libri_TradAutCur A WHERE A.NomeTr=%s AND A.CognomeTr=%s AND A.NazioneTr=%s",[dati["NomePost"],dati["CognomePost"],dati["NazionePost"]])
    ris=cursor.fetchone()
    if ris is None:
        
        autPostfazione=in_TradAutCur({"NomeTr":dati["NomePost"],"CognomeTr":dati["CognomePost"],"NazioneTr":dati["NazionePost"]})
       
    else:
        autPostfazione=ris[0]
    
    cursor.execute("SELECT P.CodPostfazione FROM libri_TradAutCur A, libri_PostfazionePre P WHERE P.autPostfazione_id=%s AND P.autPrefazione_id=%s",[autPostfazione,autPrefazione])
    ris=cursor.fetchone()
    if ris is None:
        query="INSERT INTO libri_PostfazionePre VALUES(%s,%s,%s)"
        cod="P"+str(randrange(1000))
        cursor.execute(query,[cod,autPostfazione,autPrefazione])
        cursor.close()
        return cod
    else:
        return ris[0]
        

def in_Collana(dati):
    query="INSERT INTO libri_Collane VALUES(%s, %s)"
    cod = "C"+str(randrange(1000))
    cursor = connection.cursor()
    cursor.execute(query,[cod, dati["NomeCo"]])
    cursor.close()
    return cod

def in_CasaEd(dati):
    query="INSERT INTO libri_CasaEditrice VALUES(%s, %s, %s)"
    cod = "E"+str(randrange(1000))
    cursor = connection.cursor()
    cursor.execute(query,[cod, dati["Sede"], dati["NomeCa"],])
    cursor.close()
    return cod

def inspector(dati,identificatore):

    if(identificatore=="A"):
        query="SELECT A.CodAutore FROM libri_TradAutCur A WHERE A.NomeTr=%s AND A.CognomeTr=%s AND A.NazioneTr=%s"
        dato=[dati["NomeTr"],dati["CognomeTr"],dati["NazioneTr"]]
  
    if(identificatore=="E"):
        query="SELECT E.CodCasaEd FROM libri_CasaEditrice E WHERE E.Sede=%s AND E.NomeCa=%s"
        dato=[dati["Sede"],dati["NomeCa"]]

    if(identificatore=="O"):
        query="SELECT O.CodCollane FROM libri_Collane O WHERE O.NomeCo=%s"
        dato=[dati["NomeCo"],]

    if(identificatore=="P"):
        cod=in_PostfazionePre(dati)
        return cod

    cursor = connection.cursor()
    cursor.execute(query,dato)
    ris=cursor.fetchone()
    
    
    if ris is None:

        if(identificatore=="A"):
            cod=in_TradAutCur(dati)

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
            nomiautori.append(ris.NomeTr)
            cognomiautori.append(ris.CognomeTr)

        for ris in CasaEditrice.objects.raw("SELECT C.NomeCa,C.Sede,C.CodCasaEd FROM libri_CasaEditrice C"):
            casaed.append(ris.NomeCa)
            sedeed.append(ris.Sede)
        return(render(request,"inserimento.html",{'form':form,'NomiAu':nomiautori,'cognomiAu':cognomiautori,'casaEd':casaed,'sede':sedeed}))

    elif request.method =='POST':
    
        form = InserimentoLibro(request.POST)
        obj=objlist()

        if form.is_valid():

            identificatore=request.POST.get("IsSerial")

            #dati collane e casa editrice
            NomeCo=request.POST.get("NomeCo")
            NomeCa=request.POST.get("NomeCa")
            SedeCa =request.POST.get("SedeCa")

            #dati autori
            NomeAu=request.POST.get("NomeAu")
            CognomeAu=request.POST.get("CognomeAu")
            NazioneAu=request.POST.get("NazioneAu")

            #dati postfazione
            NomePost=request.POST.get("NomePost")
            CognomePost=request.POST.get("CognomePost")
            NazionePost=request.POST.get("NazionePost")

            #Dati prefazione
            NomePre=request.POST.get("NomePre")
            CognomePre=request.POST.get("CognomePre")
            NazionePre=request.POST.get("NazionePre") 
            
            #Dati anagrafici
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
            NomeC=request.POST.get("NomeCu")
            CognomeC=request.POST.get("CognomeCu")
            NazioneC=request.POST.get("NazioneCu")

            CodCollane=inspector({'NomeCo':NomeCo},"O")
            CodCasaEd=inspector({'Sede':SedeCa,'NomeCa':NomeCa},"E")
            CodAutore=inspector({'NomeTr':NomeAu ,'CognomeTr':CognomeAu ,'NazioneTr':NazioneAu},"A")
            CodPost=inspector({'NomePost':NomePost ,'CognomePost':CognomePost ,'NazionePost':NazionePost,'NomePre':NomePre ,'CognomePre':CognomePre ,'NazionePre':NazionePre},"P")
            CodTrad=inspector({'NomeTr':NomeTr ,'CognomeTr':CognomeTr,'NazioneTr':NazioneTr},"A")
            CodCri=inspector({'NomeTr':NomeC ,'CognomeTr':CognomeC,'NazioneTr':NazioneC},"A")
            
            if identificatore=='off':
                query="INSERT INTO libri_NonSeriale VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cod="N"+str(randrange(1000))
                Dati=[cod,Straniero,TitoloOrig,Titolo,Sottotitolo,AnnoEd,Illustrazioni,ISBN_ISSN,Genere,NumPub,CopertinaRigida,Ristampa,nRistampa,Edizione,NumPagine,Curatore,CodCri,CodAutore,CodCasaEd,CodCollane,CodPost,CodTrad]
                cursor = connection.cursor()
                cursor.execute(query,Dati)
                
            if identificatore=='on':
                query="INSERT INTO libri_Seriale VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cod="S"+str(randrange(1000))
                Dati=[cod,Straniero,TitoloOrig,Titolo,Sottotitolo,AnnoEd,Illustrazioni,ISBN_ISSN,Genere,NumPub,CopertinaRigida,Ristampa,nRistampa,Edizione,NumPagine,Curatore,CodCri,CodAutore,CodCasaEd,CodCollane,CodPost,CodTrad]
                
                cursor = connection.cursor()
                cursor.execute(query,Dati)
                cursor.close()
                return HttpResponseRedirect(reverse('base'))
                

        else:
                print(form.errors)
                return HttpResponseRedirect(reverse('#errore'))



"""
def del_libro(request, Cod):

    cursor = connection.cursor()

    if request.method =='GET':
        cursor.execute("DELETE FROM libri_SingoliLibri S WHERE S.CodLibro=%s", [Cod,])
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
    if request.method = 'GET':
        context[]
        for record in Seriale.object.raw("SELECT S.Titolo, T.NomeTr, T.CognomeTr, S.Genere FROM libri_Seriale S, libri_TradAutCur T WHERE S.IDAutoreCuratore_id=T.CodAutore")
            elemento = objlist()
            elemento.inserimentoHome(record.Titolo,record.NomeTr+" "+record.CognomeTr,record.Genere)
            context.append(elemento)
        return render(request, 'Serial.html',{'context_list':context}) 
    else:
        print("Errore")


def HomePageViewNonSeriale(request):
    if request.method = 'GET':
        context[]
        for record in NonSeriale.object.raw("SELECT N.Titolo, T.NomeTr, T.CognomeTr, N.Genere FROM libri_NonSeriale N, libri_TradAutCur T WHERE N.IDAutoreCuratore_id=T.CodAutore")
            elemento = objlist()
            elemento.inserimentoHome(record.Titolo,record.NomeTr+" "+record.CognomeTr,record.Genere)
            context.append(elemento)
        return render(request, 'notSerial.html',{'context_list':context}) 
    else:
        print("Errore")

"""

def HomePageView(request):
    if request.method == 'GET':
        context=[]
        for record in NonSeriale.objects.raw("SELECT N.CodLibro,N.Titolo,T.NomeTr,T.CognomeTr,N.Genere FROM libri_NonSeriale N, libri_TradAutCur T WHERE N.IDAutoreCuratore_id=T.CodAutore"):
            elemento = objlist()
            elemento.inserimentoHome(record.Titolo, record.Autore, record.Genere)
            context.append(elemento)
        
        for record in Seriale.objects.raw("SELECT S.CodLibro,S.Titolo,T.NomeTr,T.CognomeTr,S.Genere FROM libri_Seriale S, libri_TradAutCur T WHERE S.IDAutoreCuratore_id=T.CodAutore"):
            elemento = objlist()
            elemento.inserimentoHome(record.Titolo,record.NomeTr+" "+record.CognomeTr,record.Genere)
            context.append(elemento)


        return render(request, 'base.html',{'context_list':context}) 
    else:
        print("Errore")


