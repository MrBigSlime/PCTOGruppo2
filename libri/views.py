from django.shortcuts import render, redirect
from django import forms
from django.db import connection
from libri.forms import *
from libri.models import *
from django.urls import reverse
from django.http import HttpResponseRedirect
from random import randrange
import datetime

class objlist():                        
    def __Init__(self):
        self.CodLibro = ""
        self.NomeCo = ""
        self.Sede = ""
        self.NomeCa = ""
        self.NomeAu = ""                            #NomeAu è riferito alla tabella TradAutCur
        self.CognomeAu = ""
        self.NazioneAu = ""
        self.NomePo = ""                            #NomePo è riferito alla tabella TradAutCur
        self.CognomePo = ""
        self.NazionePo = ""
        self.NomePr = ""                            #NomePr è riferito alla tabella TradAutCur
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

    def inserimentoHome(self,Titolo, Autore, Genere,Cod, ISBN):
        self.Titolo = Titolo
        self.Autore = Autore
        self.Genere = Genere
        self.CodLibro = Cod
        self.ISBN_ISSN = ISBN

    
class listaPrestiti():
    def __Init__(self):
        self.DataInizio = ""
        self.DataFine = ""
        self.NomeUt = ""
        self.CognomeUt = ""
        self.NumTelefono = ""
        self.Ritardo = False

    def inserimento(self, DataInizio, DataFine, NomeUt, CognomeUt, NumTelefono, Ritardo):
        self.DataInizio = DataInizio
        self.DataFine = DataFine
        self.NomeUt = NomeUt
        self.CognomeUt = CognomeUt
        self.NumTelefono = NumTelefono
        self.Ritardo = Ritardo

def check(cod):
    if cod[0]=='N':
        query = "SELECT CodLibro FROM libri_NonSeriale WHERE CodLibro=%s"
    if cod[0]=='S':
        query = "SELECT CodLibro FROM libri_Seriale WHERE CodLibri=%s"
    if cod[0]=='A':
        query = "SELECT CodAutore FROM libri_TradAutCur WHERE CodAutore=%s"
    if cod[0]=='P':
        query = "SELECT CodPostfazione FROM libri_PostfazionePre WHERE CodPostfazione=%s"
    if cod[0]=='C':
        query = "SELECT CodCollane FROM libri_Collane WHERE CodCollane=%s"
    if cod[0]=='E':
        query = "SELECT CodCasaEd FROM libri_CasaEditrice WHERE CodCasaEd=%s"
    if cod[0]=='U':
        query = "SELECT CodUser FROM libri_Utenti WHERE CodUser=%s"
    if cod[0]=='P':
        query = "SELECT CodPrestito FROM libri_Prestito WHERE CodPrestito=%s"

    cursor = connection.cursor()
    cursor.execute(query,cod)
    ris=cursor.fetchone()
    if ris is None:
        return True
    else:
        return False

def in_serNotser(dati,id):          #Funzione per l'inserimento di un modello di libro, dati=dizionario con i dati da inserire, id=identificatore tipo di libro 
    
    if id=="N":
        query="INSERT INTO libri_NonSeriale VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"          #controllo del tipo di libro che si vuole inserire 
        cod="N"+str(randrange(1000))

    else:
        query="INSERT INTO libri_Seriale VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"             
        cod="S"+str(randrange(1000))

    Dati=[cod,dati['Straniero'],dati['TitoloOrig'],dati['Titolo'],dati['Sottotitolo'],dati['AnnoEd'],dati['Illustrazioni'],dati['ISBN_ISSN'],dati['Genere'],dati['NumPub'],dati['CopertinaRigida'],dati['Ristampa'],dati['nRistampa'],dati['Edizione'],dati['NumPagine'],dati['Curatore'],dati['CodCri'],dati['CodAutore'],dati['CodCasaEd'],dati['CodCollane'],dati['CodPost'],dati['CodTrad']]
    cursor = connection.cursor()        #Apertura connessione al db
    cursor.execute(query,Dati)                  
    cursor.close()
    
