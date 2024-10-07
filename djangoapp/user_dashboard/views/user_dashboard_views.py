from django.shortcuts import render, get_object_or_404
from user_dashboard.models import (
    SectionOne, SectionTwo, SectionThree, SectionFour, Card,
    SectionFiveHeader, SectionSix, SectionEight, SectionNine,
    TiposDeAulas
)
from django.contrib import messages


def admin_home(request):
    return render(request, 'user_dashboard/pages/admin-home.html')


def section_one(request):
    section_one = SectionOne.objects.all().first()
    context = {
        'section_one': section_one,
    }
    return render(request,
                  'user_dashboard/pages/section-one.html',
                  context,
                  )


def section_two(request):
    section_two = SectionTwo.objects.all().first()
    context = {
        'section_two': section_two,
    }
    return render(request,
                  'user_dashboard/pages/section-two.html',
                  context,)


def section_three(request):
    section_three = SectionThree.objects.all().first()
    context = {
        'section_three': section_three,
    }
    return render(request,
                  'user_dashboard/pages/section-three.html',
                  context,)


def section_four(request):
    section_four = SectionFour.objects\
        .all()\
        .order_by('order')
    context = {
        'section_four': section_four,
    }
    return render(request, 'user_dashboard/pages/section-four.html', context)


def section_five(request):
    header = SectionFiveHeader.objects.filter(is_visible=True).first()
    cards = Card.objects\
        .order_by('order')\
        .all()
    context = {
        'header': header,
        'cards': cards,
    }
    return render(
        request,
        'user_dashboard/pages/section-five.html',
        context)


def section_six(request):
    section_six = SectionSix.objects\
        .all()

    context = {

        'section_six': section_six,
    }
    return render(
        request,
        'user_dashboard/pages/section-six.html',
        context
    )


def section_seven(request):
    return render(request, 'user_dashboard/pages/section-seven.html')


def section_eight(request):
    videos = SectionEight.objects.all()
    escolhas = []

    for video in videos:
        print(video.is_visible)
        if video.is_visible:
            escolhas.append('Video escolhido!')
        else:
            escolhas.append('Video não escolhido!')

    context = {
        'videos': zip(videos, escolhas),
    }

    if escolhas.count('Video escolhido!') > 1:
        print(f'Escolhas: {escolhas.count("Video escolhido!")}')
        messages.error(request, 'Você só pode escolher um vídeo!')
        return render(request, 'user_dashboard/pages/section-eight.html', context)

    return render(request, 'user_dashboard/pages/section-eight.html', context)


def section_nine(request):
    services = SectionNine.objects\
        .filter(is_visible=True)\
        .order_by('order')

    print(f'Services: {services}')

    context = {
        'services': services,
    }

    return render(
        request,
        'user_dashboard/pages/section-nine.html',
        context
    )


def classes_type(request):
    tipos_de_aulas = TiposDeAulas.objects\
        .filter(is_visible=True)\
        .order_by('order')

    context = {
        'tipos_de_aulas': tipos_de_aulas,
    }

    return render(
        request,
        'user_dashboard/pages/classes-type.html',
        context
    )


def classes_type_single_class(request, id):
    tipo_de_aula = get_object_or_404(TiposDeAulas, id=id)

    context = {
        'tipo_de_aula': tipo_de_aula,
    }

    return render(
        request,
        'user_dashboard/pages/classes-type-single-class.html',
        context
    )
