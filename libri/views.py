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

    def inserimentoHome(self,Titolo, Autore, Genere,Cod):
        self.Titolo = Titolo
        self.Autore = Autore
        self.Genere = Genere
        self.CodLibro = Cod

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
            if Straniero=='on':
                Straniero=False
            else:
                Straniero=True
            TitoloOrig=request.POST.get("TitoloOrig")
            Titolo=request.POST.get("Titolo")
            Sottotitolo=request.POST.get("Sottotitolo")
            AnnoEd=request.POST.get("AnnoEd")
            Illustrazioni=request.POST.get("Illustrazioni")
            if Illustrazioni=='on':
                Illustrazioni=False
            else:
                Illustrazioni=True
            ISBN_ISSN=request.POST.get("ISBN_ISSN")
            Genere=request.POST.get("Genere")
            NumPub=request.POST.get("NumPub")
            CopertinaRigida=request.POST.get("CopertinaRigida")
            if CopertinaRigida=='on':
                CopertinaRigida=False
            else:
                CopertinaRigida=True
            Ristampa=request.POST.get("Ristampa")
            if Ristampa=='on':
                Ristampa=False
            else:
                Ristampa=True
            nRistampa=request.POST.get("nRistampa")
            Edizione=request.POST.get("Edizione")
            NumPagine=request.POST.get("NumPagine")
            Curatore=request.POST.get("Curatore")
            if Curatore=='on':
                Curatore=False
            else:
                Curatore=True

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
                print("hfrghfswrghfsw")
                query="INSERT INTO libri_NonSeriale VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cod="N"+str(randrange(1000))
                Dati=[cod,Straniero,TitoloOrig,Titolo,Sottotitolo,AnnoEd,Illustrazioni,ISBN_ISSN,Genere,NumPub,CopertinaRigida,Ristampa,nRistampa,Edizione,NumPagine,Curatore,CodCri,CodAutore,CodCasaEd,CodCollane,CodPost,CodTrad]
                print(Dati)
                cursor = connection.cursor()
                cursor.execute(query,Dati)
                cursor.close()
                
            if identificatore=='on':
                query="INSERT INTO libri_Seriale VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cod="S"+str(randrange(1000))
                Dati=[cod,CodCasaEd,CodCollane,AnnoEd,CopertinaRigida,Curatore,Edizione,Genere,Illustrazioni,NumPagine,NumPub,Ristampa,Sottotitolo,Straniero,Titolo,TitoloOrig,nRistampa,CodAutore,CodPost,CodCri,CodTrad,ISBN_ISSN]
                cursor = connection.cursor()
                print(Dati)
                cursor.execute(query,Dati)
                cursor.close()
                return HttpResponseRedirect(reverse('base'))
                

        else:
                print(form.errors)
                return HttpResponseRedirect(reverse('#errore'))