def in_TradAutCur(dati):
    
    query="INSERT INTO libri_TradAutCur VALUES(%s,%s,%s,%s)"
    cod="A"+str(randrange(1000))
    cursor = connection.cursor()
    cursor.execute(query,[cod,dati["NazioneTr"],dati["CognomeTr"],dati["NomeTr"]])
    return cod

def in_Collana(dati):
    query="INSERT INTO libri_Collane VALUES(%s, %s)"                #inserimento nuova collana
    cod = "C"+str(randrange(1000))
    cursor = connection.cursor()
    cursor.execute(query,[cod, dati["NomeCo"]])
    cursor.close()
    return cod

def in_CasaEd(dati):
    query="INSERT INTO libri_CasaEditrice VALUES(%s, %s, %s)"           #inseriment nuova CasaEditrice
    cod = "E"+str(randrange(1000))                          
    cursor = connection.cursor()
    cursor.execute(query,[cod, dati["Sede"], dati["NomeCa"],])
    cursor.close()
    return cod

def in_PostfazionePre(dati):    #Funzione per l'inserimento delle chiavi alla tabella PostfazionePre
    cursor = connection.cursor()
    
    cursor.execute("SELECT A.CodAutore FROM libri_TradAutCur A WHERE A.NomeTr=%s AND A.CognomeTr=%s AND A.NazioneTr=%s",[dati["NomePre"],dati["CognomePre"],dati["NazionePre"]])
    ris=cursor.fetchone()                                       

    
    if ris is None:             #Check se un determinato autore è presente nel db
        
        autPrefazione=in_TradAutCur({"NomeTr":dati["NomePre"],"CognomeTr":dati["CognomePre"],"NazioneTr":dati["NazionePre"]})
    else:
        autPrefazione=ris[0]

    cursor.execute("SELECT A.CodAutore FROM libri_TradAutCur A WHERE A.NomeTr=%s AND A.CognomeTr=%s AND A.NazioneTr=%s",[dati["NomePost"],dati["CognomePost"],dati["NazionePost"]])
    ris=cursor.fetchone()
    if ris is None:              #Check se un determinato autore è presente nel db               
        
        autPostfazione=in_TradAutCur({"NomeTr":dati["NomePost"],"CognomeTr":dati["CognomePost"],"NazioneTr":dati["NazionePost"]})
       
    else:
        autPostfazione=ris[0]
    
    cursor.execute("SELECT P.CodPostfazione FROM libri_TradAutCur A, libri_PostfazionePre P WHERE P.autPostfazione_id=%s AND P.autPrefazione_id=%s",[autPostfazione,autPrefazione])
    ris=cursor.fetchone()               
    if ris is None:             #Check se la coppia di codici autore è gia esistente nel db            
        query="INSERT INTO libri_PostfazionePre VALUES(%s,%s,%s)"
        cod="P"+str(randrange(1000))
        cursor.execute(query,[cod,autPostfazione,autPrefazione])
        cursor.close()
        return cod
    else:
        return ris[0]

def in_Utenti(dati):
    query="INSERT INTO libri_Utenti VALUES(%s,%s,%s,%s,%s)"
    while True:
        cod="U"+str(randrange(1000))                                                                                            #CHECK
        if check(cod):
            break                                                                                           #CHECK
    cursor = connection.cursor()
    cursor.execute(query,[cod,dati["CognomeUt"],dati["NomeUt"],dati["Email"],dati["NumTelefono"]])
    return cod

