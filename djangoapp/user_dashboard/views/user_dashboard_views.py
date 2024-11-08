
from django.shortcuts import render, get_object_or_404, redirect
from user_dashboard.models import (
    SectionOne, SectionTwo, SectionThree, SectionFour, Card,
    SectionFiveHeader, SectionSix, SectionEight, SectionNine,
    TiposDeAulas
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def admin_home(request):
    ''' Admin home page. '''

    # Check if the user is in the _admin group
    if not request.user.groups.filter(name='_admin').exists():
        return redirect('user_profiles:user_account')

    return render(request, 'user_dashboard/pages/admin-home.html')


@login_required(login_url='/login/')
def admin_site_config(request):
    ''' Admin site configuration page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    return render(request, 'user_dashboard/pages/admin-site-config.html')


@login_required(login_url='/login/')
def section_one(request):
    ''' Section one page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    section_one = SectionOne.objects.all().first()
    context = {
        'section_one': section_one,
    }
    return render(
        request,
        'user_dashboard/pages/section-one.html',
        context,
    )


@login_required(login_url='/login/')
def section_two(request):
    ''' Section two page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    section_two = SectionTwo.objects.all().first()
    context = {
        'section_two': section_two,
    }
    return render(
        request,
        'user_dashboard/pages/section-two.html',
        context,
    )


@login_required(login_url='/login/')
def section_three(request):
    ''' Section three page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    section_three = SectionThree.objects.all().first()
    context = {
        'section_three': section_three,
    }
    return render(
        request,
        'user_dashboard/pages/section-three.html',
        context,
    )


@login_required(login_url='/login/')
def section_four(request):
    ''' Section four page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    section_four = SectionFour.objects\
        .all()\
        .order_by('order')
    context = {
        'section_four': section_four,
    }
    return render(request, 'user_dashboard/pages/section-four.html', context)


@login_required(login_url='/login/')
def section_five(request):
    ''' Section five page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

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


@login_required(login_url='/login/')
def section_six(request):
    ''' Section six page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    section_six = SectionSix.objects.all()

    context = {

        'section_six': section_six,
    }
    return render(
        request,
        'user_dashboard/pages/section-six.html',
        context
    )


@login_required(login_url='/login/')
def section_seven(request):
    ''' Section seven page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    return render(request, 'user_dashboard/pages/section-seven.html')


@login_required(login_url='/login/')
def section_eight(request):
    ''' Section eight page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    videos = SectionEight.objects.all()
    escolhas = []

    for video in videos:
        if video.is_visible:
            escolhas.append('Video escolhido!')
        else:
            escolhas.append('Video não escolhido!')

    chani = 'Amo-te'

    context = {
        'videos': zip(videos, escolhas),
        'chani': chani,
    }

    if escolhas.count('Video escolhido!') > 1:
        messages.error(request, 'Você só pode escolher um vídeo!')
        return render(
            request,
            'user_dashboard/pages/section-eight.html',
            context
        )

    return render(request, 'user_dashboard/pages/section-eight.html', context)


@login_required(login_url='/login/')
def section_nine(request):
    ''' Section nine page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    services = SectionNine.objects\
        .filter(is_visible=True)\
        .order_by('order')

    context = {
        'services': services,
    }

    return render(
        request,
        'user_dashboard/pages/section-nine.html',
        context
    )


@login_required(login_url='/login/')
def classes_type(request):
    ''' Classes type page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

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


@login_required(login_url='/login/')
def classes_type_single_class(request, id):
    ''' Classes type single class page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    tipo_de_aula = get_object_or_404(TiposDeAulas, id=id)

    context = {
        'tipo_de_aula': tipo_de_aula,
    }

    return render(
        request,
        'user_dashboard/pages/classes-type-single-class.html',
        context
    )
