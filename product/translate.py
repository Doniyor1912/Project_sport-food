from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from product.models import Products, Category, Testimonial
from FAQ.models import FaqModel


@register(Products)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name','description')


@register(Testimonial)
class TestimonialTranslationOptions(TranslationOptions):
    fields = ('review',)



@register(FaqModel)
class FaqModelTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')