def inspector(dati,identificatore):                                 #funzione che gestrisce il controllo della esistenza di un dato nel database

    if(identificatore=="U"):
        query="SELECT U.CodUser FROM libri_Utenti U WHERE U.NomeUt=%s AND U.CognomeUt=%s AND U.Email=%s AND U.NumTelefono=%s "
        dato=[dati["NomeUt"],dati["Cognome"],dati["Email"],dati["NumTelefono"]]

    if(identificatore=="A"):            
        query="SELECT A.CodAutore FROM libri_TradAutCur A WHERE A.NomeTr=%s AND A.CognomeTr=%s AND A.NazioneTr=%s"
        dato=[dati["NomeTr"],dati["CognomeTr"],dati["NazioneTr"]]
  
    if(identificatore=="E"):                                                                                        #in base al id si seleziona quale query e set di dati utilizzare
        query="SELECT E.CodCasaEd FROM libri_CasaEditrice E WHERE E.Sede=%s AND E.NomeCa=%s"
        dato=[dati["Sede"],dati["NomeCa"]]

    if(identificatore=="O"):
        query="SELECT O.CodCollane FROM libri_Collane O WHERE O.NomeCo=%s"
        dato=[dati["NomeCo"],]

    if(identificatore=="P"):
        cod=in_PostfazionePre(dati)
        return cod

    cursor = connection.cursor()
    cursor.execute(query,dato)                                                                                      #si esegue la query e si controlla se ritorna un codice 
    ris=cursor.fetchone()
    
    
    if ris is None:

        if(identificatore=="U"):
            cod=in_Utenti(dati)
        
        if(identificatore=="A"):
            cod=in_TradAutCur(dati)

        if(identificatore=="E"):
            cod=in_CasaEd(dati)
                    
        if(identificatore=="O"):
            cod=in_Collana(dati)

        return cod

    else:                                                                       #se non viene trovato il codice viene chiamata una delle 4 funzioni di insermento che ritorneranno il codice che poi passera alla view di insermento
        
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
            nomiautori.append(ris.NomeTr)                                                                                       #invio delle liste per i datalist
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
            Illustrazioni=request.POST.get("Illustrazioni")                                                            #Get di tutti i dati ricevuti dal form
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

            CodCollane=inspector({'NomeCo':NomeCo},"O")                                                                                         #controllo e fetch dei codici per l'inserimento
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
                                                                                                        #inserimenti in base alla tabella 
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

        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(S.CodLibro) FROM libri_SingoliLibri S")
        totale=cursor.fetchone()
        cursor.close()

        """
        nomiautori=[]
        cognomiautori=[]
        casaed=[]
        sedeed=[]
        collane=[]  
                                                                                                     #invio delle liste per i datalist
        for ris in TradAutCur.objects.raw("SELECT A.NomeTr,A.CognomeTr,A.CodAutore FROM libri_TradAutCur A"):
            nomiautori.append(ris.NomeTr)
            cognomiautori.append(ris.CognomeTr)

        for ris in CasaEditrice.objects.raw("SELECT C.NomeCa,C.Sede,C.CodCasaEd FROM libri_CasaEditrice C"):
            casaed.append(ris.NomeCa)
            sedeed.append(ris.Sede)

        for ris in Collane.objects.raw("SELECT C.NomeCo,C.CodCollane FROM libri_Collane C"):
            collane.append(ris.NomeCo)
        """
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
            Traduttore = record.Traduttore
            Critico = record.Critico

            #Anagrafica Libro
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

            #Dati Collana
            NomeCo = record.IDCollana.NomeCo

            #Dati casaEditrice
            Sede = record.IDCasaEd.Sede
            NomeCa = record.IDCasaEd.NomeCa

            #Dati Autore
            NomeAu = record.IDAutoreCuratore.NomeTr
            CognomeAu = record.IDAutoreCuratore.CognomeTr
            NazioneAu = record.IDAutoreCuratore.CognomeTr

            #Dati Traduttore
            NomeTr = record.Traduttore.NomeTr
            CognomeTr = record.Traduttore.CognomeTr
            NazioneTr = record.Traduttore.NazioneTr
            
            #Dati critico
            NomeCu = record.Critico.NomeTr
            CognomeCu = record.Critico.CognomeTr
            NazioneCu = record.Critico.NazioneTr

            for record in PostfazionePre.objects.raw("SELECT P.CodPostfazione,P.autPrefazione_id,P.autPostfazione_id FROM libri_PostfazionePre P WHERE P.CodPostfazione=%s",[record.IDPostPrefazione.CodPostfazione]):
                #Dati Autore Postfazione
                NomePo = record.autPostfazione.NomeTr
                CognomePo = record.autPostfazione.CognomeTr
                NazionePo = record.autPostfazione.NazioneTr 
                
                #Dati Autore Prefazione
                NomePr = record.autPrefazione.NomeTr
                CognomePr = record.autPrefazione.CognomeTr
                NazionePr = record.autPrefazione.NazioneTr    
            
            #Lista dei dati per formattare il form
            elemento={'Straniero':Stranieroo,'TitoloOrig':TitoloOrig,'Titolo':Titolo,'Sottotitolo':Sottotitolo,'AnnoEd':AnnoEd,'Illustrazioni':Illustrazionii,'Genere':str(Genere),'NumPub':NumPub,'CopertinaRigida':Copertina,
            'Ristampa':Ristampaa,'nRistampa':nRistampa,'Edizione':Edizione,'NumPagine':NumPagine,'Curatore':Curatoree,'Traduttore':Traduttore,'Critico':Critico,'NomeCo':NomeCo,'SedeCa':Sede,
            'NomeCa':NomeCa,'NomeAu':NomeAu,'CognomeAu':CognomeAu,'NazioneAu':NazioneAu,'NomeTr':NomeTr,'CognomeTr':CognomeTr,'NazioneTr':NazioneTr,'NomeCu':NomeCu,'CognomeCu':CognomeCu,'NazioneCu':NazioneCu,
            'NomePost':NomePo,'CognomePost':CognomePo,'NazionePost':NazionePo,'NomePre':NomePr,'CognomePre':CognomePr,'NazionePre':NazionePr,'ISBN_ISSN':ISBN,'IsSerial':ide,"QLibri":totale}
           
            form = InserimentoLibro(initial=elemento)       
        #return(render(request,"modifica.html",{'form':form,'NomiAu':nomiautori,'cognomiAu':cognomiautori,'casaEd':casaed,'sede':sedeed,'collane':collane}))
        return(render(request,"modifica.html",{'form':form}))

    if request.method== 'POST':
        form = InserimentoLibro(request.POST)

        if cod[0]=='N':
            query="SELECT CodLibro,IDCollana_id,IDCasaEd_id,IDAutoreCuratore_id,IDPostPrefazione_id,Traduttore_id,Critico_id FROM libri_NonSeriale WHERE CodLibro=%s"
            ris=NonSeriale.objects.raw(query,[cod,])
                                            #In base al codice ricevuto si deriva quale query 
        if cod[0]=='S':
            query="SELECT CodLibro,IDCollana_id,IDCasaEd_id,IDAutoreCuratore_id,IDPostPrefazione_id,Traduttore_id,Critico_id FROM libri_Seriale WHERE CodLibro=%s"
            ris=Seriale.objects.raw(query,[cod,])

        for record in ris:
            #Recupero dei codici 
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

        #Singoli Libri
        Qlibri=request.POST.get("QLibri")
        invDef(Qlibri)
        cursor = connection.cursor()
    
        if identificatore=='on':                        #Controllo se l'utente ha modificato la serialità del libro 
            if cod[0]=='N':
                
                dati={'CodLibro':CodLibro,'CodCollane':IDCollana.CodCollane,'CodCasaEd':IDCasaEd.CodCasaEd,'CodAutore':IDAutoreCuratore.CodAutore,'CodPost':IDPostPrefazione.CodPostfazione,'CodTrad':Traduttore.CodAutore,'CodCri':Critico.CodAutore,'TitoloOrig':TitoloOrig,'Titolo':Titolo,'Sottotitolo':Sottotitolo,'AnnoEd':AnnoEd,'ISBN_ISSN':ISBN_ISSN,'Genere':Genere,'NumPub':NumPub,'nRistampa':nRistampa,'Edizione':Edizione,'NumPagine':NumPagine,'Ristampa':Ristampa,'Straniero':Straniero,'Illustrazioni':Illustrazioni,'Curatore':Curatore,'CopertinaRigida':CopertinaRigida}
                in_serNotser(dati,'S')
                #viene chiamata la funzione per l'inserimento ed viene eliminato la riga 
                query="DELETE FROM libri_NonSeriale WHERE CodLibro=%s"
                cursor.execute(query,[cod,])        
            else:
                #query per l'update
                query="UPDATE libri_Seriale SET TitoloOrig=%s, Titolo=%s, Sottotitolo=%s, AnnoEd=%s, ISSN=%s, Genere=%s, NumPub=%s, nRistampa=%s, Edizione=%s, NumPagine=%s, Ristampa=%s, Straniero=%s, Illustrazioni=%s, Curatore=%s,CopertinaRigida=%s WHERE CodLibro=%s"
                cursor.execute(query,[TitoloOrig,Titolo,Sottotitolo,AnnoEd,ISBN_ISSN,Genere,NumPub,nRistampa,Edizione,NumPagine,Ristampa,Straniero,Illustrazioni,Curatore,CopertinaRigida,cod])

        if identificatore=='off':
            if cod[0]=="S":
                
                dati={'CodLibro':CodLibro,'CodCollane':IDCollana.CodCollane,'CodCasaEd':IDCasaEd.CodCasaEd,'CodAutore':IDAutoreCuratore.CodAutore,'CodPost':IDPostPrefazione.CodPostfazione,'CodTrad':Traduttore.CodAutore,'CodCri':Critico.CodAutore,'TitoloOrig':TitoloOrig,'Titolo':Titolo,'Sottotitolo':Sottotitolo,'AnnoEd':AnnoEd,'ISBN_ISSN':ISBN_ISSN,'Genere':Genere,'NumPub':NumPub,'nRistampa':nRistampa,'Edizione':Edizione,'NumPagine':NumPagine,'Ristampa':Ristampa,'Straniero':Straniero,'Illustrazioni':Illustrazioni,'Curatore':Curatore,'CopertinaRigida':CopertinaRigida}
                in_serNotser(dati,'N')
                #viene chiamata la funzione per l'inserimento ed viene eliminato la riga 
                query="DELETE FROM libri_Seriale WHERE CodLibro=%s"
                cursor.execute(query,[cod,])
            else:
                #query per l'update
                query="UPDATE libri_NonSeriale SET TitoloOrig=%s,Titolo=%s,Sottotitolo=%s,AnnoEd=%s,ISBN=%s,Genere=%s,NumPub=%s,nRistampa=%s,Edizione=%s,NumPagine=%s,Ristampa=%s,Straniero=%s,Curatore=%s,CopertinaRigida=%s,Illustrazioni=%s WHERE CodLibro=%s"
                cursor.execute(query,[TitoloOrig,Titolo,Sottotitolo,AnnoEd,ISBN_ISSN,Genere,NumPub,nRistampa,Edizione,NumPagine,Ristampa,Straniero,Illustrazioni,Curatore,CopertinaRigida,cod])

        #Update a cascata di ogni riga legata 
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
    #elimina la row in base al codice inserito
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
            #controllo Seriale o Non Seriale
            if Cod[0]=='N':
                query="SELECT * FROM libri_NonSeriale WHERE CodLibro=%s"

            if Cod[0]=='S':
                query="SELECT * FROM libri_Seriale WHERE CodLibro=%s"
            #estrazione dati
            for record in NonSeriale.objects.raw(query,[Cod,]):

                #codice del libro
                CodLibro = record.CodLibro

                #dati collane e casa editrice
                NomeCo = record.IDCollana.NomeCo
                Sede = record.IDCasaEd.Sede
                NomeCa = record.IDCasaEd.NomeCa

                #dati autore
                NomeAu = record.IDAutoreCuratore.NomeTr
                CognomeAu = record.IDAutoreCuratore.CognomeTr
                NazioneAu = record.IDAutoreCuratore.NazioneTr

                #dati autore prefazione
                NomePr = record.IDPostPrefazione.autPrefazione.NomeTr
                CognomePr = record.IDPostPrefazione.autPrefazione.CognomeTr
                NazionePr = record.IDPostPrefazione.autPrefazione.NazioneTr

                #dati autore postfazione
                NomePo = record.IDPostPrefazione.autPostfazione.NomeTr
                CognomePo = record.IDPostPrefazione.autPostfazione.CognomeTr
                NazionePo = record.IDPostPrefazione.autPostfazione.NazioneTr

                #dati anagrafici
                Straniero = record.Straniero
                TitoloOrig = record.TitoloOrig
                Titolo = record.Titolo
                Sottotitolo = record.Sottotitolo
                AnnoEd = record.AnnoEd
                Illustrazioni = record.Illustrazioni
                
                if Cod[0]=='N':
                    ISBN = record.ISBN

                if Cod[0]=='S':
                    ISBN = record.ISSN
                
                Genere = record.Genere
                NumPub = record.NumPub
                CopertinaRigida = record.CopertinaRigida
                Ristampa = record.Ristampa
                nRistampa = record.nRistampa
                Edizione = record.Edizione
                NumPagine = record.NumPagine
                Curatore = record.Curatore

                #dati traduttore
                NomeTr = record.Traduttore.NomeTr
                CognomeTr = record.Traduttore.CognomeTr
                NazioneTr = record.Traduttore.NazioneTr

                #dati critico
                NomeCu = record.Critico.NomeTr
                CognomeCu = record.Critico.CognomeTr
                NazioneCu = record.Critico.NazioneTr
            
                elemento = objlist()
                elemento.inserimento( CodLibro,  NomeCo,  Sede,  NomeCa,  NomeAu,  CognomeAu,  NazioneAu,  NomePo,  CognomePo,  NazionePo,  NomePr,  CognomePr,  NazionePr,  Straniero,  TitoloOrig,  Titolo,  Sottotitolo,  AnnoEd,  Illustrazioni,  ISBN,  Genere,  NumPub,  CopertinaRigida,  Ristampa,  nRistampa,  Edizione,  NumPagine,  Curatore,  NomeTr,  CognomeTr,  NazioneTr, NomeCu, CognomeCu, NazioneCu)
            return render(request, 'detail.html', {'context':elemento})
    else:
        print("Errore")
