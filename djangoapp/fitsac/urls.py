from django.urls import path
from fitsac.views import (index, about, courses, pricing, gallery, blog,
                          blog_details, contact, admin
                          )


app_name = 'fitsac'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('courses/', courses, name='courses'),
    path('pricing/', pricing, name='pricing'),
    path('gallery/', gallery, name='gallery'),
    path('blog/', blog, name='blog'),
    path('blog-details/', blog_details, name='blog_details'),
    path('contact/', contact, name='contact'),
    # Admin
    path('fitsac/admin/', admin, name='admin'),
]
