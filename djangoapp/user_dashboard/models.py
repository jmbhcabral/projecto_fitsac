from django.db import models
import os
from utils.image_validators import resize_image
from django.utils import timezone


# Section One
class SectionOne(models.Model):
    class Meta:
        verbose_name = 'Seção 1'
        verbose_name_plural = 'Seção 1'

    name = models.CharField(max_length=100)
    is_visible = models.BooleanField(
        default=False, verbose_name='Visível na página')
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name='Criado em')
    updated_at = models.DateTimeField(
        default=timezone.now, verbose_name='Atualizado em')
    image_1 = models.ImageField(
        upload_to='assets/frontend/images/section_1/top_images/',
        verbose_name='Imagem de Topo',
        blank=True,
        null=True,
    )
    image_2 = models.ImageField(
        upload_to='assets/frontend/images/section_1/top_images/',
        verbose_name='Imagem de Topo 2',
        blank=True,
        null=True,
    )
    text_field_1 = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name='Header 1'
    )
    text_field_2 = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name='Header 2'
    )

    def save(self, *args, **kwargs):

        current_image_name = ''
        if self.image_1:
            current_image_name = str(self.image_1.name)
            super().save(*args, **kwargs)
            image_changed = False

            if self.image_1:
                image_changed = current_image_name != self.image_1

            if image_changed:
                print('resizing')
                resize_image(self.image_1, 1920, True, 80)
                super().save(*args, **kwargs)
        if self.image_2:
            current_image_name = str(self.image_2.name)
            super().save(*args, **kwargs)
            image_changed = False

            if self.image_2:
                image_changed = current_image_name != self.image_2

            if image_changed:
                print('resizing')
                resize_image(self.image_2, 1920, True, 80)
                super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name)


# Section Two
class SectionTwo(models.Model):
    class Meta:
        verbose_name = 'Seção 2'
        verbose_name_plural = 'Seção 2'

    name = models.CharField(max_length=100)
    is_visible = models.BooleanField(
        default=False, verbose_name='Visível na página')
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name='Criado em')
    updated_at = models.DateTimeField(
        default=timezone.now, verbose_name='Atualizado em')
    text_field_3 = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name='Header foto 1'
    )
    text_field_4 = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Paragrafo foto 1'
    )
    image_1 = models.ImageField(
        upload_to='assets/frontend/images/section_2/images/',
        verbose_name='Imagem 1 de Secção 2',
        blank=True,
        null=True,
    )
    text_field_5 = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name='Header da foto 2',
    )
    text_field_6 = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Paragrafo da foto 2'
    )

    image_2 = models.ImageField(
        upload_to='assets/frontend/images/section_2/images/',
        verbose_name='Imagem 2 de Secção 2',
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs):
        current_image_name = ''
        if self.image_1:
            current_image_name = str(self.image_1.name)
            super().save(*args, **kwargs)
            image_changed = False

            if self.image_1:
                image_changed = current_image_name != self.image_1

            if image_changed:
                print('resizing')
                resize_image(self.image_1, 895, True, 80)
                super().save(*args, **kwargs)
        if self.image_2:
            current_image_name = str(self.image_2.name)
            super().save(*args, **kwargs)
            image_changed = False

            if self.image_2:
                image_changed = current_image_name != self.image_2

            if image_changed:
                print('resizing')
                resize_image(self.image_2, 895, True, 80)
                super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name)


# Section Three
class SectionThree(models.Model):
    class Meta:
        verbose_name = 'Seção 3'
        verbose_name_plural = 'Seção 3'

    name = models.CharField(max_length=100)
    is_visible = models.BooleanField(
        default=False, verbose_name='Visível na página')
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name='Criado em')
    updated_at = models.DateTimeField(
        default=timezone.now, verbose_name='Atualizado em')
    section_header = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name='Header da Secção 3'
    )
    image_1 = models.ImageField(
        upload_to='assets/frontend/images/section_3/images/',
        verbose_name='Imagem 1 de Secção 3',
        blank=True,
        null=True,
    )
    text_field_1 = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name='Header da foto 1',
    )
    url_or_path_1 = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='URL ou caminho da foto 1',
    )
    text_field_2 = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Paragrafo da foto 1'
    )
    image_2 = models.ImageField(
        upload_to='assets/frontend/images/section_3/images/',
        verbose_name='Imagem 2 de Secção 3',
        blank=True,
        null=True,
    )
    text_field_3 = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name='Header da foto 2',
    )
    url_or_path_2 = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='URL ou caminho da foto 2',
    )
    text_field_4 = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Paragrafo da foto 2'
    )
    image_3 = models.ImageField(
        upload_to='assets/frontend/images/section_3/images/',
        verbose_name='Imagem 3 de Secção 3',
        blank=True,
        null=True,
    )
    text_field_5 = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name='Header da foto 3',
    )
    url_or_path_3 = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='URL ou caminho da foto 3',
    )
    text_field_6 = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Paragrafo da foto 3'
    )

    def save(self, *args, **kwargs):
        # Obtaining the instance of the model before saving
        old_instance = SectionThree.objects.filter(pk=self.pk).first()

        # Saving the instance to get the image path before resizing
        super().save(*args, **kwargs)

        # List to store the images that need to be resized
        images_to_resize = []

        # Check if image_1 was changed
        if self.image_1 and (not old_instance or old_instance.image_1.name != self.image_1.name):
            images_to_resize.append(self.image_1)

        # Check if image_2 was changed
        if self.image_2 and (not old_instance or old_instance.image_2.name != self.image_2.name):
            images_to_resize.append(self.image_2)

        # Check if image_3 was changed
        if self.image_3 and (not old_instance or old_instance.image_3.name != self.image_3.name):
            images_to_resize.append(self.image_3)

        # Resize the images that need to be resized
        for image in images_to_resize:
            resize_image(image, 362, True, 80)
            # Go back to the beginning of the image file
            image.seek(0)

        # Saving the instance again to save the resized images
        if images_to_resize:
            super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name)