"""
def HomePageViewSeriale(request):
    #visualizza solo libri seriali
    if request.method == 'GET':
        context=[]
        #visualizza campi essenziale per libri seriali
        for record in Seriale.object.raw("SELECT S.Titolo, T.NomeTr, T.CognomeTr, S.Genere FROM libri_Seriale S, libri_TradAutCur T WHERE S.IDAutoreCuratore_id=T.CodAutore"):
            elemento = objlist()
            elemento.inserimentoHome(record.Titolo,record.NomeTr+" "+record.CognomeTr,record.Genere)
            context.append(elemento)
        return render(request, 'Serial.html',{'context_list':context}) 
    else:
        print("Errore")
        
def HomePageViewNonSeriale(request):
    #visualizza solo libri non seriali
    if request.method == 'GET':
        context=[]
        #visualizza campi essenziale per libri non seriali
        for record in NonSeriale.object.raw("SELECT N.Titolo, T.NomeTr, T.CognomeTr, N.Genere FROM libri_NonSeriale N, libri_TradAutCur T WHERE N.IDAutoreCuratore_id=T.CodAutore"):
            elemento = objlist()
            elemento.inserimentoHome(record.Titolo,record.NomeTr+" "+record.CognomeTr,record.Genere)
            context.append(elemento)
        return render(request, 'notSerial.html',{'context_list':context}) 
    else:
        print("Errore")
"""

