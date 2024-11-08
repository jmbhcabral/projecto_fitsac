
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404, redirect
from user_dashboard.forms import (
    SectionOneForm, SectionTwoForm,
    SectionThreeForm, SectionFourForm, SectionFiveHeaderForm,
    SectionFiveHeaderDeleteForm, PricingOffersForm, PricingOffersDeleteForm,
    PriceCardIconsForm, PriceCardIconsDeleteForm, OffersIconsForm,
    OffersIconsDeleteForm, CardForm, SectionSixForm, SectionEightForm,
    SectionNineForm, TiposDeAulasForm
)
from user_dashboard.models import (
    SectionOne, SectionTwo,
    SectionThree, SectionFour, SectionFiveHeader, PricingOffers,
    PriceCardIcons, OffersIcons, Card, SectionSix, SectionEight,
    SectionNine, TiposDeAulas
)
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required(login_url='/login/')
def section_one_create(request):
    ''' Section one create page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    section_one = SectionOne.objects.all().first()

    form_action = reverse('user_dashboard:section_one_create')

    if request.method == 'POST':
        form = SectionOneForm(request.POST, request.FILES, )

        context = {
            'form': form,
            'section_one': section_one,
            'form_action': form_action,
        }

        if form.is_valid():
            form.save()
            messages.success(request, 'Imagem adicionada com sucesso.')
            return redirect('user_dashboard:section_one')
        else:
            messages.error(request, 'Erro ao adicionar imagem.')

        return render(
            request,
            'user_dashboard/pages/section-one-create.html',
            context
        )

    context = {
        'form': SectionOneForm(),
        'section_one': section_one,
        'form_action': form_action,
    }

    return render(
        request,
        'user_dashboard/pages/section-one-create.html',
        context
    )


@login_required(login_url='/login/')
def section_one_update(request, id):
    ''' Section one update page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    section_one = get_object_or_404(SectionOne, id=id)

    form_action = reverse(
        'user_dashboard:section_one_update', args=[section_one.id])

    if request.method == 'POST':
        form = SectionOneForm(
            request.POST,
            request.FILES,
            instance=section_one
        )

        context = {
            'form': form,
            'section_one': section_one,
            'form_action': form_action,
        }
        if form.is_valid():
            form.save()
            messages.success(request, 'Imagem atualizada com sucesso.')
            return redirect(
                'user_dashboard:section_one_update',
                id=section_one.id
            )
        else:
            messages.error(request, 'Erro ao atualizar imagem.')

        return render(
            request,
            'user_dashboard/pages/section-one-update.html',
            context
        )

    context = {
        'form': SectionOneForm(instance=section_one),
        'section_one': section_one,
        'form_action': form_action,
    }

    return render(
        request,
        'user_dashboard/pages/section-one-update.html',
        context
    )

# Section Two


@login_required(login_url='/login/')
def section_two_create(request):
    ''' Section two create page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    section_two = SectionTwo.objects.all().first()

    form_action = reverse('user_dashboard:section_two_create')

    form = SectionTwoForm()

    if request.method == 'POST':
        form = SectionTwoForm(request.POST, request.FILES, )

        context = {
            'form': form,
            'section_two': section_two,
            'form_action': form_action,
        }
        if form.is_valid():
            form.save()
            messages.success(request, 'Secção adicionada com sucesso.')
            return redirect('user_dashboard:section_two')
        else:
            messages.error(request, 'Erro ao adicionar secção.')

        return render(
            request,
            'user_dashboard/pages/section-two-create.html',
            context
        )

    context = {
        'form': form,
        'section_two': section_two,
        'form_action': form_action,
    }

    return render(
        request,
        'user_dashboard/pages/section-two-create.html',
        context
    )


@login_required(login_url='/login/')
def section_two_update(request, id):
    ''' Section two update page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    section_two = get_object_or_404(SectionTwo, id=id)

    form_action = reverse(
        'user_dashboard:section_two_update', args=[section_two.id])

    if request.method == 'POST':
        form = SectionTwoForm(
            request.POST,
            request.FILES,
            instance=section_two
        )

        context = {
            'form': form,
            'section_two': section_two,
            'form_action': form_action,
        }
        if form.is_valid():
            form.save()
            messages.success(request, 'Secção atualizada com sucesso.')
            return redirect(
                'user_dashboard:section_two_update',
                id=section_two.id
            )
        else:
            messages.error(request, 'Erro ao atualizar secção.')

        return render(
            request,
            'user_dashboard/pages/section-two-update.html',
            context
        )

    context = {
        'form': SectionTwoForm(instance=section_two),
        'section_two': section_two,
        'form_action': form_action,
    }

    return render(
        request,
        'user_dashboard/pages/section-two-update.html',
        context
    )

