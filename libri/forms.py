from django import forms
from libri.models import *

class InserimentoLibro(forms.Form):
    #Casa Editrice
    NomeCa = forms.CharField(label="Nome CasaEd", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Nome Casa Editrice'}))
    SedeCa = forms.CharField(label="Sede CasaEd", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Sede Casa Editrice'}))
    
    #Info Autore
    NomeAu = forms.CharField(label="Nome Autore", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Nome Autore'}))
    CognomeAu = forms.CharField(label="Cognome Autore", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Cognome Autore'}))
    NazioneAu = forms.CharField(label="Nazione Autore", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Nazione Autore'}))
    
    #Postfazione
    NomePost = forms.CharField(label="Nome AutorePost", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Nome Autore Postfazione'}))
    CognomePost= forms.CharField(label="Cognome AutorePost", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Cognome Autore Postfazione'}))
    NazionePost = forms.CharField(label="Nazione AutorePost", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Nazione Autore Postfazione'}))
    
    #Prefazione
    NomePre = forms.CharField(label="Nome AutorePre", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Nome Autore Prefazione'}))
    CognomePre = forms.CharField(label="Cognome AutorePre", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Cognome Autore Prefazione'}))
    NazionePre = forms.CharField(label="Nazione AutorePre", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Nazione Autore Prefazione'}))
    
    #Info Libro
    TitoloOrig = forms.CharField(label="Titolo Originale", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Titolo Originale'}))
    Titolo = forms.CharField(label="Titolo", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Titolo'}))
    Straniero = forms.BooleanField(label="Straniero", widget=forms.TextInput(attrs={'class' : 'formBox'}))
    Sottotitolo = forms.CharField(label="Sottotitolo", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox'}))
    Genere = forms.CharField(label="Genere", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Genere'}))
    IsSerial = forms.BooleanField(label="IsSerial", widget=forms.TextInput(attrs={'class' : 'formBox'}))
    
    #Info Edizione
    AnnoEd = forms.CharField(label="Anno Edizione", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox'}))
    ISBN_ISSN = forms.CharField(label="ISBN ISSN", max_length=16, widget=forms.TextInput(attrs={'class' : 'formBox'}))
    NumPub = forms.CharField(label="Numero Pub", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox'}))
    CopertinaRigida = forms.BooleanField(label="Copertina Rigida", widget=forms.TextInput(attrs={'class' : 'formBox'}))
    Illustrazioni = forms.BooleanField(label="Illustrazioni", widget=forms.TextInput(attrs={'class' : 'formBox'}))
    Ristampa = forms.BooleanField(label="Ristampa", widget=forms.TextInput(attrs={'class' : 'formBox'}))
    nRistampa = forms.CharField(label="Num Ristampa", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox'}))
    Edizione = forms.CharField(label="Edizione", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox'}))
    NumPagine = forms.CharField(label="Num Pagine", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox'}))
    Curatore = forms.BooleanField(label="Curatore", widget=forms.TextInput(attrs={'class' : 'formBox'}))
    NomeCo = forms.CharField(label="Nome Collana", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Nome Collana'}))
    
    #Traduttore
    NomeTr = forms.CharField(label="Nome Traduttore", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Nome Traduttore'}))
    CognomeTr = forms.CharField(label="Cognome Traduttore", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Cognome Traduttore'}))
    NazioneTr = forms.CharField(label="Nazione Traduttore", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Nazione traduttore'}))
    
    #Critico
    NomeCu = forms.CharField(label="Nome Critco", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Nome critico'}))
    CognomeCu = forms.CharField(label="Cognome Critico", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Cognome critico'}))
    NazioneCu = forms.CharField(label="Nazione Critico", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox', 'placeholder':'Nazione critico'}))
    
    #Scaffale
    CodScaffale = forms.CharField(label="Codice Scaffale", max_length=4, widget=forms.TextInput(attrs={'class' : 'formBox'}))
    CatScaffale = forms.CharField(label="Categoria Scaffale", max_length=256, widget=forms.TextInput(attrs={'class' : 'formBox'}))