def HomePageView(request):
    #homepage che visualizza tutti i libri
    if request.method == 'GET':
        context=[]
        #visualizza campi essenziale per libri non seriali
        for record in NonSeriale.objects.raw("SELECT N.CodLibro,N.Titolo,T.NomeTr,T.CognomeTr,N.Genere,N.ISBN FROM libri_NonSeriale N, libri_TradAutCur T WHERE N.IDAutoreCuratore_id=T.CodAutore"):
            elemento = objlist()
            elemento.inserimentoHome(record.Titolo,record.NomeTr+" "+record.CognomeTr,record.Genere,record.CodLibro,record.ISBN)
            #print(elemento.CodLibro)
            context.append(elemento)
        #visualizza campi essenziali per libri seriali
        for record in Seriale.objects.raw("SELECT S.CodLibro,S.Titolo,T.NomeTr,T.CognomeTr,S.Genere FROM libri_Seriale S, libri_TradAutCur T WHERE S.IDAutoreCuratore_id=T.CodAutore"):
            elemento = objlist()
            elemento.inserimentoHome(record.Titolo,record.NomeTr+" "+record.CognomeTr,record.Genere,record.CodLibro," ")
            #print(elemento.CodLibro)
            context.append(elemento)


        return render(request, 'index.html',{'context_list':context}) 
    else:
        print("Errore")