# Section four (Galery)
class SectionFour(models.Model):
    class Meta:
        verbose_name = 'Seção 4 - Galeria'
        verbose_name_plural = 'Seção 4 - Galeria'
    tag = models.CharField(
        max_length=100,
        verbose_name='Tag',
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to='assets/frontend/images/section_4/gallery/',
        verbose_name='Imagem',
        blank=True,
        null=True
    )
    is_visible = models.BooleanField(
        default=False, verbose_name='Visível na página')
    order = models.IntegerField(
        default=0, verbose_name='Ordem')
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name='Criado em')
    updated_at = models.DateTimeField(
        default=timezone.now, verbose_name='Atualizado em')

    def save(self, *args, **kwargs):
        current_image_name = str(self.image)
        super().save(*args, **kwargs)
        image_changed = False

        if self.image:
            image_changed = current_image_name != self.image

        if image_changed:
            print('resizing')
            resize_image(self.image, 700, True, 80)
            super().save(*args, **kwargs)


# Section Five
class PricingOffers(models.Model):
    class Meta:
        verbose_name = 'Seção 5 - Ofertas de preço'
        verbose_name_plural = 'Seção 5 - Ofertas de preço'

    name = models.CharField(
        max_length=35,
        verbose_name='Nome da Oferta',
        blank=True,
        null=True
    )
    is_visible = models.BooleanField(
        default=False, verbose_name='Visível na página')
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name='Criado em')
    updated_at = models.DateTimeField(
        default=timezone.now, verbose_name='Atualizado em')

    def __str__(self):
        return str(self.name)


class PriceCardIcons(models.Model):
    class Meta:
        verbose_name = 'Seção 5 - Icone de preço'
        verbose_name_plural = 'Seção 5 - Icones de preço'

    name = models.CharField(
        max_length=35,
        verbose_name='Nome do Icone',
        blank=True,
        null=True
    )
    icon = models.ImageField(
        upload_to='assets/frontend/images/section_5/pricing_icons/',
        verbose_name='Icone',
        blank=True,
        null=True
    )
    is_visible = models.BooleanField(
        default=False, verbose_name='Visível na página')
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name='Criado em')
    updated_at = models.DateTimeField(
        default=timezone.now, verbose_name='Atualizado em')

    def save(self, *args, **kwargs):
        current_image_name = str(self.icon)
        super().save(*args, **kwargs)
        image_changed = False

        if self.icon:
            image_changed = current_image_name != self.icon

        if image_changed:
            print('resizing')
            resize_image(self.icon, 13)
            super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name)


class OffersIcons(models.Model):
    class Meta:
        verbose_name = 'Seção 5 - Icone de ofertas'
        verbose_name_plural = 'Seção 5 - Icones de ofertas'

    offer = models.ForeignKey(
        PricingOffers,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Oferta',
    )
    icon = models.ForeignKey(
        PriceCardIcons,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Icone',
    )
    is_visible = models.BooleanField(
        default=False, verbose_name='Visível na página')
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name='Criado em')
    updated_at = models.DateTimeField(
        default=timezone.now, verbose_name='Atualizado em')

    def __str__(self):
        return f"{self.icon} - {self.offer}"


class SectionFiveHeader(models.Model):
    class Meta:
        verbose_name = 'Seção 5 - Header'
        verbose_name_plural = 'Seção 5 - Headers'

    name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name='Header 1'
    )
    is_visible = models.BooleanField(
        default=False, verbose_name='Visível na página')
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name='Criado em')
    updated_at = models.DateTimeField(
        default=timezone.now, verbose_name='Atualizado em')

    def __str__(self):
        return str(self.name)


