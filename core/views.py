from django.shortcuts import render,HttpResponse
html_base="""
<h1>Mi web personal</h1>
<ul>
<li><a href="/">Portada</a></li>
<li><a href="/about-me">About me</a></li>
<li><a href="/portfolio">Portafolio</a></li>
<li><a href="/contact">Contactame</a></li>
</ul>
"""
# Create your views here.
def Home(request):
    return render(request,"core/home.html")
def About(request):
    return render(request,"core/aboutme.html")

def Contacto(request):
    return render(request,"core/contacto.html")
       