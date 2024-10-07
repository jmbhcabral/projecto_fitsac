from django.db import models
from utils.image_validators import validate_png, resize_image


class MenuLink(models.Model):
    class Meta:
        verbose_name = 'Menu Link'
        verbose_name_plural = 'Menu Links'

    text = models.CharField(max_length=50)
    url_or_path = models.CharField(max_length=2048)
    new_tab = models.BooleanField(default=False)
    site_setup = models.ForeignKey(
        'SiteSetup', on_delete=models.CASCADE,
        blank=True, null=True, default=None,
    )

    def __str__(self):
        return str(self.text)


class SiteSetup(models.Model):
    class Meta:
        verbose_name = 'Setup'
        verbose_name_plural = 'Setup'

    show_header = models.BooleanField(default=True)
    show_training_categories = models.BooleanField(default=True)
    show_services = models.BooleanField(default=True)
    show_gallery = models.BooleanField(default=True)
    show_pricing = models.BooleanField(default=True)
    show_about_us = models.BooleanField(default=True)
    show_blog = models.BooleanField(default=True)
    show_video = models.BooleanField(default=True)
    show_services_area = models.BooleanField(default=True)
    show_footer = models.BooleanField(default=True)  
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=255)
    head_title = models.CharField(
        max_length=65,
        blank=True,
        default='Teste',)

    favicon = models.ImageField(
        upload_to='assets/favicon/%Y/%m/',
        blank=True, default='',
        validators=[validate_png],
    )

    def save(self, *args, **kwargs):
        current_favicon_name = str(self.favicon.name)
        super().save(*args, **kwargs)
        favicon_changed = False

        if self.favicon:
            favicon_changed = current_favicon_name != self.favicon.name

        if favicon_changed:
            resize_image(self.favicon, 32)

    def __str__(self):
        return str(self.title)
