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
    
    def inserimento(self,CodLibro, NomeCo, Sede, NomeCa, NomeAu, CognomeAu, NazioneAu, NomePo, CognomePo, NazionePo, NomePr, CognomePr, NazionePr, Straniero, TitoloOrig, Titolo, Sottotitolo, AnnoEd, Illustrazioni, ISBN_ISSN, Genere, NumPub, CopertinaRigida, Ristampa, nRistampa, Edizione, NumPagine, Curatore, NomeTr, CognomeTr, NazioneTr, NomeCu, CognomeCu, NazioneCu):
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


def in_serNotser(dati,id):
    
    if id=="N":
        query="INSERT INTO libri_NonSeriale VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cod="N"+str(randrange(1000))

    else:
        query="INSERT INTO libri_Seriale VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cod="S"+str(randrange(1000))
        
    if dati['Curatore']==True:
        cur=True
    else:
        cur=False

    Dati=[cod,dati['Straniero'],dati['TitoloOrig'],dati['Titolo'],dati['Sottotitolo'],dati['AnnoEd'],dati['Illustrazioni'],dati['ISBN_ISSN'],dati['Genere'],dati['NumPub'],dati['CopertinaRigida'],dati['Ristampa'],dati['nRistampa'],dati['Edizione'],dati['NumPagine'],cur,dati['CodCri'],dati['CodAutore'],dati['CodCasaEd'],dati['CodCollane'],dati['CodPost'],dati['CodTrad']]
    cursor = connection.cursor()
    cursor.execute(query,Dati)
    cursor.close()
    
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
        collane=[]
        for ris in TradAutCur.objects.raw("SELECT A.NomeTr,A.CognomeTr,A.CodAutore FROM libri_TradAutCur A"):
            nomiautori.append(ris.NomeTr)
            cognomiautori.append(ris.CognomeTr)

        for ris in CasaEditrice.objects.raw("SELECT C.NomeCa,C.Sede,C.CodCasaEd FROM libri_CasaEditrice C"):
            casaed.append(ris.NomeCa)
            sedeed.append(ris.Sede)

        for ris in Collane.objects.raw("SELECT C.NomeCo, C.CodCollane FROM libri_Collane C"):
            collane.append(ris.NomeCo)

        return(render(request,"inserimento.html",{'form':form,'NomiAu':nomiautori,'cognomiAu':cognomiautori,'casaEd':casaed,'sede':sedeed,'collane':collane}))

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
            if Straniero=='0':
                Straniero=False
            else:
                Straniero=True
            TitoloOrig=request.POST.get("TitoloOrig")
            Titolo=request.POST.get("Titolo")
            Sottotitolo=request.POST.get("Sottotitolo")
            AnnoEd=request.POST.get("AnnoEd")
            Illustrazioni=request.POST.get("Illustrazioni")
            if Illustrazioni=='0':
                Illustrazioni=False
            else:
                Illustrazioni=True
            ISBN_ISSN=request.POST.get("ISBN_ISSN")
            Genere=request.POST.get("Genere")
            NumPub=request.POST.get("NumPub")
            CopertinaRigida=request.POST.get("CopertinaRigida")
            if CopertinaRigida=='0':
                CopertinaRigida=False
            else:
                CopertinaRigida=True
            Ristampa=request.POST.get("Ristampa")
            if Ristampa=='0':
                Ristampa=False
            else:
                Ristampa=True
            nRistampa=request.POST.get("nRistampa")
            Edizione=request.POST.get("Edizione")
            NumPagine=request.POST.get("NumPagine")
            Curatore=request.POST.get("Curatore")
            if Curatore=='0':
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
                query="INSERT INTO libri_NonSeriale VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cod="N"+str(randrange(1000))
                Dati=[cod,Straniero,TitoloOrig,Titolo,Sottotitolo,AnnoEd,Illustrazioni,ISBN_ISSN,Genere,NumPub,CopertinaRigida,Ristampa,nRistampa,Edizione,NumPagine,Curatore,CodCri,CodAutore,CodCasaEd,CodCollane,CodPost,CodTrad]
                cursor = connection.cursor()
                cursor.execute(query,Dati)
                cursor.close()
                
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