class Card(models.Model):
    class Meta:
        verbose_name = 'Seção 5 - Card'
        verbose_name_plural = 'Seção 5 - Cards'

    name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name='Nome do Card')
    logo = models.ImageField(
        upload_to='assets/frontend/images/section_5/cards/',
        verbose_name='Logo',
        blank=True,
        null=True,
    )
    price = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name='Preço'
    )
    span = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name='Span'
    )
    offers = models.ManyToManyField(
        OffersIcons,
        blank=True,
        verbose_name='Ofertas',
    )
    is_visible = models.BooleanField(
        default=False, verbose_name='Visível na página')

    order = models.IntegerField(
        default=0,
        verbose_name='Ordem',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='Criado em',
        blank=True,
        null=True,
    )
    updated_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='Atualizado em',
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs):
        current_image_name = str(self.logo)
        super().save(*args, **kwargs)
        image_changed = False

        if self.logo:
            image_changed = current_image_name != self.logo

        if image_changed:
            print('resizing')
            resize_image(self.logo, 50)
            super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name)


# Section Six
class SectionSix(models.Model):
    class Meta:
        verbose_name = 'Seção 6'
        verbose_name_plural = 'Seção 6'

    name = models.CharField(max_length=100)
    is_visible = models.BooleanField(
        default=False, verbose_name='Visível na página')
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name='Criado em')
    updated_at = models.DateTimeField(
        default=timezone.now, verbose_name='Atualizado em')
    image = models.ImageField(
        upload_to='assets/frontend/images/section_6/images/',
        verbose_name='Imagem de Secção 6',
        blank=True,
        null=True,
    )
    paragraph_1 = models.CharField(
        max_length=255,
        verbose_name='Paragrafo 1',
        blank=True,
        null=True,
    )
    paragraph_2 = models.CharField(
        max_length=255,
        verbose_name='Paragrafo 2',
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs):
        current_image_name = str(self.image.name)
        super().save(*args, **kwargs)
        image_changed = False

        if self.image:
            image_changed = current_image_name != self.image.name

        if image_changed:
            print('resizing')
            resize_image(self.image, 673, True, 80)
            super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name)

# Section Seven(Blog)


# Section Eight (Video)
class SectionEight(models.Model):
    class Meta:
        verbose_name = 'Seção 8'
        verbose_name_plural = 'Seção 8'

    name = models.CharField(
        max_length=100,
        verbose_name='Nome do video',
        blank=True,
        null=True,
    )

    video_url = models.CharField(
        max_length=255,
        verbose_name='URL do video',
        blank=True,
        null=True,
    )
    is_visible = models.BooleanField(
        default=False,
        verbose_name='Visível na página',
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='Criado em',
    )
    updated_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='Atualizado em',
    )

    def __str__(self):
        return str(self.name)


# Section Nine (Services area)
class SectionNine(models.Model):
    class Meta:
        verbose_name = 'Seção 9'
        verbose_name_plural = 'Seção 9'

    updated_at = models.DateTimeField(
        default=timezone.now, verbose_name='Atualizado em')

    icon = models.ImageField(
        upload_to='assets/frontend/images/section_9/icons/',
        verbose_name='Icone',
        blank=True,
        null=True,
    )
    name = models.CharField(
        max_length=50,
        verbose_name='Nome do serviço',
        blank=True,
        null=True,
    )
    text_field_1 = models.CharField(
        max_length=50,
        verbose_name='campo 1',
        blank=True,
        null=True,
    )
    text_field_2 = models.CharField(
        max_length=50,
        verbose_name='campo 2',
        blank=True,
        null=True,
    )
    is_visible = models.BooleanField(
        default=False,
        verbose_name='Visível na página',
    )
    order = models.IntegerField(
        default=0,
        verbose_name='Ordem',
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='Criado em',
    )

    def save(self, *args, **kwargs):
        current_image_name = str(self.icon)
        super().save(*args, **kwargs)
        image_changed = False

        if self.icon:
            image_changed = current_image_name != self.icon

        if image_changed:
            print('resizing')
            resize_image(self.icon, 78)
            super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name)

# Aulas


class TiposDeAulas(models.Model):
    ''' Model for the Tipos de Aulas section. '''
    class Meta:
        verbose_name = 'Tipo de Aula'
        verbose_name_plural = 'Tipos de Aulas'

    tipo = models.CharField(
        max_length=100,
        help_text='Escreva o tipo de aula.',
        blank=False,
        null=False,
    )
    description = models.TextField(
        help_text='Escreva a Descrição.',
        blank=False,
        null=False,
        max_length=500,
    )
    image = models.ImageField(
        upload_to='assets/frontend/images/tipos_de_aulas',
        help_text='Escolha a Imagem.',
        blank=False,
        null=False,
    )
    order = models.IntegerField(
        default=0,
        verbose_name='Ordem',
        blank=True,
        null=True,
    )
    is_visible = models.BooleanField(
        default=False,
        verbose_name='Visível na página',
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ''' Resize the image before saving. '''
        current_image_name = str(self.image.name)
        super().save(*args, **kwargs)
        image_changed = False

        if self.image:
            image_changed = current_image_name != self.image.name

        if image_changed:
            print('resizing')
            resize_image(self.image, 362, True, 80)
            super().save(*args, **kwargs)

    def __str__(self):
        return str(self.tipo)