def mod_libro(request,cod):
    context=[]
    if request.method == 'GET':
        if cod[0]=='N':
            query="SELECT * FROM libri_NonSeriale WHERE CodLibro=%s"
        if cod[0]=='S':
            query="SELECT * FROM libri_Seriale WHERE CodLibro=%s"
        
        for record in TradAutCur.objects.raw(query,[cod,]):
            CodLibro = record.CodLibro
            IDCollana = record.IDCollana
            IDCasaEd = record.IDCasaEd
            IDAutoreCuratore = record.IDAutoreCuratore
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
            NomeCo = record.IDCollana.NomeCo
            Sede = record.IDCasaEd.Sede
            NomeCa = record.IDCasaEd.NomeCa
            NomeAu = record.IDAutoreCuratore.NomeTr
            CognomeAu = record.IDAutoreCuratore.CognomeTr
            NazioneAu = record.IDAutoreCuratore.CognomeTr
            NomeTr = record.Traduttore.NomeTr
            CognomeTr = record.Traduttore.CognomeTr
            NazioneTr = record.Traduttore.NazioneTr
            NomeCu = record.Critico.NomeTr
            CognomeCu = record.Critico.CognomeTr
            NazioneCu = record.Critico.NazioneTr
            for record in NonSeriale.objecrs.raw("SELECT * FROM libri_PostfazionePre P WHERE P.CodPostfazione=%s",[record.IDPostPrefazione.CodPostfazione]):
                NomePo = record.autPostfazione.NomeTr
                CognomePo = record.autPostfazione.CognomeTr
                NazionePo = record.autPostfazione.NazioneTr 
                NomePr = record.autPrefazione.NomeTr
                CognomePr = record.autPrefazione.CognomeTr
                NazionePr = record.autPrefazione.NazioneTr    

            elemento = objlist()
            elemento.inserimento( CodLibro,  NomeCo,  Sede,  NomeCa,  NomeAu,  CognomeAu,  NazioneAu,  NomePo,  CognomePo,  NazionePo,  NomePr,  CognomePr,  NazionePr,  Straniero,  TitoloOrig,  Titolo,  Sottotitolo,  AnnoEd,  Illustrazioni,  ISBN,  Genere,  NumPub,  CopertinaRigida,  Ristampa,  nRistampa,  Edizione,  NumPagine,  Curatore,  NomeTr,  CognomeTr,  NazioneTr,  NomeCr,  CognomeCr,  NazioneCr)
            context.append(elemento)

        return(render(request,"inserimento.html",{"context":context}))

        if request.method== 'POST':
            for record in TradAutCur.objects.raw("SELECT * FROM libri_NonSeriale WHERE CodLibro=%s", [CodLibro,]):
                
                IDCollana = record.IDCollana
                IDCasaEd = record.IDCasaEd
                IDAutoreCuratore = record.IDAutoreCuratore
                IDPostPrefazione = record.IDPostPrefazione
                Traduttore = record.Traduttore
                Critico = record.Critico
                for record in TradAutCur.objects.raw("SELECT * FROM libri_PostfazionePre P WHERE CodPostfazione=%s", [IDPostPrefazione,]):
                    IDPost=record.autPostfazione
                    IDPre=record.autPrefazione

            identificatore=request.POST.get("IsSerial")

            #Dati anagrafici
            Straniero=request.POST.get("Straniero")
            if Straniero=='on': Straniero=False 
            else:   Straniero=True
            Illustrazioni=request.POST.get("Illustrazioni")
            if Illustrazioni=='on': Illustrazioni=False
            else:   Illustrazioni=True
            CopertinaRigida=request.POST.get("CopertinaRigida")
            if CopertinaRigida=='on': CopertinaRigida=False
            else:   CopertinaRigida=True
            Ristampa=request.POST.get("Ristampa")
            if Ristampa=='on':  Ristampa=False           
            else:   Ristampa=True
            Curatore=request.POST.get("Curatore")
            if Curatore=='on': Curatore=False
            else: Curatore=True

            TitoloOrig=request.POST.get("TitoloOrig")
            Titolo=request.POST.get("Titolo")
            Sottotitolo=request.POST.get("Sottotitolo")
            AnnoEd=request.POST.get("AnnoEd")
            ISBN_ISSN=request.POST.get("ISBN_ISSN")
            Genere=request.POST.get("Genere")
            NumPub=request.POST.get("NumPub")
            nRistampa=request.POST.get("nRistampa")
            Edizione=request.POST.get("Edizione")
            NumPagine=request.POST.get("NumPagine")
            

            #Dati Critico
            NomeTr=request.POST.get("NomeTr")
            CognomeTr=request.POST.get("CognomeTr")
            NazioneTr=request.POST.get("NazioneTr") 

            #Dati Critico
            NomeC=request.POST.get("NomeCu")
            CognomeC=request.POST.get("CognomeCu")
            NazioneC=request.POST.get("NazioneCu")

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

        cursor = connection.cursor()
        cursor.execute("UPDATE libri_Collane SET NomeCo=%s WHERE CodCollane=%s",[NomeCo,IDCollana,])
        cursor.execute("UPDATE libri_CasaEditrice SET Sede=%s,NomeCa=%s WHERE CodCasaEd=%s",[Sede,NomeCa,IDCasaEd,])
        cursor.execute("UPDATE libri_TradAutCur SET NomeAu=%s,CognomeAu=%s,NazioneAu=%s WHERE CodAutore=%s",[NomeAu,CognomeAu,NazioneAu,IDAutoreCuratore,])
        cursor.execute("UPDATE libri_TradAutCur SET NomeAu=%s,CognomeAu=%s,NazioneAu=%s WHERE CodAutore=%s",[NomePre,CognomePre,NazionePre,IDPre,])
        cursor.execute("UPDATE libri_TradAutCur SET NomeAu=%s,CognomeAu=%s,NazioneAu=%s WHERE CodAutore=%s",[NomePost,CognomePost,NazionePost,IDPost,])
        cursor.close()

