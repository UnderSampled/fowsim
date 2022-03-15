from django.contrib.auth import views as DjangoAuthViews
from django.conf import settings
from django.urls import path
from django.shortcuts import redirect

from . import views
from .forms import UserLoginForm

urlpatterns = [
    path('', lambda req: redirect('/search/')),
    path('search/', views.search_for_cards, name='cardDatabase-search'),
    path('card/<str:card_id>/', views.view_card, name='cardDatabase-view-card'),
    path('add_card/', views.add_card, name='cardDatabase-add-card'),
    path('decklists/', views.user_decklists, name='cardDatabase-user-decklists'),
    path('create_decklist/', views.create_decklist, name='cardDatabase-create-decklist'),
    path('edit_decklist/<int:decklist_id>/', views.edit_decklist, name='cardDatabase-edit-decklist'),
    path('save_decklist/<int:decklist_id>/', views.save_decklist, name='cardDatabase-save-decklist'),
    path('view_decklist/<int:decklist_id>/', views.view_decklist, name='cardDatabase-view-decklist'),
    path('delete_decklist/<int:decklist_id>/', views.delete_decklist, name='cardDatabase-delete-decklist'),
    path('test_error/', views.test_error, name='cardDatabase-test-error'),
    path('logout/', views.logout, name='cardDatabase-logout'),
    path('preferences/', views.userPreferences, name='cardDatabase-user-preferences'),
    path('login/', DjangoAuthViews.LoginView.as_view(template_name='registration/login.html',
                                                     authentication_form=UserLoginForm), name='cardDatabase-login'),
    path('register/', views.register, name='cardDatabase-register')
]