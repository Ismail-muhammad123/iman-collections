from .models import Category


def add_categories(request):
    categories = Category.objects.all()

    male = categories.filter(gender="M")
    female = categories.filter(gender="F")
    unisex = categories.filter(gender="U")

    return {
        "male_categories": male,
        "female_categories": female,
        "unisex_categories": unisex
    }