def UtentiIn(request): 

    if request.method == 'POST':
        form = PrenotazioneForm(request.POST)
        NomeUt=request.POST.get("NomeU")
        CognomeUt=request.POST.get("CognomeU")
        Email=request.POST.get("Email")
        NumeroTelefono=request.POST.get("NumTelefono")
        dati={"NomeUt":NomeUt,"CognomeUt":CognomeUt,"Email":Email,"NumeroTelefono":NumeroTelefono}
        cod=inspector(dati,"U")

        return cod

def PrenotazioneView(request):

    if request.method == 'GET':
        form=PrenotazioneForm()
        return render(request, 'prenotazione.html',{"form":form})    
        
    if request.method == 'POST':

        ritardo=False

        UtentiIn(request)
        data=inData(request)
        idlib=CodLibro(request)
        codU=UtentiIn(request)

        while True:
            cod = "R"+str(randrange(1000))
            if check(cod):
                break

        cod = "R"+str(randrange(1000))

        query="INSERT INTO libri_Prestito VALUES(%s,%s,%s,%s,%s,%s)"                                                        #CHECK
        dati=[cod,data[1],data[0],ritardo,idlib,codU]

        cursor=cursor.connection()
        cursor.execute(query,dati)
        cursor.close()
        return render(request, 'base.html',{"form":form})  

