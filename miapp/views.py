from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

layout="""
    <h1>A</h1>
    <hr>
    <ul>
        <li>
            <a href="/saludo">Hola</a>
        </li>
    </ul>
    </hr>
"""
def saludo (request):
    mensaje="""
    <h1>Bienvenidos</h1>
    <h2>Jose Enrique Huaycho Mamani</h2>
    """
    return HttpResponse(layout+mensaje)

def index (request):
    return render(request, 'index.html')
