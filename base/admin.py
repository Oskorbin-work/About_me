from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Base, MenuLevOne, MenuLevTwo
from .models import ContentBody, Education, GradeEducation
from .models import MessageContact

from .models import Skill, ProjectSkills, TypeSkills

# Base classes. All pages
admin.site.register(Base, TranslatableAdmin)
admin.site.register(MenuLevOne, TranslatableAdmin)
admin.site.register(MenuLevTwo, TranslatableAdmin)

# For body page. One entry basedata to one page
admin.site.register(ContentBody, TranslatableAdmin)

# For body page. One basedata to page "Education"
admin.site.register(Education, TranslatableAdmin)
admin.site.register(GradeEducation, TranslatableAdmin)

# For body page. One basedata to page "Skills"
admin.site.register(Skill, TranslatableAdmin)
admin.site.register(ProjectSkills, TranslatableAdmin)
admin.site.register(TypeSkills, TranslatableAdmin)

#  For body page. One basedata to page "Contact"

admin.site.register(MessageContact, TranslatableAdmin)


