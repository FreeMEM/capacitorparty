from django.shortcuts import render, redirect
from capacitorparty.utils.menus import Menus
from productions.models import ProductionType, Production
from productions.forms import ProductionForm
# Create your views here.


def productions(request):
    menu = Menus()
    productions = Production.objects.exclude(published_date__isnull=True).order_by('production_type')
    return render(request, "productions/productions.html", dict(main_menu=menu.main_menu, productions=productions))

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