# Section Three


@login_required(login_url='/login/')
def section_three_create(request):
    ''' Section three create page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    section_three = SectionThree.objects.all().first()

    form_action = reverse('user_dashboard:section_three_create')

    if request.method == 'POST':
        form = SectionThreeForm(request.POST, request.FILES, )

        context = {
            'form': form,
            'section_three': section_three,
            'form_action': form_action,
        }
        if form.is_valid():
            form.save()
            messages.success(request, 'Secção adicionada com sucesso.')
            return redirect('user_dashboard:section_three')
        else:
            messages.error(request, 'Erro ao adicionar secção.')

        return render(
            request,
            'user_dashboard/pages/section-three-create.html',
            context
        )

    context = {
        'form': SectionThreeForm(),
        'section_three': section_three,
        'form_action': form_action,
    }

    return render(
        request,
        'user_dashboard/pages/section-three-create.html',
        context
    )


@login_required(login_url='/login/')
def section_three_update(request, id):
    ''' Section three update page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    section_three = get_object_or_404(SectionThree, id=id)

    form_action = reverse(
        'user_dashboard:section_three_update', args=[section_three.id])

    if request.method == 'POST':
        form = SectionThreeForm(request.POST, request.FILES,
                                instance=section_three)

        context = {
            'form': form,
            'section_three': section_three,
            'form_action': form_action,
        }

        if form.is_valid():
            form.save()
            messages.success(request, 'Secção atualizada com sucesso.')
            return redirect(
                'user_dashboard:section_three_update',
                id=section_three.id
            )
        else:
            messages.error(request, 'Erro ao atualizar secção.')

        return render(
            request,
            'user_dashboard/pages/section-three-update.html',
            context
        )

    context = {
        'form': SectionThreeForm(instance=section_three),
        'section_three': section_three,
        'form_action': form_action,
    }

    return render(
        request,
        'user_dashboard/pages/section-three-update.html',
        context
    )


# Section Four

@login_required(login_url='/login/')
def section_four_create(request):
    ''' Section four create page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    section_four = SectionFour.objects.all()

    form_action = reverse('user_dashboard:section_four_create')

    if request.method == 'POST':
        form = SectionFourForm(request.POST, request.FILES, )

        context = {
            'form': form,
            'section_four': section_four,
            'form_action': form_action,
        }
        if form.is_valid():
            form.save()
            messages.success(request, 'Imagem adicionada com sucesso.')
            return redirect('user_dashboard:section_four')
        else:
            messages.error(request, 'Erro ao adicionar imagem.')

        return render(
            request,
            'user_dashboard/pages/section-four-create.html',
            context
        )

    context = {
        'form': SectionFourForm(),
        'section_four': section_four,
        'form_action': form_action,
    }

    return render(
        request,
        'user_dashboard/pages/section-four-create.html',
        context
    )


@login_required(login_url='/login/')
def section_four_single_photo(request, id):
    ''' Section four single photo page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    photo = get_object_or_404(SectionFour, id=id)

    context = {
        'photo': photo,
    }

    return render(
        request,
        'user_dashboard/pages/section-four-single-photo.html',
        context
    )


@login_required(login_url='/login/')
def section_four_single_photo_update(request, id):
    ''' Section four single photo update page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    photo = get_object_or_404(SectionFour, id=id)

    form_action = reverse(
        'user_dashboard:section_four_single_photo_update', args=[photo.id])

    if request.method == 'POST':
        form = SectionFourForm(request.POST, request.FILES, instance=photo)

        context = {
            'form': form,
            'photo': photo,
            'form_action': form_action,
        }

        if form.is_valid():
            form.save()
            messages.success(request, 'Imagem atualizada com sucesso.')
            return redirect(
                'user_dashboard:section_four_single_photo',
                id=photo.id
            )
        else:
            messages.error(request, 'Erro ao atualizar imagem.')

        return render(
            request,
            'user_dashboard/pages/section-four-single-photo-update.html',
            context
        )

    context = {
        'form': SectionFourForm(instance=photo),
        'photo': photo,
        'form_action': form_action,
    }

    return render(
        request,
        'user_dashboard/pages/section-four-single-photo-update.html',
        context
    )


@login_required(login_url='/login/')
def section_four_single_photo_delete(request, id):
    ''' Section four single photo delete page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    photo = get_object_or_404(SectionFour, id=id)

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        photo.delete()
        return redirect('user_dashboard:section_four')

    return render(
        request,
        'user_dashboard/pages/section-four-single-photo.html',
        {'photo': photo, 'confirmation': 'yes'}
    )


