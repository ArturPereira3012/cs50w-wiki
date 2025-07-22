from django.shortcuts import render, redirect
from . import util
import markdown2
import random
from django.utils.html import escape

def get_actual_title(title):
    """Encontra o título real (case-insensitive)"""
    entries = util.list_entries()
    entry_map = {e.lower(): e for e in entries}  # Mapeia minúsculas para títulos originais
    return entry_map.get(title.lower())

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    # Verificar se é o caso especial (qualquer variação de "TITLE")
    if title.lower() == "title":
        return index(request)  # Mostra a página inicial
    
    # Buscar entrada normal (case-insensitive)
    actual_title = get_actual_title(title)
    if not actual_title:
        return render(request, "encyclopedia/error.html", {
            "message": "A página solicitada não foi encontrada."
        })
    
    content = util.get_entry(actual_title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": "Entrada corrompida ou vazia."
        })
    
    # Converter Markdown para HTML
    escaped_content = escape(content)
    html_content = markdown2.markdown(escaped_content)
    
    return render(request, "encyclopedia/entry.html", {
        "title": actual_title,  # Usa título original
        "content": html_content
    })
def search(request):
    query = request.GET.get("q", "")
    entries = util.list_entries()
    
    # Verificar correspondência exata
    if query in entries:
        return redirect("entry", title=query)
    
    # Busca por substring
    results = [entry for entry in entries if query.lower() in entry.lower()]
    
    return render(request, "encyclopedia/search.html", {
        "results": results,
        "query": query
    })

def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        
        # Verificar se entrada já existe
        if util.get_entry(title):
            return render(request, "encyclopedia/error.html", {
                "message": "Uma entrada com esse título já existe."
            })
        
        # Salvar nova entrada
        util.save_entry(title, content)
        return redirect("entry", title=title)
    
    return render(request, "encyclopedia/create.html")

def edit(request, title):
    if request.method == "POST":
        content = request.POST.get("content")
        util.save_entry(title, content)
        return redirect("entry", title=title)
    
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": "A página solicitada não foi encontrada."
        })
    
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "content": content
    })

def random_page(request):
    entries = util.list_entries()
    if not entries:
        return render(request, "encyclopedia/error.html", {
            "message": "Nenhuma entrada disponível."
        })
    
    entry_title = random.choice(entries)
    return redirect("entry", title=entry_title)