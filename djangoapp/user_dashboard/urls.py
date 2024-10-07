from django.urls import path
from user_dashboard.views import (
    admin_home, section_one, section_one_create, section_one_update,
    section_two, section_two_create, section_two_update, section_three,
    section_three_create, section_three_update, section_four,
    section_four_create, section_four_single_photo,
    section_four_single_photo_update, section_four_single_photo_delete,
    section_four_ordering_photos, section_five, section_five_create,
    section_five_header_create, section_five_header,
    section_five_header_delete, section_five_pricing_offers,
    section_five_pricing_offers_create, section_five_pricing_offers_delete,
    section_five_price_card_icons, section_five_price_card_icons_create,
    section_five_price_card_icons_delete, section_five_offers_icons,
    section_five_offers_icons_create, section_five_offers_icons_delete,
    section_five_card, section_five_card_create, section_five_single_card,
    section_five_ordering_cards, section_five_card_update,
    section_five_card_delete, section_six, section_six_create,
    section_six_single_item, section_six_update, section_six_delete,
    section_seven, section_eight, section_eight_create,
    section_eight_single_video, section_eight_single_video_update,
    section_eight_single_video_delete, section_nine, section_nine_create,
    classes_type, classes_type_create, classes_type_single_class,
    classes_type_update, classes_type_delete, classes_type_ordering
)


app_name = 'user_dashboard'

urlpatterns = [
    path('user_dashboard/admin/', admin_home, name='admin_home'),
    # Section One
    path('user_dashboard/section-one/', section_one, name='section_one'),
    path('user_dashboard/section-one-create/',
         section_one_create, name='section_one_create'),
    path('user_dashboard/section-one-update/<int:id>/',
         section_one_update, name='section_one_update'),
    # Section Two
    path('user_dashboard/section-two/', section_two, name='section_two'),
    path('user_dashboard/section-two-create/',
         section_two_create, name='section_two_create'),
    path('user_dashboard/section-two-update/<int:id>/',
         section_two_update, name='section_two_update'),
    # Section Three
    path('user_dashboard/section-three/', section_three, name='section_three'),
    path('user_dasboard/section-three-create/',
         section_three_create, name='section_three_create'),
    path('user_dashboard/section-three-update/<int:id>/',
         section_three_update, name='section_three_update'),
    # Section Four
    path('user_dashboard/section-four/', section_four, name='section_four'),
    path('user_dashboaard/section-four-create/',
         section_four_create, name='section_four_create'),
    path('user_dashboard/section-four-ordering-photos/',
         section_four_ordering_photos, name='section_four_ordering_photos'),
    path('user_dashboard/section-four-single-photo/<int:id>/',
         section_four_single_photo, name='section_four_single_photo'),
    path('user_dashboard/section-four-single-photo-update/<int:id>/',
         section_four_single_photo_update,
         name='section_four_single_photo_update'),
    path('user_dashboard/section-four-delete/<int:id>/',
         section_four_single_photo_delete,
         name='section_four_single_photo_delete'),
    # Section Five
    path('user_dashboard/section-five/', section_five, name='section_five'),
    path('user_dashboard/section-five-header/',
         section_five_header, name='section_five_header'),
    path('user_dashboard/section-five-create/',
         section_five_create, name='section_five_create'),
    # Section Five - Header
    path('user_dashboard/section-five-header-create/',
         section_five_header_create, name='section_five_header_create'),
    path('user_dashboard/section-five-header-delete/',
         section_five_header_delete, name='section_five_header_delete'),
    # Section Five - Pricing Offers
    path('user_dashboard/section-five-pricing-offers/',
         section_five_pricing_offers, name='section_five_pricing_offers'),
    path('user_dashboard/section-five-pricing-offers-create/',
         section_five_pricing_offers_create,
         name='section_five_pricing_offers_create'),
    path('user_dashboard/section-five-pricing-offers-delete/',
         section_five_pricing_offers_delete,
         name='section_five_pricing_offers_delete'),
    # Section Five - Price Card Icons
    path('user_dashboard/section-five-price-card-icons/',
         section_five_price_card_icons, name='section_five_price_card_icons'),
    path('user_dashboard/section-five-price-card-icons-create/',
         section_five_price_card_icons_create,
         name='section_five_price_card_icons_create'),
    path('user_dashboard/section-five-price-card-icons-delete/',
         section_five_price_card_icons_delete,
         name='section_five_price_card_icons_delete'),
    # Section Five - Offers Icons
    path('user_dashboard/section-five-offers-icons/',
         section_five_offers_icons, name='section_five_offers_icons'),
    path('user_dashboard/section-five-offers-icons-create/',
         section_five_offers_icons_create,
         name='section_five_offers_icons_create'),
    path('user_dashboard/section-five-offers-icons-delete/',
         section_five_offers_icons_delete,
         name='section_five_offers_icons_delete'),
    # Section Five - Card
    path('user_dashboard/section-five-card/',
         section_five_card, name='section_five_card'),
    path('user_dashboard/section-five-card-create/',
         section_five_card_create, name='section_five_card_create'),
    path('user_dashboard/section-five-single-card/<int:id>/',
         section_five_single_card, name='section_five_single_card'),
    path('user_dashboard/section-five-ordering-cards/',
         section_five_ordering_cards, name='section_five_ordering_cards'),
    path('user_dashboard/section-five-card-update/<int:id>/',
         section_five_card_update, name='section_five_card_update'),
    path('user_dashboard/section-five-card-delete/<int:id>/',
         section_five_card_delete, name='section_five_card_delete'),
    # Section Six
    path('user_dashboard/section-six/', section_six, name='section_six'),
    path('user_dashboard/section-six-create/',
         section_six_create, name='section_six_create'),
    path('user_dashboard/section-six-single-item/<int:id>/',
         section_six_single_item, name='section_six_single_item'),
    path('user_dashboard/section-six-update/<int:id>/',
         section_six_update, name='section_six_update'),
    path('user_dashboard/section-six-delete/<int:id>/',
         section_six_delete, name='section_six_delete'),
    # Section Seven
    path('user_dashboard/section-seven/', section_seven, name='section_seven'),
    # Section Eight - Video
    path('user_dashboard/section-eight/', section_eight, name='section_eight'),
    path('user_dashboard/section-eight-create/',
         section_eight_create, name='section_eight_create'),
    path('user_dashboard/section-eight-single-video/<int:id>/',
         section_eight_single_video, name='section_eight_single_video'),
    path('user_dashboard/section-eight-single-video-update/<int:id>/',
         section_eight_single_video_update,
         name='section_eight_single_video_update'),
    path('user_dashboard/section-eight-single-video-delete/<int:id>/',
         section_eight_single_video_delete,
         name='section_eight_single_video_delete'),
    # Section Nine
    path('user_dashboard/section-nine/', section_nine, name='section_nine'),
    path('user_dashboard/section-nine-create/',
         section_nine_create, name='section_nine_create'),
    # Aulas
    path('user_dashboard/classes-type/', classes_type, name='classes_type'),
    path('user_dashboard/classe-type-create/',
         classes_type_create, name='classes_type_create'),
    path('user_dashboard/classes-type-single-class/<int:id>/',
         classes_type_single_class, name='classes_type_single_class'),
    path('user_dashboard/classes-type-update/<int:id>/',
         classes_type_update, name='classe_type_update'),
    path('user_dashboard/classes-type-delete/<int:id>/',
         classes_type_delete, name='classe_type_delete'),
    path('user_dashboard/classes-type-ordering/',
         classes_type_ordering, name='classes_type_ordering'),
]