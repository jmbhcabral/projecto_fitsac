from django import forms
from .models import (
    SectionOne, SectionTwo, SectionThree, SectionFour, PricingOffers,
    PriceCardIcons, OffersIcons, SectionFiveHeader, Card, SectionSix,
    SectionEight, SectionNine, TiposDeAulas
)

from django.core.exceptions import ValidationError


# Section One
class SectionOneForm(forms.ModelForm):
    class Meta:
        model = SectionOne
        fields = (
            'name', 'image_1', 'image_2', 'text_field_1',
            'text_field_2', 'is_visible'
        )

    name = forms.CharField(
        max_length=100,
        label='Nome',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite o nome da seção',
            }
        )
    )
    image_1 = forms.ImageField(
        label='Imagem 1',
        widget=forms.FileInput(
            attrs={
                'placeholder': 'Escolha uma imagem',
                'accept': 'image/*',
            }
        ),
        help_text='A imagem deve ter 1920x900 pixels.',
        required=False,
    )
    image_2 = forms.ImageField(
        label='Imagem 2',
        widget=forms.FileInput(
            attrs={
                'placeholder': 'Escolha uma imagem',
                'accept': 'image/*',
            }
        ),
        help_text='A imagem deve ter 1920x400 pixels.',
        required=False,
    )
    text_field_1 = forms.CharField(
        max_length=30,
        label='1ª Linha do cabeçalho',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite o texto da 1ª linha',
            }
        ),
        required=False,
    )
    text_field_2 = forms.CharField(
        max_length=30,
        label='2ª Linha do cabeçalho',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite o texto da 2ª linha',
            }
        ),
        required=False,
    )

    def clean(self):
        data = self.cleaned_data
        if not data.get('name'):
            self.add_error(
                'name',
                ValidationError(
                    'O campo nome é obrigatório.'
                )
            )

        return super().clean()


# Section Two
class SectionTwoForm(forms.ModelForm):
    class Meta:
        model = SectionTwo
        fields = ('name', 'text_field_3', 'text_field_4', 'image_1',
                  'text_field_5', 'text_field_6', 'image_2', 'is_visible')

    name = forms.CharField(
        max_length=100,
        label='Nome',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite o nome da seção',
            }
        )
    )
    text_field_3 = forms.CharField(
        max_length=30,
        label='Cabeçalho 1',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite o texto do cabeçalho 1',
            }
        ),
        required=False,
    )
    text_field_4 = forms.CharField(
        max_length=255,
        label='Paragrafo 1',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite o texto do paragrafo 1',
            }
        ),
        required=False,
    )
    image_1 = forms.ImageField(
        label='Imagem 1',
        widget=forms.FileInput(
            attrs={
                'placeholder': 'Escolha uma imagem',
            }
        ),
        help_text='A imagem deve ter 895x560 pixels.',
        required=False,
    )
    text_field_5 = forms.CharField(
        max_length=30,
        label='cabeçalho 2',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite o texto do cabeçalho 2',
            }
        ),
        required=False,
    )
    text_field_6 = forms.CharField(
        max_length=255,
        label='Paragrafo 2',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite o texto do paragrafo 2',
            }
        ),
        required=False,
    )
    image_2 = forms.ImageField(
        label='Imagem 2',
        widget=forms.FileInput(
            attrs={
                'placeholder': 'Escolha uma imagem',
            }
        ),
        help_text='A imagem deve ter 895x560 pixels.',
        required=False,
    )

    def clean(self):
        data = self.cleaned_data
        if not data.get('name'):
            self.add_error(
                'name',
                ValidationError(
                    'O campo nome é obrigatório.'
                )
            )

        return super().clean()


