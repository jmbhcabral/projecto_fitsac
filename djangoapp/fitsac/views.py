''' Views para a aplicação fitsac '''
from django.shortcuts import render
from django.urls import reverse
from user_dashboard.models import (
    SectionOne, SectionTwo, SectionThree, SectionFour, SectionFiveHeader,
    Card, SectionSix, SectionEight, SectionNine, TiposDeAulas
)
from django.contrib import messages
from fitsac.forms import ContactForm


def index(request):
    section_one = SectionOne.objects.filter(is_visible=True).first()
    section_two = SectionTwo.objects.filter(is_visible=True).first()
    section_three = SectionThree.objects.filter(is_visible=True).first()
    section_four = SectionFour.objects\
        .filter(is_visible=True, order__range=(1, 6))\
        .order_by('order')
    # Section Five
    header = SectionFiveHeader.objects.filter(is_visible=True).first()
    cards = Card.objects\
        .order_by('order')\
        .all()
    section_six = SectionSix.objects\
        .filter(is_visible=True)\
        .first()

    video = SectionEight.objects.filter(is_visible=True).first()

    services = SectionNine.objects\
        .filter(is_visible=True, order__range=(1, 3))\
        .all()

    return render(
        request,
        'fitsac/pages/index.html',
        {
            'section_one': section_one,
            'section_two': section_two,
            'section_three': section_three,
            'section_four': section_four,
            'header': header,
            'cards': cards,
            'section_six': section_six,
            'video': video,
            'services': services,

        },
    )


def about(request):

    return render(request, 'fitsac/pages/about.html')


def courses(request):
    services = SectionNine.objects\
        .filter(is_visible=True, order__range=(1, 3))\
        .all()

    courses = TiposDeAulas.objects\
        .filter(is_visible=True)\
        .all()

    context = {
        'services': services,
        'courses': courses,
    }

    return render(request, 'fitsac/pages/courses.html', context)


def pricing(request):
    return render(request, 'fitsac/pages/pricing.html')


def gallery(request):
    section_one = SectionOne.objects.filter(is_visible=True).first()

    section_four = SectionFour.objects\
        .filter(is_visible=True)\
        .order_by('order')\
        .all()

    services = SectionNine.objects\
        .filter(is_visible=True, order__range=(1, 3))\
        .all()

    context = {
        'section_one': section_one,
        'section_four': section_four,
        'services': services,
    }
    return render(request, 'fitsac/pages/gallery.html', context)


def blog(request):
    return render(request, 'fitsac/pages/blog.html')


def blog_details(request):
    return render(request, 'fitsac/pages/blog_details.html')


def contact(request):
    services = SectionNine.objects\
        .filter(is_visible=True, order__range=(1, 3))\

    form_action = reverse('fitsac:contact')

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Mensagem enviada com sucesso!')
            form = ContactForm()  # Cria uma nova instância do formulário vazio
            return render(request, 'fitsac/pages/contact.html', {
                'form': form,
                'form_action': form_action
            })
        else:
            messages.error(
                request, 'Corrige os erros abaixo e tenta novamente.')

    else:
        form = ContactForm()

    return render(request, 'fitsac/pages/contact.html', {
        'form': form,
        'form_action': form_action,
        'services': services,
    })


def admin(request):
    return render(request, 'fitsac/admin/admin-home.html')
