from django.contrib import admin
from nested_inline.admin import NestedModelAdmin, NestedStackedInline
from .models import Home, About, Profile, Category, Skills, Projects, Work, Email, Phone, Contact, ProjectLink, ProjectModule, ProjectModuleImage, ProjectRequirements

# Register your models here.

# HOME
admin.site.register(Home)


# ABOUT
class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1


class EmailInline(admin.TabularInline):
    model = Email
    extra = 1


class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 1


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInline,
        EmailInline,
        PhoneInline,
    ]


# SKILLS
class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 2


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        SkillsInline,
    ]


# PROJECTS
class ProjectModuleImageInline(NestedStackedInline):
    model = ProjectModuleImage
    extra = 1


class ProjectModuleInline(NestedStackedInline):
    model = ProjectModule
    inlines = [ProjectModuleImageInline, ]
    extra = 1


class ProjectLinkInline(NestedStackedInline):
    model = ProjectLink
    extra = 1


class ProjectRequirementsInline(NestedStackedInline):
    model = ProjectRequirements
    extra = 1


class ProjectsInLine(NestedModelAdmin):
    model = Projects
    extra = 1
    inlines = [
        ProjectRequirementsInline,
        ProjectModuleInline,
        ProjectLinkInline,
    ]


admin.site.register(Projects, ProjectsInLine)


# WORK
admin.site.register(Work)

# Contact
admin.site.register(Contact)