@login_required(login_url='/login/')
def section_four_ordering_photos(request):
    ''' Section four ordering photos page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    photos = SectionFour.objects.all()\
        .order_by('order')

    if request.method == 'POST':
        # creates a list of the photos in the order they were received
        updated_photos = []
        for photo in photos:
            new_order = request.POST.get(f'photo-{photo.id}', 0)
            if photo.order != new_order:
                photo.order = new_order
                updated_photos.append(photo)

        # updates the photos in the database
        if updated_photos:
            SectionFour.objects.bulk_update(updated_photos, ['order'])
            messages.success(request, 'Ordem das fotos atualizada com sucesso')
            return redirect('user_dashboard:section_four')
        else:
            messages.info(request, 'Nenhuma foto foi reordenada.')

    return render(
        request,
        'user_dashboard/pages/section-four-ordering-photos.html',
        {'photos': photos}
    )


# Section Five
@login_required(login_url='/login/')
def section_five_header(request):
    ''' Section five header page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    SectionFiveHeaderFormSet = modelformset_factory(
        SectionFiveHeader,
        form=SectionFiveHeaderForm,
        extra=0,
        can_delete=False,
    )

    if request.method == 'POST':
        formset = SectionFiveHeaderFormSet(request.POST)
        if formset.is_valid():
            # Garantir que apenas um item esteja visivel
            is_visible_count = sum([form.cleaned_data.get(
                'is_visible', False) for form in formset])
            if is_visible_count > 1:
                messages.error(
                    request, 'Apenas um item pode ser visível por vez')

                return render(
                    request,
                    'user_dashboard/pages/section-five-header.html',
                    {'formset': formset}
                )

            else:
                instances = formset.save(commit=False)
                for instance in instances:
                    if instance.is_visible:
                        # desmarcar todos os outros itens
                        SectionFiveHeader.objects.exclude(
                            id=instance.id).update(is_visible=False)

                        instance.save()
                        messages.success(
                            request, 'Seção atualizada com sucesso')

                return redirect('user_dashboard:section_five_header')

        else:
            messages.error(request, 'Erro ao atualizar seção.')

    else:
        formset = SectionFiveHeaderFormSet(
            queryset=SectionFiveHeader.objects.all())

    context = {
        'formset': formset,
        'form_action': reverse('user_dashboard:section_five_header'),
    }

    return render(
        request,
        'user_dashboard/pages/section-five-header.html',
        context
    )


@login_required(login_url='/login/')
def section_five_header_create(request):
    ''' Section five header create page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    section_five_header = SectionFiveHeader.objects.all()

    form_action = reverse('user_dashboard:section_five_header_create')

    if request.method == 'POST':
        form = SectionFiveHeaderForm(request.POST, request.FILES, )

        context = {
            'form': form,
            'section_five_header': section_five_header,
            'form_action': form_action,
        }

        if form.is_valid():
            form.save()
            messages.success(request, 'Título criado com sucesso.')
            return redirect('user_dashboard:section_five_header_create')
        else:
            messages.error(request, 'Erro ao criar título.')

        return render(
            request,
            'user_dashboard/pages/section-five-header-create.html',
            context
        )

    return render(
        request,
        'user_dashboard/pages/section-five-header-create.html'
    )


@login_required(login_url='/login/')
def section_five_create(request):
    ''' Section five create page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    return render(request, 'user_dashboard/pages/section-five-create.html')


