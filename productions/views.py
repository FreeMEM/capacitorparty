from django.shortcuts import render, redirect, get_object_or_404
from capacitorparty.utils.menus import Menus
from productions.models import ProductionType, Production
from productions.forms import ProductionForm
import inflect


# Create your views here.


def productions(request):
    menu = Menus()
    productions = Production.objects.exclude(published_date__isnull=True).order_by('production_type')
    return render(request, "productions/productions.html", dict(main_menu=menu.main_menu, productions=productions))

def production(request, production_id):
    menu = Menus()
    production = get_object_or_404(Production, pk=production_id)
    inf = inflect.engine()
    print("UEEEEEEEE1")
    print(inf.ordinal(production.classification))
    print("UEEEEEEEE2")
    return render(request, "productions/production.html", dict(main_menu=menu.main_menu, production=production, clasificacion=inf.ordinal(production.classification)))

def upload(request):
    menu = Menus()
    if request.method == 'POST':
        form = ProductionForm(request.POST, request.FILES)
        if form.is_valid():
            
            instance = Production(filepath=request.FILES['filepath'],
                                title=request.POST['title'],
                                description=request.POST['description'],
                                production_type=request.POST['production_type'] )
            print(Production.production_type)
            instance.save()
            return redirect('productions')
        else:
            print("NO ES VALIDO")
            print(form)
        # return redirect('productions:productions')
        
    else:
        form = ProductionForm()
        form.use_required_attribute=False
    
    return render(request, "productions/upload.html", dict(main_menu=menu.main_menu, form=form))