# Section Three
class SectionThreeForm(forms.ModelForm):
    class Meta:
        model = SectionThree
        fields = ('name',
                  'image_1', 'text_field_1', 'url_or_path_1', 'text_field_2',
                  'image_2', 'text_field_3', 'url_or_path_2', 'text_field_4',
                  'image_3', 'text_field_5', 'url_or_path_3', 'text_field_6',
                  'is_visible')
    name = forms.CharField(
        max_length=100,
        label='Nome',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite o nome da seção',
            }
        )
    )
    image_1 = forms.ImageField(
        label='Imagem 1',
        widget=forms.FileInput(
            attrs={
                'placeholder': 'Escolha uma imagem',
            }
        ),
        help_text='A imagem deve ter 362x300 pixels.',
        required=False,
    )
    text_field_1 = forms.CharField(
        max_length=30,
        label='Cabeçalho 1',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite o texto do cabeçalho 1',
            }
        ),
        required=False,
    )
    url_or_path_1 = forms.CharField(
        max_length=255,
        label='URL ou caminho 1',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite o url ou caminho para o link 1',
            }
        ),
        required=False,
    )
    text_field_2 = forms.CharField(
        max_length=255,
        label='Paragrafo 1',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite o texto do paragrafo 1',
            }
        ),
        required=False,
    )
    image_2 = forms.ImageField(
        label='Imagem 2',
        widget=forms.FileInput(
            attrs={
                'placeholder': 'Escolha uma imagem',
            }
        ),
        help_text='A imagem deve ter 362x300 pixels.',
        required=False,
    )
    text_field_3 = forms.CharField(
        max_length=30,
        label='Cabeçalho 2',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite o texto do cabeçalho 2',
            }
        ),
        required=False,
    )
    url_or_path_2 = forms.CharField(
        max_length=255,
        label='URL ou caminho 2',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite o url ou caminho para o link 2',
            }
        ),
        required=False,
    )
    text_field_4 = forms.CharField(
        max_length=255,
        label='Paragrafo 2',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite o texto do paragrafo 2',
            }
        ),
        required=False,
    )
    image_3 = forms.ImageField(
        label='Imagem 3',
        widget=forms.FileInput(
            attrs={
                'placeholder': 'Escolha uma imagem',
            }
        ),
        help_text='A imagem deve ter 362x300 pixels.',
        required=False,
    )
    text_field_5 = forms.CharField(
        max_length=30,
        label='Cabeçalho 3',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite o texto do cabeçalho 3',
            }
        ),
        required=False,
    )
    url_or_path_3 = forms.CharField(
        max_length=255,
        label='URL ou caminho 3',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite o url ou caminho para o link 3',
            }
        ),
        required=False,
    )
    text_field_6 = forms.CharField(
        max_length=255,
        label='Paragrafo 3',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite o texto do paragrafo 3',
            }
        ),
        required=False,
    )

    def clean(self):
        data = self.cleaned_data
        if not data.get('name'):
            self.add_error(
                'name',
                ValidationError(
                    'O campo nome é obrigatório.'
                )
            )

        return super().clean()


# Section Four - Gallery
class SectionFourForm(forms.ModelForm):
    class Meta:
        model = SectionFour
        fields = ('tag', 'image', 'order', 'is_visible')

    tag = forms.CharField(
        max_length=100,
        label='Tag',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite a tag da imagem',
            }
        )
    )

    image = forms.ImageField(
        label='Imagem',
        widget=forms.FileInput(
            attrs={
                'placeholder': 'Escolha uma imagem',
            }
        ),
        help_text='A imagem deve ter 700x500 pixels.',
        required=False,
    )
    order = forms.IntegerField(
        label='Ordem',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Digite a ordem da imagem',
            }),
        required=False,
    )
    is_visible = forms.BooleanField(
        label='Visível',
        widget=forms.CheckboxInput(
            attrs={
                'placeholder': 'Visível',
            }),
        required=False,
    )


# Section Five - pricing cards
class PricingOffersForm(forms.ModelForm):
    class Meta:
        model = PricingOffers
        fields = ('name', 'is_visible')

    name = forms.CharField(
        max_length=100,
        label='Nome',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite o nome da oferta',
            }
        )
    )

    is_visible = forms.BooleanField(
        label='Visível',
        widget=forms.CheckboxInput(
            attrs={
                'placeholder': 'Visível',
            }),
        required=False,
    )


class PricingOffersDeleteForm(forms.Form):
    offers = forms.ModelMultipleChoiceField(
        queryset=PricingOffers.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Ofertas',
    )


