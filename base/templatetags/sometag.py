from django import template
from ..models import GradeEducation
from django.db.models import Avg
register = template.Library()

@register.filter
def grades_average(obj):
    some_objects = GradeEducation.objects.all().filter(education=obj.id)
    stars_average = some_objects.aggregate(Avg('amount'))
    return round(stars_average['amount__avg'], 1)


@register.filter(name='has_group')
def has_group(user, group_name):
    print(group_name)
    print(user.groups.all)
    print(user.groups.all())
    return user.groups.filter(name=group_name).exists()