def del_libro(request, Cod):
    cursor = connection.cursor()
    if request.method =='GET':
        cursor.execute("DELETE FROM libri_SingoliLibri S WHERE S.CodLibro=%s",[Cod,])
        return HttpResponseRedirect(reverse('base'))
        cursor.close()
    else:
        print("Errore")


def LibroDetailView(request,Cod):
    """
    if request.method == 'GET':             #controllo seriale o non seriale

        cursor = connection.cursor()
        cursor.execute("SELECT S.IDSeriale, S.IDNonseriale FROM libri_SingoliLibri S WHERE S.CodLibro=%s", [Cod,])
        ris = cursor.fetchall()
        for record in ris:
            IDSeriale = record.IDSeriale
            IDNonseriale = record.IDNonseriale

    else:

        print("Errore")
    """

    if request.method == 'GET':

            if Cod[0]=='N':
                query="SELECT * FROM libri_NonSeriale WHERE CodLibro=%s"

            if Cod[0]=='S':
                query="SELECT * FROM libri_Seriale WHERE CodLibro=%s"

            for record in NonSeriale.objects.raw(query,[Cod,]):
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

            for record in Collane.objects.raw("SELECT * FROM libri_Collane C WHERE C.CodCollane=%s", [IDCollana,]):
                NomeCo = record.NomeCo

            for record in CasaEditrice.objects.raw("SELECT * FROM libri_CasaEditrice C WHERE C.CodCasaEd=%s", [IDCasaEd,]):
                Sede = record.Sede
                NomeCa = record.NomeCa

            for record in TradAutCur.objects.raw("SELECT * FROM libri_TradAutCur T WHERE T.CodAutore=%s", [IDAutoreCuratore,]):
                NomeAu = record.NomeTr
                CognomeAu = record.CognomeTr
                NazioneAu = record.CognomeTr

            for record in TradAutCur.objects.raw("SELECT * FROM libri_TradAutCur T WHERE T.CodAutore=%s", [Traduttore,]):
                NomeTr = record.NomeTr
                CognomeTr = record.CognomeTr
                NazioneTr = record.NazioneTr

            for record in TradAutCur.objects.raw("SELECT * FROM libri_TradAutCur WHERE CodAutore=%s", [Critico,]):
                NomeCu = record.NomeTr
                CognomeCu = record.CognomeTr
                NazioneCu = record.NazioneTr

            for record in PostfazionePre.objecrs.raw("SELECT T.NomeTr, T.CognomeTr, T.NazioneTr FROM libri_TradAutCur T, libri_PostfazionePre P, libri_NonSeriale N WHERE N.IDPostPrefazione = P.CodAutore AND P.autPostfazione = T.CodAutore AND P.CodLibro=%s",[Cod,]):
                NomePo = record.NomeTr
                CognomePo = record.CognomeTr
                NazionePo = record.NazioneTr 

            for record in PostfazionePre.objecrs.raw("SELECT T.NomeTr, T.CognomeTr, T.NazioneTr FROM libri_TradAutCur T, libri_PostfazionePre P, libri_NonSeriale N WHERE N.IDPostPrefazione = P.CodAutore AND P.autPrefazione = T.CodAutore AND P.CodLibro=%s",[Cod,]):
                NomePr = record.NomeTr
                CognomePr = record.CognomeTr
                NazionePr = record.NazioneTr    

            elemento = objlist()
            elemento.inserimento(record.CodLibro, record.NomeCo, record.Sede, record.NomeCa, record.NomeAu, record.CognomeAu, record.NazioneAu, record.NomePo, record.CognomePo, record.NazionePo, record.NomePr, record.CognomePr, record.NazionePr, record.Straniero, record.TitoloOrig, record.Titolo, record.Sottotitolo, record.AnnoEd, record.Illustrazioni, record.ISBN, record.Genere, record.NumPub, record.CopertinaRigida, record.Ristampa, record.nRistampa, record.Edizione, record.NumPagine, record.Curatore, record.NomeTr, record.CognomeTr, record.NazioneTr, record.NomeCr, record.CognomeCr, record.NazioneCr)
            return render(request, 'dettaglio.html', {'context':elemento})
    else:
        print("Errore")