class PriceCardIconsForm(forms.ModelForm):
    class Meta:
        model = PriceCardIcons
        fields = ('name', 'icon', 'is_visible')

    name = forms.CharField(
        max_length=100,
        label='Nome',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite o nome do ícone',
            }
        )
    )
    icon = forms.ImageField(
        label='Ícone',
        widget=forms.FileInput(
            attrs={
                'placeholder': 'Escolha um ícone',
            }
        ),
        help_text='O ícone deve ter 13x13 pixels.',
        required=False,
    )
    is_visible = forms.BooleanField(
        label='Visível',
        widget=forms.CheckboxInput(
            attrs={
                'placeholder': 'Visível',
            }),
        required=False,
    )


class PriceCardIconsDeleteForm(forms.Form):
    icons = forms.ModelMultipleChoiceField(
        queryset=PriceCardIcons.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Ícones',
    )


class OffersIconsForm(forms.ModelForm):
    class Meta:
        model = OffersIcons
        fields = ('icon', 'offer', 'is_visible')

    offer = forms.ModelChoiceField(
        queryset=PricingOffers.objects.all(),
        label='Oferta',
        widget=forms.Select(
            attrs={
                'placeholder': 'Escolha uma oferta',
            }
        ),
        required=False,
    )

    icon = forms.ModelChoiceField(
        queryset=PriceCardIcons.objects.all(),
        label='Ícone',
        widget=forms.Select(
            attrs={
                'placeholder': 'Escolha um ícone',
            }
        ),
        required=False,
    )
    is_visible = forms.BooleanField(
        label='Visível',
        widget=forms.CheckboxInput(
            attrs={
                'placeholder': 'Visível',
            }),
        required=False,
    )


class OffersIconsDeleteForm(forms.Form):
    # offers_icons é o nome do campo no form
    offers_icons = forms.ModelMultipleChoiceField(
        queryset=OffersIcons.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Ofertas e ícones',
    )


class SectionFiveHeaderForm(forms.ModelForm):
    class Meta:
        model = SectionFiveHeader
        fields = ('name', 'is_visible')

    name = forms.CharField(
        max_length=30,
        label='Cabeçalho',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite o texto do cabeçalho',
            }
        ),
        required=True,
    )
    is_visible = forms.BooleanField(
        label='Visível',
        widget=forms.CheckboxInput(
            attrs={
                'placeholder': 'Visível',
            }),
        required=False,
    )


class SectionFiveHeaderDeleteForm(forms.Form):
    titulos = forms.ModelMultipleChoiceField(
        queryset=SectionFiveHeader.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Títulos',
    )


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ('name', 'logo', 'price', 'span',
                  'offers', 'is_visible', 'order')

    name = forms.CharField(
        max_length=30,
        label='Nome',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite o nome do card',
            }
        )
    )
    logo = forms.ImageField(
        label='Logo',
        widget=forms.FileInput(
            attrs={
                'placeholder': 'Escolha uma imagem',
            }
        ),
        help_text='A imagem deve ter 50x50 pixels.',
        required=False,
    )
    price = forms.DecimalField(
        max_digits=10,
        label='Preço',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Digite o preço',
            }),
        required=False,
    )
    span = forms.CharField(
        max_length=30,
        label='Span',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite o span',
            }
        ),
        required=False,
    )
    offers = forms.ModelMultipleChoiceField(
        queryset=OffersIcons.objects.all(),
        label='Ofertas',
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    is_visible = forms.BooleanField(
        label='Visível',
        widget=forms.CheckboxInput(
            attrs={
                'placeholder': 'Visível',
            }),
        required=False,
    )
    order = forms.IntegerField(
        label='Ordem',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Digite a ordem',
            }),
        required=False,
    )

# Section Six


class SectionSixForm(forms.ModelForm):
    class Meta:
        model = SectionSix
        fields = ('name', 'image', 'paragraph_1', 'paragraph_2', 'is_visible')

    name = forms.CharField(
        max_length=100,
        label='Nome',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite o nome da secção',
            }
        )
    )
    image = forms.ImageField(
        label='Imagem',
        widget=forms.FileInput(
            attrs={
                'placeholder': 'Escolha uma imagem',
            }
        ),
        help_text='A imagem deve ter 925x673 pixels.',
        required=False,
    )
    paragraph_1 = forms.CharField(
        max_length=255,
        widget=forms.Textarea(
            attrs={
                'maxlength': 255,
                'placeholder': 'Digite o texto do parágrafo 1',
                'rows': 5,
            }),
    )
    paragraph_2 = forms.CharField(
        max_length=255,
        widget=forms.Textarea(
            attrs={
                'maxlength': 255,
                'placeholder': 'Digite o texto do parágrafo 2',
                'rows': 5,
            }),
        required=False,
    )
    is_visible = forms.BooleanField(
        label='Visível',
        widget=forms.CheckboxInput(
            attrs={
                'placeholder': 'Visível',
            }),
        required=False,
    )

    def clean(self):
        data = self.cleaned_data
        if not data.get('name'):
            self.add_error(
                'name',
                ValidationError(
                    'O campo nome é obrigatório.'
                )
            )

        return super().clean()

