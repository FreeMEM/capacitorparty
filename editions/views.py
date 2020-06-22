from django.shortcuts import render
from capacitorparty.utils.menus import Menus
from editions.models import Edition, EditionPicture


def index(request):
    menu = Menus()
    current_party = Edition.objects.first()
    return render(request, "editions/current.html", dict(main_menu=menu.main_menu, current_party=current_party))


def editions(request):
    menu = Menus()
    pictures = EditionPicture.objects.select_related('edition').all()
    editions = {}
    for picture in pictures:
        editions[picture.edition] = True
    return render(request, "editions/editions.html", dict(main_menu=menu.main_menu, pictures=pictures, editions=editions.keys()))