@login_required(login_url='/login/')
def section_five_header_delete(request):
    ''' Section five header delete page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    form_action = reverse('user_dashboard:section_five_header_delete')

    if request.method == 'POST':
        form = SectionFiveHeaderDeleteForm(request.POST)
        if form.is_valid():
            titulos_seleccionados = form.cleaned_data['titulos']
            titulos_seleccionados.delete()
            messages.success(request, 'Título(s) deletado(s) com sucesso.')
            return redirect('user_dashboard:section_five_header')
        else:
            messages.error(request, 'Erro ao deletar títulos.')
            print(f'Form is not valid: {form.errors}')

    else:
        form = SectionFiveHeaderDeleteForm()

    context = {
        'form': form,
        'form_action': form_action,
    }

    return render(
        request,
        'user_dashboard/pages/section-five-header-delete.html',
        context
    )


@login_required(login_url='/login/')
def section_five_pricing_offers(request):
    ''' Section five pricing offers page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    pricing_offers = PricingOffers.objects.all()
    # count = pricing_offers.count()

    if pricing_offers.exists():
        SectionFivePricingOffers = modelformset_factory(
            PricingOffers,
            form=PricingOffersForm,
            extra=0,
            can_delete=False,

        )
        if request.method == 'POST':
            formset = SectionFivePricingOffers(request.POST)
            if formset.is_valid():
                formset.save()
                messages.success(request, 'Ofertas atualizadas com sucesso.')
                return redirect('user_dashboard:section_five_pricing_offers')
            else:
                messages.error(request, 'Erro ao atualizar ofertas.')

        else:
            formset = SectionFivePricingOffers(queryset=pricing_offers)
        context = {
            'formset': formset,
            'form_action': reverse(
                'user_dashboard:section_five_pricing_offers'
            ),
            'pricing_offers': pricing_offers,
        }

        return render(
            request,
            'user_dashboard/pages/section-five-pricing-offers.html',
            context
        )

    context = {
        'pricing_offers': pricing_offers,
    }

    return render(
        request,
        'user_dashboard/pages/section-five-pricing-offers.html',
        context
    )


@login_required(login_url='/login/')
def section_five_pricing_offers_create(request):
    ''' Section five pricing offers create page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    form_action = reverse('user_dashboard:section_five_pricing_offers_create')

    if request.method == 'POST':
        form = PricingOffersForm(request.POST, request.FILES, )

        context = {
            'form': form,
            'form_action': form_action,
        }
        if form.is_valid():
            form.save()
            messages.success(request, 'Oferta  adicionada com sucesso.')
            return redirect('user_dashboard:section_five_pricing_offers')
        else:
            messages.error(request, 'Erro ao adicionar oferta.')

        return render(
            request,
            'user_dashboard/pages/section-five-pricing-offers-create.html',
            context
        )

    return render(
        request,
        'user_dashboard/pages/section-five-pricing-offers-create.html')


@login_required(login_url='/login/')
def section_five_pricing_offers_delete(request):
    ''' Section five pricing offers delete page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    form_action = reverse('user_dashboard:section_five_pricing_offers_delete')

    if request.method == 'POST':
        form = PricingOffersDeleteForm(request.POST)
        if form.is_valid():
            ofertas_seleccionadas = form.cleaned_data['offers']
            ofertas_seleccionadas.delete()
            messages.success(request, 'Oferta(s) deletada(s) com sucesso.')
            return redirect('user_dashboard:section_five_pricing_offers')
        else:
            messages.error(request, 'Erro ao deletar ofertas.')

    else:
        form = PricingOffersDeleteForm()

    context = {
        'form': form,
        'form_action': form_action,
    }

    return render(
        request,
        'user_dashboard/pages/section-five-pricing-offers-delete.html',
        context)


@login_required(login_url='/login/')
def section_five_price_card_icons(request):
    ''' Section five price card icons page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    icons = PriceCardIcons.objects.all()

    form_action = reverse('user_dashboard:section_five_price_card_icons')

    PriceCardIconsFormSet = modelformset_factory(
        PriceCardIcons,
        fields=('name', 'icon', 'is_visible'),
        form=PriceCardIconsForm,
        extra=0,
        can_delete=False,
    )

    if request.method == 'POST':
        formset = PriceCardIconsFormSet(
            request.POST, request.FILES, queryset=icons)
        if formset.is_valid():
            formset.save()
            messages.success(request, 'Icons atualizados com sucesso.')
            return redirect('user_dashboard:section_five_price_card_icons')
        else:
            messages.error(request, 'Erro ao atualizar icons.')

    else:
        formset = PriceCardIconsFormSet(queryset=icons)

    context = {
        'icons': icons,
        'formset': formset,
        'form_action': form_action,
    }

    return render(
        request,
        'user_dashboard/pages/section-five-price-card-icons.html',
        context
    )


@login_required(login_url='/login/')
def section_five_price_card_icons_create(request):
    ''' Section five price card icons create page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    icons = PriceCardIcons.objects.all()
    form_action = reverse(
        'user_dashboard:section_five_price_card_icons_create')

    if request.method == 'POST':
        form = PriceCardIconsForm(request.POST, request.FILES, )

        context = {
            'form': form,
            'icons': icons,
            'form_action': form_action,
        }

        if form.is_valid():
            form.save()
            messages.success(request, 'Icon adicionado com sucesso.')
            return redirect('user_dashboard:section_five_price_card_icons')
        else:
            messages.error(request, 'Erro ao adicionar icon.')

        return render(
            request,
            'user_dashboard/pages/section-five-price-card-icons-create.html',
            context
        )

    context = {
        'form': PriceCardIconsForm(),
        'icons': icons,
        'form_action': form_action,
    }

    return render(
        request,
        'user_dashboard/pages/section-five-price-card-icons-create.html',
        context
    )