# Section Seven - Blog

# Section Eight - video


class SectionEightForm(forms.ModelForm):
    class Meta:
        model = SectionEight
        fields = ('name', 'video_url', 'is_visible')

    name = forms.CharField(
        max_length=100,
        label='Nome',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite o nome do vídeo',
            }
        )
    )
    video_url = forms.CharField(
        max_length=255,
        label='URL do vídeo',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite a URL do vídeo',
            }
        )
    )
    is_visible = forms.BooleanField(
        label='Visível',
        widget=forms.CheckboxInput(
            attrs={
                'placeholder': 'Visível',
            }),
        required=False,
    )

    def clean(self):
        data = self.cleaned_data
        if not data.get('name'):
            self.add_error(
                'name',
                ValidationError(
                    'O campo nome é obrigatório.'
                )
            )

        return super().clean()
# Section Nine - Services area


class SectionNineForm(forms.ModelForm):
    class Meta:
        model = SectionNine
        fields = ('name', 'icon', 'text_field_1',
                  'text_field_2', 'order', 'is_visible')

    name = forms.CharField(
        max_length=100,
        label='Nome',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite o nome da seção',
            }
        )
    )
    icon = forms.ImageField(
        label='Ícone',
        widget=forms.FileInput(
            attrs={
                'placeholder': 'Escolha um ícone',
            }
        ),
        help_text='O ícone deve ter 50x50 pixels.',
        required=False,
    )
    text_field_1 = forms.CharField(
        max_length=30,
        label='Parágrafo 1',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite o texto do parágrafo 1',
            }
        ),
        required=False,
    )
    text_field_2 = forms.CharField(
        max_length=255,
        label='Parágrafo 2',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite o texto do parágrafo 2',
            }
        ),
        required=False,
    )

    order = forms.IntegerField(
        label='Ordem',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Digite a ordem da seção',
            }),
        required=False,
    )

    is_visible = forms.BooleanField(
        label='Visível',
        widget=forms.CheckboxInput(
            attrs={
                'placeholder': 'Visível',
            }),
        required=False,
    )

    def clean(self):
        data = self.cleaned_data
        if not data.get('name'):
            self.add_error(
                'name',
                ValidationError(
                    'O campo nome é obrigatório.'
                )
            )

        return super().clean()

# Aulas


class TiposDeAulasForm(forms.ModelForm):
    ''' Form for the TiposDeAulas model. '''
    class Meta:
        model = TiposDeAulas
        fields = ['tipo', 'description', 'image', 'order', 'is_visible']
        labels = {
            'tipo': 'Tipo',
            'description': 'Descrição',
            'image': 'Imagem',
            'order': 'Ordem',
            'is_visible': 'Visível',
        }
        widgets = {
            'tipo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digita o tipo',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digita a descrição',
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'order': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digita a ordem',
                }
            ),
            'is_visible': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'placeholder': 'Visível',
                }
            ),
        }

    def clean_tipo(self):
        tipo = self.cleaned_data['tipo']

        if not tipo:
            raise ValidationError('O campo tipo é obrigatório.')

        if len(tipo) < 3:
            raise ValidationError('O tipo deve ter no mínimo 3 caracteres.')

        return tipo

    def clean_description(self):
        description = self.cleaned_data['description']

        if not description:
            raise ValidationError('O campo descrição é obrigatório.')

        if len(description) < 10:
            raise ValidationError(
                'A descrição deve ter no mínimo 10 caracteres.')

        return description

    def clean_image(self):
        image = self.cleaned_data['image']

        if not image:
            raise ValidationError('O campo imagem é obrigatório.')

        return image

    def clean(self):
        cleaned_data = super().clean()

        return cleaned_data