def UtentiIn(request):

    if request.method == 'POST':
        form = PrenotazioneForm(request.POST)
        NomeUt=request.POST.get("NomeU")
        CognomeUt=request.POST.get("CognomeU")
        Email=request.POST.get("Email")
        NumeroTelefono=request.POST.get("NumTelefono")
        dati={"NomeUt":NomeUt,"CognomeUt":CognomeUt,"Email":Email,"NumeroTelefono":NumeroTelefono}
        cod=inspector(dati,"U")

        return cod
        
def inData(request):
    
    if request.method == 'POST':
        form = PrenotazioneForm(request.POST)
        if form.is_valid():

            DataInizio = request.POST.get("DataInizio")
            DataFine = request.POST.get("DataFine")
            return [DataFine,DataInizio]

        else:

            print(form.errors)
            return HttpResponseRedirect(reverse('#errore'))

def CodLibro(request):
    
    if request.method == 'POST':
        cursor = connection.cursor()
        form = PrenotazioneForm(request.POST)
        if form.is_valid():

            IDLibro = request.POST.get("IDLibro")
            return IDLibro

        else:
            print(form.errors)
            return HttpResponseRedirect(reverse('#errore'))
        
def CheckRitardo():
    oggi = datetime.date.today()
    cursor = connection.cursor()
    query = "UPDATE Prestito SET Ritardo = true WHERE DataFine < %s"
    cursor.execute(query,[oggi,])
    cursor.close()