@login_required(login_url='/login/')
def section_five_price_card_icons_delete(request):
    ''' Section five price card icons delete page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    form_action = reverse(
        'user_dashboard:section_five_price_card_icons_delete')

    if request.method == 'POST':
        form = PriceCardIconsDeleteForm(request.POST)

        if form.is_valid():
            icons_selected = form.cleaned_data['icons']
            icons_selected.delete()
            messages.success(request, 'Icon(s) deletado(s) com sucesso.')
            return redirect('user_dashboard:section_five_price_card_icons')
        else:
            messages.error(request, 'Erro ao deletar icons.')

    else:
        form = PriceCardIconsDeleteForm()

    context = {
        'form': form,
        'form_action': form_action,
    }

    return render(
        request,
        'user_dashboard/pages/section-five-price-card-icons-delete.html',
        context)


@login_required(login_url='/login/')
def section_five_offers_icons(request):
    ''' Section five offers icons page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    # Get all existing instances
    offers_icons = OffersIcons.objects.all()

    form_action = reverse('user_dashboard:section_five_offers_icons')

    OffersIconsFormSet = modelformset_factory(
        OffersIcons,
        form=OffersIconsForm,
        extra=0,
        can_delete=False,
        fields=('offer', 'icon', 'is_visible'),
    )

    if request.method == 'POST':
        formset = OffersIconsFormSet(
            request.POST, request.FILES, queryset=offers_icons)
        if formset.is_valid():
            formset.save()
            messages.success(request, 'Conjunto atualizado com sucesso.')
            return redirect('user_dashboard:section_five_offers_icons')
        else:
            messages.error(request, 'Erro ao atualizar conjunto.')

    else:
        formset = OffersIconsFormSet(
            queryset=offers_icons)

    context = {
        'offers_icons': offers_icons,
        'formset': OffersIconsFormSet(
            queryset=offers_icons),
        'form_action': form_action,
    }

    return render(
        request,
        'user_dashboard/pages/section-five-offers-icons.html',
        context
    )


@login_required(login_url='/login/')
def section_five_offers_icons_create(request):
    ''' Section five offers icons create page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    offers = PricingOffers.objects.all()
    icons = PriceCardIcons.objects.all()

    form_action = reverse('user_dashboard:section_five_offers_icons_create')

    if request.method == 'POST':
        form = OffersIconsForm(request.POST, request.FILES, )

        context = {
            'form': form,
            'form_action': form_action,
            'offers': offers,
            'icons': icons,
        }

        if form.is_valid():
            form.save()
            messages.success(request, 'Conjunto adicionado com sucesso.')
            return redirect('user_dashboard:section_five_offers_icons')
        else:
            messages.error(request, 'Erro ao adicionar conjunto.')

        return render(
            request,
            'user_dashboard/pages/section-five-offers-icons-create.html',
            context
        )
    form = OffersIconsForm()

    context = {
        'form': form,
        'form_action': form_action,
        'offers': offers,
        'icons': icons,
    }

    return render(
        request,
        'user_dashboard/pages/section-five-offers-icons-create.html',
        context
    )


@login_required(login_url='/login/')
def section_five_offers_icons_delete(request):
    ''' Section five offers icons delete page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    form_action = reverse(
        'user_dashboard:section_five_offers_icons_delete')

    if request.method == 'POST':
        form = OffersIconsDeleteForm(request.POST)

        if form.is_valid():
            icons_selected = form.cleaned_data['offers_icons']
            icons_selected.delete()
            messages.success(request, 'Conjunto(s) deletado(s) com sucesso.')
            return redirect('user_dashboard:section_five_offers_icons')
        else:
            messages.error(request, 'Erro ao deletar conjunto.')

    else:
        form = OffersIconsDeleteForm()

    context = {
        'form': form,
        'form_action': form_action,
    }

    return render(
        request,
        'user_dashboard/pages/section-five-offers-icons-delete.html',
        context)


