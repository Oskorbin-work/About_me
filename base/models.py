from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from django.core.validators import MaxValueValidator, MinValueValidator


class MenuLevTwo(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=90, blank=True,),
        address=models.CharField(max_length=90, default="#"),
    )

    def __str__(self):
        return self.name


class MenuLevOne(TranslatableModel):
    menu_two = models.ManyToManyField(MenuLevTwo, blank=True, )
    translations = TranslatedFields(
        name=models.CharField(max_length=90, blank=True,),
        address=models.CharField(max_length=90, default="#", blank=True,),
    )

    def __str__(self):
        return self.name


class Base(TranslatableModel):
    menu_one = models.ManyToManyField(MenuLevOne, blank=True, )
    translations = TranslatedFields(
        title=models.CharField(max_length=90, blank=True,),
        name_menu=models.CharField(max_length=90, blank=True,),
    )

    def __str__(self):
        return self.title


class ContentBody(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=90, blank=True,),
        data_json=models.JSONField(blank=True, null=True)
    )

    def __str__(self):
        return self.title


class Education(TranslatableModel):

    translations = TranslatedFields(
        name=models.CharField(max_length=300, blank=True,),
        degree=models.CharField(max_length=90, blank=True,),
        specialty=models.CharField(max_length=90, blank=True,),
        city=models.CharField(max_length=90, blank=True,),
        country=models.CharField(max_length=90, blank=True,),
        name_diploma_project=models.CharField(max_length=300, blank=True,),
    )
    grade_diploma_project = models.IntegerField(default=1, blank=True, )
    learn_start = models.DateField(blank=True, null=True)
    learn_end = models.DateField(blank=True, null=True)
    # 2048 – it is max length url
    url_to_photo_diploma = models.CharField(max_length=2048, blank=True,)
    max_amount = models.IntegerField(
        default=100,)

    class Meta:
        ordering = ('-learn_end',)

    def __str__(self):
        return self.name+" ("+self.degree+")"


class GradeEducation(TranslatableModel):
    amount = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1),
        ],
        blank=True,
    )
    education = models.ForeignKey(Education, on_delete=models.CASCADE, blank=True, null=True)
    translations = TranslatedFields(
        name=models.CharField(max_length=90, blank=True,),
        commentary=models.CharField(max_length=90, blank=True,),
    )

    def __str__(self):
        return self.name


class ProjectSkills(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=90, blank=True, ),
    )
    link = models.URLField(
        max_length=200,
        db_index=True,
        unique=True,
        blank=True
    )

    def __str__(self):
        return self.name


class TypeSkills(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=90, blank=True, ),
    )

    def __str__(self):
        return self.name


class Skill(TranslatableModel):
    TYPE_CHOICES = (
        ('Base', 'Base'),
        ('Frameworks and libs', 'Frameworks and libs'),
        ('Tools', 'Tools'),
        ('Other', 'Other'),
    )
    img = models.ImageField(upload_to='skills/', blank=True, max_length=500)
    translations = TranslatedFields(
        name=models.CharField(verbose_name="name_90", max_length=90, blank=True, ),
        description=models.CharField(verbose_name="description_100", max_length=100, blank=True, ),
    )
    type_skill = models.ForeignKey(TypeSkills, on_delete=models.CASCADE, blank=True, null=True)
    projects_skill = models.ManyToManyField(ProjectSkills, blank=True, )

    def __str__(self):
        return self.name

    def get_type_choices(self):
        return [choice[0] for choice in self.TYPE_CHOICES]


class MessageContact(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=400, blank=True,),
    )

    def __str__(self):
        return self.name



