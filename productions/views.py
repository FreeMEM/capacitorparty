from django.shortcuts import render
from capacitorparty.utils.menus import Menus
from productions.models import ProductionType, Production
# Create your views here.


def productions(request):
    menu = Menus()
    productions = Production.objects.exclude(published_date__isnull=True).order_by('production_type')
    return render(request, "productions/productions.html", dict(main_menu=menu.main_menu, productions=productions))