@login_required(login_url='/login/')
def section_five_card(request):
    ''' Section five card page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    cards = Card.objects\
        .prefetch_related('offers')\
        .all()\
        .order_by('order')

    context = {
        'cards': cards,
    }

    return render(
        request,
        'user_dashboard/pages/section-five-card.html',
        context
    )


@login_required(login_url='/login/')
def section_five_card_create(request):
    ''' Section five card create page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    form_action = reverse('user_dashboard:section_five_card_create')

    if request.method == 'POST':

        form = CardForm(request.POST, request.FILES, )

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            form.save()
            messages.success(request, 'Card adicionado com sucesso.')
            return redirect('user_dashboard:section_five_card')
        else:
            messages.error(request, 'Erro ao adicionar card.')

        return render(
            request,
            'user_dashboard/pages/section-five-card-create.html',
            context
        )

    context = {
        'form': CardForm(),
        'form_action': form_action,
    }

    return render(
        request,
        'user_dashboard/pages/section-five-card-create.html',
        context
    )


@login_required(login_url='/login/')
def section_five_single_card(request, id):
    ''' Section five single card page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    card = get_object_or_404(Card, id=id)

    context = {
        'card': card,
    }

    return render(
        request,
        'user_dashboard/pages/section-five-single-card.html',
        context
    )


@login_required(login_url='/login/')
def section_five_ordering_cards(request):
    ''' Section five ordering cards page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    cards = Card.objects.all()\
        .order_by('order')

    if request.method == 'POST':
        # creates a list of the cards in the order they were received
        updated_cards = []
        for card in cards:
            new_order = request.POST.get(f'card-{card.id}', 0)
            if card.order != new_order:
                card.order = new_order
                updated_cards.append(card)

        # updates the cards in the database
        if updated_cards:
            Card.objects.bulk_update(updated_cards, ['order'])
            messages.success(request, 'Ordem dos cards atualizada com sucesso')
            return redirect('user_dashboard:section_five_card')
        else:
            messages.info(request, 'Nenhum card foi reordenado.')

    return render(
        request,
        'user_dashboard/pages/section-five-ordering-cards.html',
        {'cards': cards}
    )


@login_required(login_url='/login/')
def section_five_card_update(request, id):
    ''' Section five card update page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    card = get_object_or_404(Card, id=id)

    form_action = reverse(
        'user_dashboard:section_five_card_update', args=[card.id])

    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES,
                        instance=card)

        context = {
            'form': form,
            'card': card,
            'form_action': form_action,
        }
        if form.is_valid():
            form.save()
            messages.success(request, 'Card atualizado com sucesso.')
            return redirect(
                'user_dashboard:section_five_single_card', id=card.id
            )
        else:
            messages.error(request, 'Erro ao atualizar card.')

        return render(
            request,
            'user_dashboard/pages/section-five-card-update.html',
            context
        )

    context = {
        'form': CardForm(instance=card),
        'card': card,
        'form_action': form_action,
    }
    return render(
        request,
        'user_dashboard/pages/section-five-card-update.html',
        context
    )


@login_required(login_url='/login/')
def section_five_card_delete(request, id):
    ''' Section five card delete page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    card = get_object_or_404(Card, id=id)

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':

        card.delete()
        messages.success(request, 'Card deletado com sucesso.')
        return redirect('user_dashboard:section_five_card')

    return render(
        request,
        'user_dashboard/pages/section-five-single-card.html',
        {'card': card, 'confirmation': 'yes'}
    )


@login_required(login_url='/login/')
def section_six_create(request):
    ''' Section six create page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    form_action = reverse('user_dashboard:section_six_create')

    if request.method == 'POST':
        form = SectionSixForm(
            request.POST,
            request.FILES,
        )

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():

            form.save()
            messages.success(request, 'Secção adicionada com sucesso.')
            return redirect('user_dashboard:section_six')
        else:
            messages.error(request, 'Erro ao adicionar secção.')

        return render(
            request,
            'user_dashboard/pages/section-six-create.html',
            context
        )

    context = {
        'form': SectionSixForm(),
        'form_action': form_action,
    }

    return render(
        request,
        'user_dashboard/pages/section-six-create.html',
        context
    )


@login_required(login_url='/login/')
def section_six_single_item(request, id):
    ''' Section six single item page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    item = get_object_or_404(SectionSix, id=id)

    context = {
        'item': item,
    }

    return render(
        request,
        'user_dashboard/pages/section-six-single-item.html',
        context
    )


