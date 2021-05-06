from django import forms
from  django.core.exceptions import ValidationError
#from  django.core import validator
from  .models  import Titoli2


from django.contrib.auth.models import  User

class FormContatto(forms.Form):
   nome = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
   cognome = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
   email   =  forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control"}))
   contenuto = forms.CharField(widget= forms.Textarea(attrs={"placeholder":"Area Testuale scrivi pure", "class":"form-control"}))


class FormTitoli(forms.Form):
    codtitv= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    codslugtitv = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    codauthortitv = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))              
    codisintitv= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    codbodytitv = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    codpublishtitv= forms.DateTimeField(widget=forms.TextInput(attrs={"class":"form-control"}))
    codcreatedtitv = forms.DateTimeField(widget=forms.TextInput(attrs={"class":"form-control"}))
    codupdatedtitv = forms.DateTimeField(widget=forms.TextInput(attrs={"class":"form-control"}))
    codmintitv = forms.FloatField(widget=forms.TextInput(attrs={"class":"form-control"}))
    codmaxtitv = forms.FloatField(widget=forms.TextInput(attrs={"class":"form-control"}))


class TitoliModelForm (forms.ModelForm):
  
    class Meta:
       model = Titoli2
       fields = "__all__"
    


def clean_contenuto(self):
   dati = self.cleaned_data["contenuto"]
   if "parola" in dati:
      raise ValidationError("la stringa non e' ammessa")
   return  dati



class FormRegistrazioneUser(forms.ModelForm):

   username = forms.CharField(widget=forms.TextInput())
   email = forms.CharField(widget=forms.EmailInput())
   password = forms.CharField(widget=forms.PasswordInput())
   conferma_password = forms.CharField(widget=forms.PasswordInput())

   class Meta:
      model = User
      fields = ["username", "email", "password", "conferma_password"]


   def clean(self):
      super().clean()
      password = self.cleaned_data["password"]
      conferma_password = self.cleaned_data["conferma_password"]

      if password != conferma_password:
          raise forms.ValidationError("le password non sono identiche")
      return self.cleaned_data


      
      
      
      
      
      
      
      
      
      
      