def HomePageViewSeriale(request):
    if request.method == 'GET':
        context=[]
        for record in Seriale.object.raw("SELECT S.Titolo, T.NomeTr, T.CognomeTr, S.Genere FROM libri_Seriale S, libri_TradAutCur T WHERE S.IDAutoreCuratore_id=T.CodAutore"):
            elemento = objlist()
            elemento.inserimentoHome(record.Titolo,record.NomeTr+" "+record.CognomeTr,record.Genere)
            context.append(elemento)
        return render(request, 'Serial.html',{'context_list':context}) 
    else:
        print("Errore")
        
def HomePageViewNonSeriale(request):
    if request.method == 'GET':
        context=[]
        for record in NonSeriale.object.raw("SELECT N.Titolo, T.NomeTr, T.CognomeTr, N.Genere FROM libri_NonSeriale N, libri_TradAutCur T WHERE N.IDAutoreCuratore_id=T.CodAutore"):
            elemento = objlist()
            elemento.inserimentoHome(record.Titolo,record.NomeTr+" "+record.CognomeTr,record.Genere)
            context.append(elemento)
        return render(request, 'notSerial.html',{'context_list':context}) 
    else:
        print("Errore")


def HomePageView(request):
    if request.method == 'GET':
        context=[]
        for record in NonSeriale.objects.raw("SELECT N.CodLibro,N.Titolo,T.NomeTr,T.CognomeTr,N.Genere FROM libri_NonSeriale N, libri_TradAutCur T WHERE N.IDAutoreCuratore_id=T.CodAutore"):
            elemento = objlist()
            elemento.inserimentoHome(record.Titolo,record.NomeTr+" "+record.CognomeTr,record.Genere,record.CodLibro)
            print(elemento.CodLibro)
            context.append(elemento)
        
        for record in Seriale.objects.raw("SELECT S.CodLibro,S.Titolo,T.NomeTr,T.CognomeTr,S.Genere FROM libri_Seriale S, libri_TradAutCur T WHERE S.IDAutoreCuratore_id=T.CodAutore"):
            elemento = objlist()
            elemento.inserimentoHome(record.Titolo,record.NomeTr+" "+record.CognomeTr,record.Genere,record.CodLibro)
            print(elemento.CodLibro)
            context.append(elemento)


        return render(request, 'base.html',{'context_list':context}) 
    else:
        print("Errore")


def HomePageView(request):
    if request.method == 'GET':
        context=[]
        for record in NonSeriale.objects.raw("SELECT N.CodLibro,N.Titolo,T.NomeTr,T.CognomeTr,N.Genere FROM libri_NonSeriale N, libri_TradAutCur T WHERE N.IDAutoreCuratore_id=T.CodAutore"):
            elemento = objlist()
            elemento.inserimentoHome(record.Titolo,record.NomeTr+" "+record.CognomeTr,record.Genere,record.CodLibro)
            print(elemento.CodLibro)
            context.append(elemento)
        
        for record in Seriale.objects.raw("SELECT S.CodLibro,S.Titolo,T.NomeTr,T.CognomeTr,S.Genere FROM libri_Seriale S, libri_TradAutCur T WHERE S.IDAutoreCuratore_id=T.CodAutore"):
            elemento = objlist()
            elemento.inserimentoHome(record.Titolo,record.NomeTr+" "+record.CognomeTr,record.Genere,record.CodLibro)
            print(elemento.CodLibro)
            context.append(elemento)


        return render(request, 'base.html',{'context_list':context}) 
    else:
        print("Errore")