def PrestitoPageView(request):
    CheckRitardo()
    if request.method == 'GET':
        context = []
        query = "SELECT P.DataInizio, P.Datafine, U.NomeUt, U.CognomeUt, U.NumTelefono, P.Ritardo FROM libri_Prestito P, libri_Utenti U WHERE P.IDUtente = U.CodUser ORDER BY P.Datafine"
        ris = Prestito.objects.raw(query)

        for record in ris:
            elemento = listaPrestiti()
            elemento.inserimento(record.DataInizio, record.DataFine, record.NomeUt, record.CognomeUt, record.NumTelefono, record.Ritardo)
            context.append(elemento)

def invDef(codlib):
    cursor = connection.cursor()

    cod="L"+str(randrange(1000))
    
    if codlib[0] == 'N':                                                                  #In base al identificatore si decide se eliminare o inserire un libro
        query="INSERT INTO libri_SingoliLibri(CodLibro,IDNonseriale_id) VALUES(%s,%s)"       #nel inserimento si controlla il codice per capire se è seriale oppure no
    else:
        query="INSERT INTO libri_SingoliLibri(CodLibro,IDSeriale_id) VALUES(%s,%s)"

    cursor.execute(query,[cod,codlib])
    cursor.close()        
 
        #return
def Ghet(request, Cod):
    if request.method == 'GET':
        cursor = connection.cursor()
        if Cod[0]=='N':
            query="SELECT COUNT(*) FROM libri_SingoliLibri WHERE IDNonseriale_id=%s"

        if Cod[0]=='S':
            query="SELECT COUNT(*) FROM libri_SingoliLibri WHERE IDSeriale_id=%s"
        
        cursor.execute(query, [Cod,])
        numero_libri = cursor.fetchone()
        return numero_libri

    elif request.method == 'POST':
 
        form = InserimentoLibro(request.POST)
        if form.is_valid():
            if Cod[0]=='N':
                query="SELECT COUNT(*) FROM libri_SingoliLibri WHERE IDNonseriale_id=%s"
            

            if Cod[0]=='S':
                query="SELECT COUNT(*) FROM libri_SingoliLibri WHERE IDSeriale_id=%s"
               
        
                cursor.execute(query, [Cod,])
                numero_libri = cursor.fetchone()

            numero_inserito = request.POST.get("numero_inserito")
            
            if numero_inserito > numero_libri :
                ris = numero_inserito - numero_libri
                for x in range(ris):
                    invDef(Cod)
    else:
        print(form.errors)
        return HttpResponseRedirect(reverse('#errore'))
            
def del_singoloView(request):
    cursor = connection.cursor()
    #elimina la row in base al codice inserito
    if request.method =='POST':
        form = DelSingLib(request.POST)
        if form.is_valid():
            CodLibro = request.POST.get("CodLibro")
            query ="SELECT P.IDLibro FROM Prestito P, SingoliLibri S WHERE IDLibro_id=%s"
            cursor.execute(query,[CodLibro,])
            ris=cursor.fetchone()
            if ris is None:
                query="DELETE FROM libri_SingoliLibri WHERE CodLibro=%s"
                cursor.execute(query,[CodLibro,])
                cursor.close()
            else:


            return HttpResponseRedirect(reverse('base'))
        else:
            print(form.errors)
            return HttpResponseRedirect(reverse('#errore'))   

def ResetSingoloView(request,Cod):
    Testo=[]
        
def del_singololibro(request, Cod):
    cursor = connection.cursor()
    if request.method =='GET':
        query="DELETE FROM libri_SingoliLibri WHERE CodLibro=%s"
        cursor.execute(query,[Cod,])
        query = "DELETE FROM libri_Prestito P libri_SingoliLibri S WHERE P.IDLibro = S.CodLibro AND P.IDLibro=%s"
        cursor.execute(query,[Cod,])
        cursor.close()
        return HttpResponseRedirect(reverse('#'))
    else:
        return HttpResponseRedirect(reverse('#errore'))    