def mod_libro(request,cod):
    context=[]
    if request.method == 'GET':
        form = InserimentoLibro()

        nomiautori=[]
        cognomiautori=[]
        casaed=[]
        sedeed=[]
        collane=[]
        for ris in TradAutCur.objects.raw("SELECT A.NomeTr,A.CognomeTr,A.CodAutore FROM libri_TradAutCur A"):
            nomiautori.append(ris.NomeTr)
            cognomiautori.append(ris.CognomeTr)

        for ris in CasaEditrice.objects.raw("SELECT C.NomeCa,C.Sede,C.CodCasaEd FROM libri_CasaEditrice C"):
            casaed.append(ris.NomeCa)
            sedeed.append(ris.Sede)

        for ris in Collane.objects.raw("SELECT C.NomeCo FROM libri_Collane C"):
            collane.append(ris.NomeCo)

        if cod[0]=='N':
            ide='off'
            query="SELECT N.CodLibro, N.IDCollana_id, N.IDCasaEd_id, N.IDAutoreCuratore_id, N.Straniero, N.TitoloOrig, N.Titolo, N.Sottotitolo, N.AnnoEd, N.Illustrazioni, N.ISBN, N.Genere, N.NumPub, N.CopertinaRigida, N.Ristampa, N.nRistampa, N.Edizione, N.NumPagine, N.Curatore, N.Traduttore_id, N.Critico_id FROM libri_NonSeriale N WHERE N.CodLibro=%s"
            ris=NonSeriale.objects.raw(query,[cod,])
        if cod[0]=='S':
            query="SELECT S.CodLibro, S.IDCollana_id, S.IDCasaEd_id, S.IDAutoreCuratore_id, S.Straniero, S.TitoloOrig, S.Titolo, S.Sottotitolo, S.AnnoEd, S.Illustrazioni, S.ISSN, S.Genere, S.NumPub, S.CopertinaRigida, S.Ristampa, S.nRistampa, S.Edizione, S.NumPagine, S.Curatore, S.Traduttore_id, S.Critico_id FROM libri_Seriale S WHERE S.CodLibro=%s"
            ris=Seriale.objects.raw(query,[cod,])
            ide='on'

        for record in ris:
            CodLibro = record.CodLibro
            IDCollana = record.IDCollana
            IDCasaEd = record.IDCasaEd
            IDAutoreCuratore = record.IDAutoreCuratore
            Straniero = record.Straniero
            if Straniero == False:
                Stranieroo="0"
            else: 
                Stranieroo="1"
            
            TitoloOrig = record.TitoloOrig
            Titolo = record.Titolo
            Sottotitolo = record.Sottotitolo
            AnnoEd = record.AnnoEd
            Illustrazioni = record.Illustrazioni
            if  Illustrazioni== False:
                Illustrazionii="0"
            else: 
                Illustrazionii="1"

            if cod[0]=='N':
                ISBN = record.ISBN
            if cod[0]=='S':
                ISBN = record.ISSN    

            Genere = record.Genere
            NumPub = record.NumPub
            
            CopertinaRigida = record.CopertinaRigida
            if CopertinaRigida == False:
                Copertina="0"
            else: 
                Copertina="1"

            Ristampa = record.Ristampa
            if Ristampa == False:
                Ristampaa="0"
            else: 
                Ristampaa="1"

            nRistampa = record.nRistampa
            Edizione = record.Edizione
            NumPagine = record.NumPagine

            Curatore = record.Curatore
            if Curatore == False:
                Curatoree="0"
            else: 
                Curatoree="1"

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
            for record in PostfazionePre.objects.raw("SELECT P.CodPostfazione,P.autPrefazione_id,P.autPostfazione_id FROM libri_PostfazionePre P WHERE P.CodPostfazione=%s",[record.IDPostPrefazione.CodPostfazione]):
                NomePo = record.autPostfazione.NomeTr
                CognomePo = record.autPostfazione.CognomeTr
                NazionePo = record.autPostfazione.NazioneTr 
                NomePr = record.autPrefazione.NomeTr
                CognomePr = record.autPrefazione.CognomeTr
                NazionePr = record.autPrefazione.NazioneTr    
            
            elemento={'Straniero':Stranieroo,'TitoloOrig':TitoloOrig,'Titolo':Titolo,'Sottotitolo':Sottotitolo,'AnnoEd':AnnoEd,'Illustrazioni':Illustrazionii,'Genere':str(Genere),'NumPub':NumPub,'CopertinaRigida':Copertina,
            'Ristampa':Ristampaa,'nRistampa':nRistampa,'Edizione':Edizione,'NumPagine':NumPagine,'Curatore':Curatoree,'Traduttore':Traduttore,'Critico':Critico,'NomeCo':NomeCo,'SedeCa':Sede,
            'NomeCa':NomeCa,'NomeAu':NomeAu,'CognomeAu':CognomeAu,'NazioneAu':NazioneAu,'NomeTr':NomeTr,'CognomeTr':CognomeTr,'NazioneTr':NazioneTr,'NomeCu':NomeCu,'CognomeCu':CognomeCu,'NazioneCu':NazioneCu,
            'NomePost':NomePo,'CognomePost':CognomePo,'NazionePost':NazionePo,'NomePre':NomePr,'CognomePre':CognomePr,'NazionePre':NazionePr,'ISBN_ISSN':ISBN,'IsSerial':ide}
            form = InserimentoLibro(initial=elemento)       
        return(render(request,"modifica.html",{'form':form,'NomiAu':nomiautori,'cognomiAu':cognomiautori,'casaEd':casaed,'sede':sedeed,'collane':collane}))

    if request.method== 'POST':
        form = InserimentoLibro(request.POST)
        if cod[0]=='N':
            
            query="SELECT CodLibro,IDCollana_id,IDCasaEd_id,IDAutoreCuratore_id,IDPostPrefazione_id,Traduttore_id,Critico_id FROM libri_NonSeriale WHERE CodLibro=%s"
            ris=NonSeriale.objects.raw(query,[cod,])
        if cod[0]=='S':
            query="SELECT CodLibro,IDCollana_id,IDCasaEd_id,IDAutoreCuratore_id,IDPostPrefazione_id,Traduttore_id,Critico_id FROM libri_Seriale WHERE CodLibro=%s"
            ris=Seriale.objects.raw(query,[cod,])
        for record in ris:
            CodLibro = record.CodLibro
            IDCollana = record.IDCollana
            IDCasaEd = record.IDCasaEd
            IDAutoreCuratore = record.IDAutoreCuratore
            IDPostPrefazione = record.IDPostPrefazione
            Traduttore = record.Traduttore
            Critico = record.Critico
            for record in PostfazionePre.objects.raw("SELECT * FROM libri_PostfazionePre P WHERE CodPostfazione=%s", [IDPostPrefazione.CodPostfazione,]):
                IDPost=record.autPostfazione
                IDPre=record.autPrefazione

        identificatore=request.POST.get("IsSerial")

        #Dati anagrafici
        Straniero=request.POST.get("Straniero")
        if Straniero=='0': Straniero=False 
        else:   Straniero=True
        Illustrazioni=request.POST.get("Illustrazioni")
        if Illustrazioni=='0': Illustrazioni=False
        else:   Illustrazioni=True
        CopertinaRigida=request.POST.get("CopertinaRigida")
        if CopertinaRigida=='0': CopertinaRigida=False
        else:   CopertinaRigida=True
        Ristampa=request.POST.get("Ristampa")
        if Ristampa=='0':  Ristampa=False           
        else:   Ristampa=True
        Curatore=request.POST.get("Curatore")
        if Curatore=='0': Curatore=False
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
    
        if identificatore=='on':
            if cod[0]=='N':
                
                dati={'CodLibro':CodLibro,'CodCollane':IDCollana.CodCollane,'CodCasaEd':IDCasaEd.CodCasaEd,'CodAutore':IDAutoreCuratore.CodAutore,'CodPost':IDPostPrefazione.CodPostfazione,'CodTrad':Traduttore.CodAutore,'CodCri':Critico.CodAutore,'TitoloOrig':TitoloOrig,'Titolo':Titolo,'Sottotitolo':Sottotitolo,'AnnoEd':AnnoEd,'ISBN_ISSN':ISBN_ISSN,'Genere':Genere,'NumPub':NumPub,'nRistampa':nRistampa,'Edizione':Edizione,'NumPagine':NumPagine,'Ristampa':Ristampa,'Straniero':Straniero,'Illustrazioni':Illustrazioni,'Curatore':Curatore,'CopertinaRigida':CopertinaRigida}
                in_serNotser(dati,'S')
                
                query="DELETE FROM libri_NonSeriale WHERE CodLibro=%s"
                cursor.execute(query,[cod,])
            else:
                query="UPDATE libri_Seriale SET TitoloOrig=%s, Titolo=%s, Sottotitolo=%s, AnnoEd=%s, ISSN=%s, Genere=%s, NumPub=%s, nRistampa=%s, Edizione=%s, NumPagine=%s, Ristampa=%s, Straniero=%s, Illustrazioni=%s, Curatore=%s,CopertinaRigida=%s WHERE CodLibro=%s"
                cursor.execute(query,[TitoloOrig,Titolo,Sottotitolo,AnnoEd,ISBN_ISSN,Genere,NumPub,nRistampa,Edizione,NumPagine,Ristampa,Straniero,Illustrazioni,Curatore,CopertinaRigida,cod])

        if identificatore=='off':
            if cod[0]=="S":
                
                dati={'CodLibro':CodLibro,'CodCollane':IDCollana.CodCollane,'CodCasaEd':IDCasaEd.CodCasaEd,'CodAutore':IDAutoreCuratore.CodAutore,'CodPost':IDPostPrefazione.CodPostfazione,'CodTrad':Traduttore.CodAutore,'CodCri':Critico.CodAutore,'TitoloOrig':TitoloOrig,'Titolo':Titolo,'Sottotitolo':Sottotitolo,'AnnoEd':AnnoEd,'ISBN_ISSN':ISBN_ISSN,'Genere':Genere,'NumPub':NumPub,'nRistampa':nRistampa,'Edizione':Edizione,'NumPagine':NumPagine,'Ristampa':Ristampa,'Straniero':Straniero,'Illustrazioni':Illustrazioni,'Curatore':Curatore,'CopertinaRigida':CopertinaRigida}
                in_serNotser(dati,'N')

                query="DELETE FROM libri_Seriale WHERE CodLibro=%s"
                cursor.execute(query,[cod,])
            else:
                query="UPDATE libri_NonSeriale SET TitoloOrig=%s,Titolo=%s,Sottotitolo=%s,AnnoEd=%s,ISBN=%s,Genere=%s,NumPub=%s,nRistampa=%s,Edizione=%s,NumPagine=%s,Ristampa=%s,Straniero=%s,Curatore=%s,CopertinaRigida=%s,Illustrazioni=%s WHERE CodLibro=%s"
                cursor.execute(query,[TitoloOrig,Titolo,Sottotitolo,AnnoEd,ISBN_ISSN,Genere,NumPub,nRistampa,Edizione,NumPagine,Ristampa,Straniero,Illustrazioni,Curatore,CopertinaRigida,cod])

        cursor.execute("UPDATE libri_Collane SET NomeCo=%s WHERE CodCollane=%s",[NomeCo,IDCollana.CodCollane,])
        cursor.execute("UPDATE libri_CasaEditrice SET Sede=%s,NomeCa=%s WHERE CodCasaEd=%s",[SedeCa,NomeCa,IDCasaEd.CodCasaEd,])
        cursor.execute("UPDATE libri_TradAutCur SET NomeTr=%s,CognomeTr=%s,NazioneTr=%s WHERE CodAutore=%s",[NomeAu,CognomeAu,NazioneAu,IDAutoreCuratore.CodAutore,])
        cursor.execute("UPDATE libri_TradAutCur SET NomeTr=%s,CognomeTr=%s,NazioneTr=%s WHERE CodAutore=%s",[NomePre,CognomePre,NazionePre,IDPre.CodAutore,])
        cursor.execute("UPDATE libri_TradAutCur SET NomeTr=%s,CognomeTr=%s,NazioneTr=%s WHERE CodAutore=%s",[NomePost,CognomePost,NazionePost,IDPost.CodAutore,])
        cursor.execute("UPDATE libri_TradAutCur SET NomeTr=%s,CognomeTr=%s,NazioneTr=%s WHERE CodAutore=%s",[NomeC,CognomeC,NazioneC,Critico.CodAutore,])
        cursor.execute("UPDATE libri_TradAutCur SET NomeTr=%s,CognomeTr=%s,NazioneTr=%s WHERE CodAutore=%s",[NomeTr,CognomeTr,NazioneTr,Traduttore.CodAutore,])
        cursor.close()
        return HttpResponseRedirect(reverse('base'))
        
        
    """
    def del_libro(request, Cod):
        cursor = connection.cursor()
        if request.method =='GET':
            cursor.execute("DELETE FROM libri_SingoliLibri S WHERE S.CodLibro=%s",[Cod,])
            return HttpResponseRedirect(reverse('base'))
            cursor.close()
        else:
            print("Errore")
    """

