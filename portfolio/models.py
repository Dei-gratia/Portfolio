from django.db import models
from phone_field import PhoneField
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


# HOME SECTION
class Home(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    greeting = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='home/')

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# ABOUT SECTION


class About(models.Model):
    heading = models.CharField(max_length=50)
    career = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/')

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career


class Email(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    primary = models.BooleanField()


class Phone(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    phone = PhoneField()
    primary = models.BooleanField()


class Profile(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    social_name = models.CharField(max_length=50)
    link = models.URLField(max_length=254)
    social_font_owesome_icon = models.CharField(max_length=50, blank=True)

# Skills Section


class Category(models.Model):
    name = models.CharField(max_length=50)

    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name


class Skills(models.Model):
    category = models.ForeignKey(
        Category, related_name='skills', on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=50)
    font_owesome_icon = models.CharField(max_length=50, blank=True)
    level = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)])

# PROJECTS SECTION


class Project(models.Model):
    image = models.ImageField(upload_to='projects/')
    title = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    description = models.TextField()
    future_scope = models.TextField(blank=True)

    def __str__(self):
        return self.title


class ProjectRequirements(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    technology = models.CharField(max_length=254)


class ProjectLink(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    link_text = models.CharField(max_length=50)
    link = models.URLField(max_length=254)
    font_owesome_icon = models.CharField(max_length=50, blank=True)


class ProjectModule(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()


class ProjectModuleImage(models.Model):
    project_module = models.ForeignKey(ProjectModule, on_delete=models.CASCADE)
    module_image = models.ImageField(upload_to='projects/modules/')


# WORK SECTION
class Work(models.Model):
    organisation = models.CharField(max_length=254)
    role = models.CharField(max_length=254)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)

    def __str__(self):
        return f'{self.role} at {self.organisation}'


class Contact(models.Model):
    name = models.CharField(max_length=254, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.email
