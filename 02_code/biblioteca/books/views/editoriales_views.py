from django.shortcuts import render
from books.forms import EditorialCreate, EditorialModelFormCreate
from books.models import Editorial
from django.shortcuts import redirect
from django.urls import reverse

def editoriales_view(request):
    
    editoriales = Editorial.objects.all()

    context = {
        'editoriales' : editoriales
    }
    return render(request, "editoriales/editoriales.html", context)

def editorial_detail(request, id):

    editorial = Editorial.objects.get(pk=id)
    context = {
        "editorial": editorial,
    }
    return render(request, "editoriales/editorial_detail.html", context)



def editorial_create(request):
    if request.POST:
        form = EditorialModelFormCreate(request.POST)
        if form.is_valid():
            nueva_editorial = Editorial.objects.create(
                nombre = form.cleaned_data['nombre'],
                direccion = form.cleaned_data['direccion'],
                email = form.cleaned_data['email'],
                fecha_fundacion = form.cleaned_data['fecha_fundacion']
            )
            # Redireccionar a la vista detalle de la nueva editorial creada
            return redirect(reverse('books:editorial_detail', kwargs={'id': nueva_editorial.pk}))
    else:
        form = EditorialModelFormCreate()

    context = {
        'form': form
    }
    return render(request, "editoriales/editorial_create.html", context)
