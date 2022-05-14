from django.contrib import admin
from cardDatabase.models.Ability import *
from cardDatabase.models.CardType import *
from cardDatabase.models.Effects import OneTimeEffect
from cardDatabase.models.User import Profile
from cardDatabase.models.DeckList import DeckList, DeckListCard, DeckListZone, UserDeckListZone
from cardDatabase.models.Spoilers import SpoilerSeason


class AbilityTextInline(admin.TabularInline):
    model = CardAbility
    extra = 1


class CardsWithAbilityTextInline(admin.TabularInline):
    model = CardAbility


class CardAdmin(admin.ModelAdmin):
    list_display = ('name', 'card_id', )
    search_fields = ['name', 'ability_texts__text', 'card_id']
    inlines = [AbilityTextInline]

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            self.exclude = ('ability_texts',)
        return super().get_form(request, obj=obj, **kwargs)


class AbilityTextAdmin(admin.ModelAdmin):
    list_display = ('text',)
    inlines = [CardsWithAbilityTextInline]
    search_fields = ['text']


admin.site.register(OneTimeEffect)
admin.site.register(Card, CardAdmin)
admin.site.register(AbilityText, AbilityTextAdmin)
admin.site.register(Profile)
admin.site.register(Keyword)
admin.site.register(DeckList)
admin.site.register(DeckListCard)
admin.site.register(DeckListZone)
admin.site.register(UserDeckListZone)
admin.site.register(SpoilerSeason)