@login_required(login_url='/login/')
def section_six_update(request, id):
    ''' Section six update page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    section_six = get_object_or_404(SectionSix, id=id)

    form_action = reverse(
        'user_dashboard:section_six_update', args=[section_six.id])

    if request.method == 'POST':
        form = SectionSixForm(
            request.POST,
            request.FILES,
            instance=section_six
        )

        context = {
            'form': form,
            'section_six': section_six,
            'form_action': form_action,
        }
        if form.is_valid():
            form.save()
            messages.success(request, 'Secção atualizada com sucesso.')
            return redirect('user_dashboard:section_six')
        else:
            messages.error(request, 'Erro ao atualizar secção.')

        return render(
            request,
            'user_dashboard/pages/section-six-update.html',
            context
        )

    context = {
        'form': SectionSixForm(instance=section_six),
        'section_six': section_six,
        'form_action': form_action,
    }

    return render(
        request,
        'user_dashboard/pages/section-six-update.html',
        context
    )


@login_required(login_url='/login/')
def section_six_delete(request, id):
    ''' Section six delete page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    item = get_object_or_404(SectionSix, id=id)

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        item.delete()
        messages.success(request, 'Item deletado com sucesso.')
        return redirect('user_dashboard:section_six')
    else:
        messages.error(request, 'Erro ao deletar item.')

    return render(
        request,
        'user_dashboard/pages/section-six-single-item.html',
        {'item': item, 'confirmation': 'yes'}
    )

# Section Seven - Blog

# Section Eight - video


@login_required(login_url='/login/')
def section_eight_create(request):
    ''' Section eight create page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    form_action = reverse('user_dashboard:section_eight_create')

    if request.method == 'POST':
        form = SectionEightForm(
            request.POST,
            request.FILES,
        )

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            form.save()
            messages.success(request, 'Vídeo adicionado com sucesso.')
            return redirect('user_dashboard:section_eight')
        else:
            messages.error(request, 'Erro ao adicionar vídeo.')

        return render(
            request,
            'user_dashboard/pages/section-eight-create.html',
            context
        )

    context = {
        'form': SectionEightForm(),
        'form_action': form_action,
    }

    return render(
        request,
        'user_dashboard/pages/section-eight-create.html',
        context
    )


@login_required(login_url='/login/')
def section_eight_single_video(request, id):
    ''' Section eight single video page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    video = get_object_or_404(SectionEight, id=id)

    context = {
        'video': video,
    }

    return render(
        request,
        'user_dashboard/pages/section-eight-single-video.html',
        context
    )


@login_required(login_url='/login/')
def section_eight_single_video_update(request, id):
    ''' Section eight single video update page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    video = get_object_or_404(SectionEight, id=id)

    form_action = reverse(
        'user_dashboard:section_eight_single_video_update', args=[video.id])

    if request.method == 'POST':
        form = SectionEightForm(request.POST, request.FILES,
                                instance=video)

        context = {
            'form': form,
            'video': video,
            'form_action': form_action,
        }
        if form.is_valid():
            form.save()
            messages.success(request, 'Vídeo atualizado com sucesso.')
            return redirect(
                'user_dashboard:section_eight_single_video', id=video.id
            )
        else:
            messages.error(request, 'Erro ao atualizar vídeo.')
            print(f'Form is not valid: {form.errors}')

        return render(
            request,
            'user_dashboard/pages/section-eight-single-video-update.html',
            context
        )

    context = {
        'form': SectionEightForm(instance=video),
        'video': video,
        'form_action': form_action,
    }

    return render(
        request,
        'user_dashboard/pages/section-eight-single-video-update.html',
        context
    )


@login_required(login_url='/login/')
def section_eight_single_video_delete(request, id):
    ''' Section eight single video delete page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    video = get_object_or_404(SectionEight, id=id)

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        video.delete()
        messages.success(request, 'Vídeo deletado com sucesso.')
        return redirect('user_dashboard:section_eight')
    elif confirmation == 'no':
        messages.warning(request, 'Quer deletar o vídeo?')
    else:
        messages.error(request, 'Erro ao deletar vídeo.')

    return render(
        request,
        'user_dashboard/pages/section-eight-single-video.html',
        {'video': video, 'confirmation': 'yes'}
    )

# Section Nine - Services área


