from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from funzioniiot.forms import FormContatto

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import TemplateView

from .models import Titoli2, Giornalista,  PublishedManager, Cliente
from funzioniiot.forms import FormContatto, FormTitoli, TitoliModelForm, FormRegistrazioneUser

# Create your views here.



def hellocontattaci(request):
    if request.method == 'POST':
        form = FormContatto(request.POST)
        if form.is_valid():
            print("il form e' valido")
            print("NomE ",  form.cleaned_data["nome"])
            print("Cognome ",  form.cleaned_data["cognome"])
            return HttpResponse("<h1> Grazie per averci contattato </h1>")

    else:
        form = FormContatto()
    context = {"form": form}
    import os
    print("prova")
    print(os.path.abspath(os.getcwd()))
    return render(request, 'funzioniiot/post/contattaci.html', context)


def titoli_list(request):
    posts = Titoli2.objects.all()
    object_list = Titoli2.objects.all()
    paginator = Paginator(object_list, 3)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/list.html', {'page': page, 'posts': posts})


def clienti_list(request):
    cli = Cliente.objects.all()
    object_list = Cliente.objects.all()
    paginator = Paginator(object_list, 3)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/listcli.html', {'page': page, 'posts': posts})


def titoli_detail(request, year, month, day, post):
    post = get_object_or_404(Titoli2, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})


def crea_titoli(request):
    if request.method == 'POST':
        form = TitoliModelForm(request.POST)
        if form.is_valid():
            # inserimento dati nel data base
            new_titolo = form.save()
            titolo = Titoli2.objects.all()
            context = {"titoli": titolo}
            return render(request, 'blog/post/homepage2.html', context)

    else:
        form = TitoliModelForm()
    context = {"form": form}
    return render(request, "blog/post/institoli.html", context)


def mod_titoli(request):
    if request.method == 'POST':
        pk1 = request.POST.get("pk")
        print(pk1)
        codtit = request.POST.get("codtit2")
        codslugtit = request.POST.get("codslugtit2")
        isin = request.POST.get("isin")
        body = request.POST.get("body")
        autor = request.POST.get("autor")
        Titoli2.objects.filter(pk=pk1).update(codtit2=codtit, codslugtit2=codslugtit,  codisintit2=isin, codbodytit2=body, codpublishtit2=datetime.datetime.now(
        ), codcreatedtit2=datetime.datetime.now(), codupdatedtit2=datetime.datetime.now(), codmintit2=1, codmaxtit2=10)
        titolo = Titoli2.objects.all()
        context = {"titoli": titolo}
        return render(request, 'blog/post/homepage2.html', context)


def can_titoli(request):
    if request.method == 'POST':
        pk = request.POST.get("pk")
        titol = Titoli2.objects.get(id=pk)
        titol.delete()
        titolo = Titoli2.objects.all()
        context = {"titoli": titolo}
        return render(request, 'blog/post/homepage2.html', context)


def visuatitoli(request):
    return render(request, "contattaci.html", context)

def homeiot(request):
    return render(request, "funzioniiot/post/scelta.html")


def homeTitoly(request):
    titolo = Titoli2.objects.all()
    context = {"titoli": titolo}
    return render(request, 'blog/post/homepage2.html', context)

class AboutView(TemplateView):
    template_name = "blog/post/about2.html"



def titoloDetailView(request, pk):
    titolo = Titoli2.objects.get(pk=pk)
    context = {"titoli": titolo}
    return render(request, 'blog/post/titolo_detail.html', context)

#  CBV   Class Based Views
#  Documentazione ufficiale


class TitoloDetailViewCB(DetailView):
    model = Titoli2
    template_name = "titolo_detail.html"


class Titoli_list_view(ListView):
    model = Titoli2
    template_name = "lista_titoli.html"


class Clienti_list_view(ListView):
    model = Cliente
    template_name = "lista_clienti.html"


def home(request):
    g = []
    for gio in Giornalista.objects.all():
        g.append(gio.nome)
    response = str(g)
    print(response)
    return HttpResponse(response, content_type='text/plain')
