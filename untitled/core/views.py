from django.shortcuts import render, HttpResponse

html_base = '''
<h1>Mi web personal</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about/">Acerca de</a></li>
    <li><a href="/portfolio/">Portfolio</a></li>
    <li><a href="/contacto/">Contacto</a></li>
</ul>
'''

# Create your views here.
def home(request):
    return render(request, "core/home.html")



def about(request):
    #html_response = "<h1>Sobre Mi</h1><h2>Personal</h2><p>Me llamo Abraham y soy Ingeniero</p>"

    return render(request, "core/about.html")


def portfolio(request):
    return render(request, "core/portfolio.html")



def contacto(request):
    return render(request, "core/contacto.html")