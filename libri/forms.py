from django import forms
from libri.models import *



class InserimentoLibro(forms.Form):
    #Casa Editrice
    NomeCa = forms.CharField(label="Nome CasaEd", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Nome Casa Editrice*'}))
    SedeCa = forms.CharField(label="Sede CasaEd", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Sede Casa Editrice*'}))
    
    #Info Autore
    NomeAu = forms.CharField(label="Nome Autore", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Nome Autore*'}))
    CognomeAu = forms.CharField(label="Cognome Autore", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Cognome Autore*'}))
    NazioneAu = forms.CharField(label="Nazione Autore", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Nazione Autore*'}))
    
    #Postfazione
    NomePost = forms.CharField(label="Nome AutorePost", max_length=256, required=False, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Nome Autore Postfazione'}))
    CognomePost = forms.CharField(label="Cognome AutorePost", max_length=256, required=False, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Cognome Autore Postfazione'}))
    NazionePost = forms.CharField(label="Nazione AutorePost", max_length=256, required=False, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Nazione Autore Postfazione'}))
    
    #Prefazione
    NomePre = forms.CharField(label="Nome AutorePre", max_length=256, required=False, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Nome Autore Prefazione'}))
    CognomePre = forms.CharField(label="Cognome AutorePre", max_length=256, required=False, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Cognome Autore Prefazione'}))
    NazionePre = forms.CharField(label="Nazione AutorePre", max_length=256, required=False, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Nazione Autore Prefazione'}))
    
    #Info Libro
    TitoloOrig = forms.CharField(label="Titolo Originale", max_length=256, required=False, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Titolo Originale'}))
    Titolo = forms.CharField(label="Titolo", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Titolo*'}))
    Straniero = forms.ChoiceField(choices = (('1','Si'),('0','No')))
    Sottotitolo = forms.CharField(label="Sottotitolo", max_length=256, required=False, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Sottotitolo'}))
    #Genere = forms.CharField(label="Genere", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Genere'}))
    Genere = forms.ChoiceField(choices = 
        ((' ',' '),
        ('Fantascienza','Fantascienza'),
        ('Romance','Romance'),
        ('Fantasy','Fantasy'),
        ('Storico','Storico'),
        ('Avventura','Avventura'),
        ('Horror','Horror'),
        ('Thriller','Thriller'),
        ('Giallo','Giallo'),
        ('Umoristico','Umoristico'),
        ('Erotico','Erotico'),
        ('Fiabesco','Fiabesco'),
        ('Biografico','Biografico'),
        ('Antologico','Antologico'),
        ('Poesia','Poesia'),
        ('Divulgazione','Divulgazione'),
        ('Scolastico','Scolastico'),
        ('Tragedia','Tragedia'),
        ('Monologo','Monologo'),
        ))
    IsSerial = forms.ChoiceField(choices = (('on','Si'),('off','No')))
    #Info Edizione
    AnnoEd = forms.CharField(label="Anno Edizione", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Anno Edizione*'}))
    ISBN_ISSN = forms.CharField(label="ISBN ISSN", max_length=16, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'ISBN / ISSN*'}))
    NumPub = forms.CharField(label="Numero Pub", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Numero Pubblicazione*'}))
    CopertinaRigida = forms.ChoiceField(choices = (('1','Si'),('0','No')))
    Illustrazioni = forms.ChoiceField(choices = (('1','Si'),('0','No')))
    Ristampa = forms.ChoiceField(choices = (('1','Si'),('0','No')))
    nRistampa = forms.CharField(label="Num Ristampa", required=False, max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Numero di ristampa'}))
    Edizione = forms.CharField(label="Edizione", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Edizione*'}))
    NumPagine = forms.CharField(label="NumPagine", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Numero Pagine*'}))
    Curatore = forms.ChoiceField(choices = (('1','Si'),('0','No')))
    NomeCo = forms.CharField(label="Nome Collana", max_length=256, required=False, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Nome Collana'}))
    
    #Traduttore
    NomeTr = forms.CharField(label="Nome Traduttore", max_length=256, required=False, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Nome Traduttore'}))
    CognomeTr = forms.CharField(label="Cognome Traduttore", max_length=256, required=False, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Cognome Traduttore'}))
    NazioneTr = forms.CharField(label="Nazione Traduttore", max_length=256, required=False, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Nazione traduttore'}))
    
    #Critico
    NomeCu = forms.CharField(label="Nome Critco", max_length=256, required=False, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Nome critico'}))
    CognomeCu = forms.CharField(label="Cognome Critico", max_length=256, required=False, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Cognome critico'}))
    NazioneCu = forms.CharField(label="Nazione Critico", max_length=256, required=False, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Nazione critico'}))
    
    #Singoli libri
    QLibri = forms.CharField(label="QLibri", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Quantità Libri*'}))
    
    #Scaffale
    #CodScaffale = forms.CharField(label="Codice Scaffale", max_length=4, widget=forms.TextInput(attrs={'class' : 'formBox'}))
    #CatScaffale = forms.CharField(label="Categoria Scaffale", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox'}))
    
class PrenotazioneForm(forms.Form):
    NomeU = forms.CharField(label="NomeU",max_length = 256, widget = forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Nome Utente*'}))
    CognomeU = forms.CharField(label="CognomeU",max_length = 256, widget = forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Cognome Utente*'}))
    Email = forms.CharField(label="Email",max_length = 256,required=False, widget = forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Email*'}))
    NumTelefono = forms.CharField(label="NumTelefono",max_length = 10, widget = forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Numero Telefono*'}))

    DataInizioG = forms.CharField(label="DataInizioG",max_length = 2, widget = forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'gg'}))
    DataInizioM = forms.CharField(label="DataInizioM",max_length = 2, widget = forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'mm'}))
    DataInizioA = forms.CharField(label="DataInizioA",max_length = 4, widget = forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'aa'}))

    DataFineG = forms.CharField(label="DataFineG",max_length = 2, widget = forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'gg'}))
    DataFineM = forms.CharField(label="DataFineM",max_length = 2, widget = forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'mm'}))
    DataFineA = forms.CharField(label="DataFineA",max_length = 4, widget = forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'aa'}))

    IDLibro = forms.CharField(label = "IDLibro", max_length = 4,  widget = forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'IDLibro'}))
    
class DelSingLib(forms.Form):
    Numero = forms.CharField(label="CodLib", max_length=256, widget = forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'IDLibro*'}))

class UserRegistrationForm(forms.Form):
    Username = forms.CharField(label="Username", max_length = 256, widget=forms.TextInput(attrs={'class' : 'logclass', 'placeholder':'Username'}))
    Password = forms.CharField(label="Password", max_length = 256, widget=forms.PasswordInput(attrs={'class' : 'logclass', 'placeholder':'Password'}))

class UserLoginForm(forms.Form):
    Username = forms.CharField(label="Username", max_length = 256, widget=forms.TextInput(attrs={'class' : 'logclass', 'placeholder':'Username'}))
    Password = forms.CharField(label="Password", max_length = 256, widget=forms.PasswordInput(attrs={'class' : 'logclass', 'placeholder':'Password'}))


class ricercaform(forms.Form):
    Campo = forms.CharField(label="camporicerca", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Ricerca per NomeAutore,Genere,Titolo,'}))
