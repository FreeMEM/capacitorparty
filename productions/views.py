from django.shortcuts import render, redirect, get_object_or_404
from productions.models import ProductionType, Production, Scener, ScenersGroup
from productions.forms import ProductionForm
import inflect


# Create your views here.


def productions(request):
    
    productions = Production.objects.exclude(published_date__isnull=True).order_by('production_type')
    return render(request, "productions/productions.html", dict(productions=productions))

def production(request, production_id):
    
    production = get_object_or_404(Production, pk=production_id)
    inf = inflect.engine()
    clasificacion=None
    if production.classification:
        clasificacion = inf.ordinal(production.classification)

    return render(request, "productions/production.html", dict(production=production, clasificacion=clasificacion))

def author(request, author_id):

    author = get_object_or_404(Scener, pk=author_id)
    productions = Production.objects.filter(authors=author)

    groups = ScenersGroup.objects.filter(member=author)

    return render(request, "productions/author.html", dict(scener=author, groups=groups, productions=productions))


def upload(request):
    if request.method == 'POST':
        form = ProductionForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Production(filepath=request.FILES['filepath'],
                                title=request.POST['title'],
                                description=request.POST['description'],
                                production_type=request.POST['production_type'] )
            
            instance.save()
            return redirect('productions')
    else:
        form = ProductionForm()
        # form.use_required_attribute=False
    return render(request, "productions/upload.html", dict(form=form))