def del_libro(request, Cod):
    cursor = connection.cursor()
    
    if request.method =='GET':
        if Cod[0]=='N':
            query="DELETE FROM libri_NonSeriale WHERE CodLibro=%s"
            
        if Cod[0]=='S':
            query="DELETE FROM libri_Seriale WHERE CodLibro=%s"
        cursor.execute(query,[Cod,])
        cursor.close()
        return HttpResponseRedirect(reverse('base'))

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
                NomeCo = record.IDCollana.NomeCo
                Sede = record.IDCasaEd.Sede
                NomeCa = record.IDCasaEd.NomeCa
                NomeAu = record.IDAutoreCuratore.NomeTr
                CognomeAu = record.IDAutoreCuratore.CognomeTr
                NazioneAu = record.IDAutoreCuratore.NazioneTr
                NomePr = record.IDPostPrefazione.autPrefazione.NomeTr
                CognomePr = record.IDPostPrefazione.autPrefazione.CognomeTr
                NazionePr = record.IDPostPrefazione.autPrefazione.NazioneTr
                NomePo = record.IDPostPrefazione.autPostfazione.NomeTr
                CognomePo = record.IDPostPrefazione.autPostfazione.CognomeTr
                NazionePo = record.IDPostPrefazione.autPostfazione.NazioneTr
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
                NomeTr = record.Traduttore.NomeTr
                CognomeTr = record.Traduttore.CognomeTr
                NazioneTr = record.Traduttore.NazioneTr
                NomeCu = record.Critico.NomeTr
                CognomeCu = record.Critico.CognomeTr
                NazioneCu = record.Critico.NazioneTr
                elemento = objlist()
                elemento.inserimento( CodLibro,  NomeCo,  Sede,  NomeCa,  NomeAu,  CognomeAu,  NazioneAu,  NomePo,  CognomePo,  NazionePo,  NomePr,  CognomePr,  NazionePr,  Straniero,  TitoloOrig,  Titolo,  Sottotitolo,  AnnoEd,  Illustrazioni,  ISBN,  Genere,  NumPub,  CopertinaRigida,  Ristampa,  nRistampa,  Edizione,  NumPagine,  Curatore,  NomeTr,  CognomeTr,  NazioneTr, NomeCu, CognomeCu, NazioneCu)
            return render(request, 'detail.html', {'context':elemento})
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
            context.append(elemento)
        
        for record in Seriale.objects.raw("SELECT S.CodLibro,S.Titolo,T.NomeTr,T.CognomeTr,S.Genere FROM libri_Seriale S, libri_TradAutCur T WHERE S.IDAutoreCuratore_id=T.CodAutore"):
            elemento = objlist()
            elemento.inserimentoHome(record.Titolo,record.NomeTr+" "+record.CognomeTr,record.Genere,record.CodLibro)
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
            context.append(elemento)
        
        for record in Seriale.objects.raw("SELECT S.CodLibro,S.Titolo,T.NomeTr,T.CognomeTr,S.Genere FROM libri_Seriale S, libri_TradAutCur T WHERE S.IDAutoreCuratore_id=T.CodAutore"):
            elemento = objlist()
            elemento.inserimentoHome(record.Titolo,record.NomeTr+" "+record.CognomeTr,record.Genere,record.CodLibro)
            context.append(elemento)


        return render(request, 'base.html',{'context_list':context}) 
    else:
        print("Errore")