@login_required(login_url='/login/')
def section_nine_create(request):
    ''' Section nine create page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    form_action = reverse('user_dashboard:section_nine_create')

    if request.method == 'POST':
        form = SectionNineForm(
            request.POST,
            request.FILES,
        )

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            form.save()
            messages.success(request, 'Serviço adicionado com sucesso.')
            return redirect('user_dashboard:section_nine')
        else:
            messages.error(request, 'Erro ao adicionar serviço.')
            print(f'Form is not valid: {form.errors}')

        return render(
            request,
            'user_dashboard/pages/section-nine-create.html',
            context
        )

    context = {
        'form': SectionNineForm(),
        'form_action': form_action,
    }

    return render(
        request,
        'user_dashboard/pages/section-nine-create.html',
        context)


@login_required(login_url='/login/')
def section_nine_update(request, id):
    ''' Section nine update page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    service = get_object_or_404(SectionNine, id=id)

    form_action = reverse(
        'user_dashboard:section_nine_update', args=[service.id])

    if request.method == 'POST':
        form = SectionNineForm(request.POST, request.FILES, instance=service)

        context = {
            'form': form,
            'service': service,
            'form_action': form_action,
        }

        if form.is_valid():
            form.save()
            messages.success(request, 'Serviço atualizado com sucesso.')
            return redirect('user_dashboard:section_nine')
        else:
            messages.error(request, 'Erro ao atualizar serviço.')

        return render(
            request,
            'user_dashboard/pages/section-nine-update.html',
            context
        )

    context = {
        'form': SectionNineForm(instance=service),
        'service': service,
        'form_action': form_action,
    }

    return render(
        request,
        'user_dashboard/pages/section-nine-update.html',
        context)


@login_required(login_url='/login/')
def classes_type_create(request):
    ''' Classes type create page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    form_action = reverse('user_dashboard:classes_type_create')

    if request.method == 'POST':
        form = TiposDeAulasForm(
            request.POST,
            request.FILES,
        )

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            form.save()
            messages.success(request, 'Tipo de aula adicionado com sucesso.')
            return redirect('user_dashboard:classes_type')
        else:
            messages.error(request, 'Erro ao adicionar tipo de aula.')

        return render(
            request,
            'user_dashboard/pages/classes-type-create.html',
            context
        )

    context = {
        'form': TiposDeAulasForm(),
        'form_action': form_action,
    }

    return render(
        request,
        'user_dashboard/pages/classes-type-create.html',
        context)


@login_required(login_url='/login/')
def classes_type_update(request, id):
    ''' Classes type update page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    classes_type = get_object_or_404(TiposDeAulas, id=id)

    form_action = reverse(
        'user_dashboard:classe_type_update',
        args=[classes_type.id])

    if request.method == 'POST':
        form = TiposDeAulasForm(
            request.POST,
            request.FILES,
            instance=classes_type
        )

        context = {
            'form': form,
            'form_action': form_action,
            'classes_type': classes_type,
        }

        if form.is_valid():
            form.save()
            messages.success(request, 'Tipo de aula atualizado com sucesso.')
            return redirect('user_dashboard:classes_type')
        else:
            messages.error(request, 'Erro ao atualizar tipo de aula.')

        return render(
            request,
            'user_dashboard/pages/classes-type-update.html',
            context
        )

    context = {
        'form': TiposDeAulasForm(instance=classes_type),
        'form_action': form_action,
        'classes_type': classes_type,
    }

    return render(
        request,
        'user_dashboard/pages/classes-type-update.html',
        context
    )


@login_required(login_url='/login/')
def classes_type_delete(request, id):
    ''' Classes type delete page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    tipo_de_aula = get_object_or_404(TiposDeAulas, id=id)

    if request.method == 'POST':
        confirmation = request.POST.get('confirmation', 'no')

        if confirmation == 'yes':
            tipo_de_aula.delete()
            messages.success(request, 'Tipo de aula deletado com sucesso.')
            return redirect('user_dashboard:classes_type')
        else:
            return render(
                request,
                'user_dashboard/pages/classes-type-single-class.html',
                {'tipo_de_aula': tipo_de_aula, 'confirmation': 'yes'}
            )

    return render(
        request,
        'user_dashboard/pages/classes-type-single-class.html',
        {'tipo_de_aula': tipo_de_aula}
    )


@login_required(login_url='/login/')
def classes_type_ordering(request):
    ''' Classes type ordering page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    classes_type = TiposDeAulas.objects\
        .filter(is_visible=True)\
        .order_by('order')

    # form_action = reverse('user_dashboard:classes_type_ordering')

    if request.method == 'POST':
        # creates a list of the classes in the order they were received
        updated_classes = []
        for classes in classes_type:
            new_order = request.POST.get(f'classes-{classes.id}', 0)
            if classes.order != new_order:
                classes.order = new_order
                updated_classes.append(classes)

        # updates the classes in the database
        if updated_classes:
            TiposDeAulas.objects.bulk_update(updated_classes, ['order'])
            messages.success(request, 'Ordem das aulas atualizada com sucesso')
            return redirect('user_dashboard:classes_type')
        else:
            messages.info(request, 'Nenhuma aula foi reordenada.')
    return render(
        request,
        'user_dashboard/pages/classes-type-ordering.html',
        {'classes_type': classes_type}
    )
