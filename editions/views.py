from django.shortcuts import render

from editions.models import Edition, EditionPicture


def index(request):

    current_party = Edition.objects.first()
    return render(request, "editions/current.html", dict(current_party=current_party))


def editions(request):

    pictures = EditionPicture.objects.select_related('edition').all()
    editions = {}
    for picture in pictures:
        editions[picture.edition] = True
    return render(request, "editions/editions.html", dict(pictures=pictures, editions=editions.keys()))


def author(request, author_id):

    author = get_object_or_404(Scener, pk=author_id)
    groups = ScenersGroup.objects.filter(member=author)

    return render(request, "productions/author.html", dict(scener=author, groups=groups))