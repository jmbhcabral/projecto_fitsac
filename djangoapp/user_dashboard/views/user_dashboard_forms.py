
from django.contrib import messages
from django.shortcuts import render, reverse, redirect, get_object_or_404
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


def section_one_create(request):

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
            print(f'Form is not valid: {form.errors}')

        return render(request, 'user_dashboard/pages/section-one-create.html',
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


def section_one_update(request, id):
    section_one = get_object_or_404(SectionOne, id=id)

    form_action = reverse(
        'user_dashboard:section_one_update', args=[section_one.id])

    if request.method == 'POST':
        form = SectionOneForm(request.POST, request.FILES,
                              instance=section_one)

        context = {
            'form': form,
            'section_one': section_one,
            'form_action': form_action,
        }
        if form.is_valid():
            form.save()
            messages.success(request, 'Imagem atualizada com sucesso.')
            return redirect('user_dashboard:section_one_update', id=section_one.id)
        else:
            messages.error(request, 'Erro ao atualizar imagem.')
            print(f'Form is not valid: {form.errors}')

        return render(request, 'user_dashboard/pages/section-one-update.html',
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


def section_two_create(request):

    section_two = SectionTwo.objects.all().first()

    form_action = reverse('user_dashboard:section_two_create')

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
            print(f'Form is not valid: {form.errors}')

        return render(request, 'user_dashboard/pages/section-two-create.html',
                      context
                      )
    return render(request, 'user_dashboard/pages/section-two-create.html')


def section_two_update(request, id):
    section_two = get_object_or_404(SectionTwo, id=id)

    form_action = reverse(
        'user_dashboard:section_two_update', args=[section_two.id])

    if request.method == 'POST':
        form = SectionTwoForm(request.POST, request.FILES,
                              instance=section_two)

        context = {
            'form': form,
            'section_two': section_two,
            'form_action': form_action,
        }
        if form.is_valid():
            form.save()
            messages.success(request, 'Secção atualizada com sucesso.')
            return redirect('user_dashboard:section_two_update', id=section_two.id)
        else:
            messages.error(request, 'Erro ao atualizar secção.')
            print(f'Form is not valid: {form.errors}')

        return render(request, 'user_dashboard/pages/section-two-update.html',
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


def section_three_create(request):
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
            print(f'Form is not valid: {form.errors}')

        return render(request, 'user_dashboard/pages/section-three-create.html',
                      context
                      )
    context = {
        'form': SectionThreeForm(),
        'section_three': section_three,
        'form_action': form_action,
    }
    return render(request,
                  'user_dashboard/pages/section-three-create.html',
                  context
                  )


def section_three_update(request, id):
    section_three = get_object_or_404(SectionThree, id=id)
    print(f'Section Three: {section_three}')

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
            return redirect('user_dashboard:section_three_update', id=section_three.id)
        else:
            messages.error(request, 'Erro ao atualizar secção.')
            print(f'Form is not valid: {form.errors}')

        return render(request, 'user_dashboard/pages/section-three-update.html',
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
def section_four_create(request):
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
            print(f'Form is not valid: {form.errors}')

        return render(request, 'user_dashboard/pages/section-four-create.html',
                      context
                      )

    context = {
        'form': SectionFourForm(),
        'section_four': section_four,
        'form_action': form_action,
    }
    return render(request, 'user_dashboard/pages/section-four-create.html', context)


def section_four_single_photo(request, id):
    photo = get_object_or_404(SectionFour, id=id)

    context = {
        'photo': photo,
    }
    return render(
        request,
        'user_dashboard/pages/section-four-single-photo.html',
        context
    )


def section_four_single_photo_update(request, id):
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
            print(f'Form is not valid: {form.errors}')

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


def section_four_single_photo_delete(request, id):
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


def section_four_ordering_photos(request):
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
def section_five_header(request):
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

                return render(request, 'user_dashboard/pages/section-five-header.html', {'formset': formset})

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
            print(f'Formset is not valid: {formset.errors}')
    else:
        formset = SectionFiveHeaderFormSet(
            queryset=SectionFiveHeader.objects.all())

    context = {
        'formset': formset,
        'form_action': reverse('user_dashboard:section_five_header'),
    }

    return render(request, 'user_dashboard/pages/section-five-header.html', context)


def section_five_header_create(request):
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
            print(f'Form is not valid: {form.errors}')

        return render(request,
                      'user_dashboard/pages/section-five-header-create.html',
                      context
                      )
    return render(request,
                  'user_dashboard/pages/section-five-header-create.html')


def section_five_create(request):
    return render(request, 'user_dashboard/pages/section-five-create.html')


def section_five_header_delete(request):

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

    return render(request, 'user_dashboard/pages/section-five-header-delete.html', context)


def section_five_pricing_offers(request):
    pricing_offers = PricingOffers.objects.all()
    count = pricing_offers.count()
    print(f'Pricing Offers: {pricing_offers}')
    print(f'Count: {count}')

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
                print(f'Formset is not valid: {formset.errors}')

        else:
            formset = SectionFivePricingOffers(queryset=pricing_offers)
        context = {
            'formset': formset,
            'form_action': reverse('user_dashboard:section_five_pricing_offers'),
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


def section_five_pricing_offers_create(request):

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
            print(f'Form is not valid: {form.errors}')

        return render(
            request,
            'user_dashboard/pages/section-five-pricing-offers-create.html',
            context
        )
    return render(
        request,
        'user_dashboard/pages/section-five-pricing-offers-create.html')


def section_five_pricing_offers_delete(request):

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
            print(f'Form is not valid: {form.errors}')

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


def section_five_price_card_icons(request):
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
            print(f'Formset is not valid: {formset.errors}')
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


def section_five_price_card_icons_create(request):

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
            print(f'Form is not valid: {form.errors}')

        return render(request, 'user_dashboard/pages/section-five-price-card-icons-create.html',
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


def section_five_price_card_icons_delete(request):
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
            print(f'Form is not valid: {form.errors}')

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


def section_five_offers_icons(request):
    # Pegar todas as instâncias existentes
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
        print('Post request')
        formset = OffersIconsFormSet(
            request.POST, request.FILES, queryset=offers_icons)
        if formset.is_valid():
            print('Formset is valid')
            formset.save()
            messages.success(request, 'Conjunto atualizado com sucesso.')
            return redirect('user_dashboard:section_five_offers_icons')
        else:
            messages.error(request, 'Erro ao atualizar conjunto.')
            print(f'Formset is not valid: {formset.errors}')
    else:
        formset = OffersIconsFormSet(
            queryset=offers_icons)  # Passar o queryset atual

    context = {
        'offers_icons': offers_icons,
        'formset': OffersIconsFormSet(
            queryset=offers_icons),
        'form_action': form_action,
    }

    return render(request, 'user_dashboard/pages/section-five-offers-icons.html', context)


def section_five_offers_icons_create(request):

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
            print(f'Form is not valid: {form.errors}')

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


def section_five_offers_icons_delete(request):
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
            print(f'Form is not valid: {form.errors}')

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


def section_five_card(request):
    cards = Card.objects\
        .prefetch_related('offers')\
        .all()\
        .order_by('order')

    # for card in cards:
    #     for icon_offer in card.offers.all():
    #         offer_name = icon_offer.offer.name
    #         print(f'Offer Name: {offer_name}')
    context = {
        'cards': cards,
    }
    return render(
        request,
        'user_dashboard/pages/section-five-card.html',
        context
    )


def section_five_card_create(request):

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
            print(f'Form is not valid: {form.errors}')

        return render(request, 'user_dashboard/pages/section-five-card-create.html',
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


def section_five_single_card(request, id):
    card = get_object_or_404(Card, id=id)

    context = {
        'card': card,
    }
    return render(
        request,
        'user_dashboard/pages/section-five-single-card.html',
        context
    )


def section_five_ordering_cards(request):

    cards = Card.objects.all()\
        .order_by('order')

    if request.method == 'POST':
        # creates a list of the cards in the order they were received
        updated_cards = []
        for card in cards:
            new_order = request.POST.get(f'card-{card.id}', 0)
            print(f'New Order: {new_order}')
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


def section_five_card_update(request, id):
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
            return redirect('user_dashboard:section_five_single_card', id=card.id)
        else:
            messages.error(request, 'Erro ao atualizar card.')
            print(f'Form is not valid: {form.errors}')

        return render(request, 'user_dashboard/pages/section-five-card-update.html',
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


def section_five_card_delete(request, id):
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


def section_six_create(request):

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
            print(f'Form is not valid: {form.errors}')

        return render(request, 'user_dashboard/pages/section-six-create.html',
                      context
                      )
    context = {
        'form': SectionSixForm(),
        'form_action': form_action,
    }

    return render(
        request,
        'user_dashboard/pages/section-six-create.html',
        context)


def section_six_single_item(request, id):
    item = get_object_or_404(SectionSix, id=id)

    context = {
        'item': item,
    }
    return render(
        request,
        'user_dashboard/pages/section-six-single-item.html',
        context
    )


def section_six_update(request, id):
    section_six = get_object_or_404(SectionSix, id=id)

    form_action = reverse(
        'user_dashboard:section_six_update', args=[section_six.id])

    if request.method == 'POST':
        form = SectionSixForm(request.POST, request.FILES,
                              instance=section_six)

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
            print(f'Form is not valid: {form.errors}')

        return render(request, 'user_dashboard/pages/section-six-update.html',
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


def section_six_delete(request, id):
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


def section_eight_create(request):

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
            print(f'Form is not valid: {form.errors}')

        return render(request, 'user_dashboard/pages/section-eight-create.html',
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


def section_eight_single_video(request, id):
    video = get_object_or_404(SectionEight, id=id)

    context = {
        'video': video,
    }

    return render(
        request,
        'user_dashboard/pages/section-eight-single-video.html',
        context
    )


def section_eight_single_video_update(request, id):
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
            return redirect('user_dashboard:section_eight_single_video', id=video.id)
        else:
            messages.error(request, 'Erro ao atualizar vídeo.')
            print(f'Form is not valid: {form.errors}')

        return render(request, 'user_dashboard/pages/section-eight-single-video-update.html',
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


def section_eight_single_video_delete(request, id):
    video = get_object_or_404(SectionEight, id=id)

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        video.delete()
        messages.success(request, 'Vídeo deletado com sucesso.')
        return redirect('user_dashboard:section_eight')
    else:
        messages.error(request, 'Erro ao deletar vídeo.')

    return render(
        request,
        'user_dashboard/pages/section-eight-single-video.html',
        {'video': video, 'confirmation': 'yes'}
    )

# Section Nine - Services área


def section_nine_create(request):
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


def classes_type_create(request):
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
            print(f'Form is not valid: {form.errors}')

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


def classes_type_update(request, id):
    classes_type = get_object_or_404(TiposDeAulas, id=id)

    print(f'Classes Type: {classes_type}')

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
            print(f'Form is not valid: {form.errors}')

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


def classes_type_delete(request, id):
    tipo_de_aula = get_object_or_404(TiposDeAulas, id=id)

    if request.method == 'POST':
        print("Requisição POST recebida")
        confirmation = request.POST.get('confirmation', 'no')
        print(f'Confirmação recebida: {confirmation}')

        if confirmation == 'yes':
            print("Deletando o tipo de aula")
            tipo_de_aula.delete()
            messages.success(request, 'Tipo de aula deletado com sucesso.')
            return redirect('user_dashboard:classes_type')
        else:
            print("Confirmação não recebida, pedindo confirmação...")
            print(f'Tipo de aula: {tipo_de_aula.id}')
            print(f'Confirmação: {confirmation}')
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


def classes_type_ordering(request):
    classes_type = TiposDeAulas.objects\
        .filter(is_visible=True)\
        .order_by('order')

    form_action = reverse('user_dashboard:classes_type_ordering')

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
    return render(request, 'user_dashboard/pages/classes-type-ordering.html',
                  {'classes_type': classes_type}
                  )
