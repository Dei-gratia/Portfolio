from django.shortcuts import render
from django.urls import reverse
from .models import Home, About, Profile, Category, Projects, Work, Email, Phone
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def index(request):
    # Home
    home = Home.objects.latest('updated')

    # About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

    # Skills
    categories = Category.objects.all()

    # Projects
    projects = Projects.objects.all()
    print(projects)

    # Email and Phone
    email = ''
    phone = ''
    if Email.objects.filter(primary=True):
        email = Email.objects.get(primary=True)
    if Phone.objects.filter(primary=True):
        phone = Phone.objects.get(primary=True)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New contact{form.cleaned_data["name"]}, {form.cleaned_data["email"]}: from Portfolio'
            email_message = form.cleaned_data['message']
            print(settings.CONTACT_EMAIL + '\n')
            send_mail(email_subject, email_message,
                      settings.CONTACT_EMAIL, settings.ADMIN_EMAILS)
            request.session['contact_success'] = True
            return HttpResponseRedirect(reverse("index"))

    else:
        form = ContactForm()

    contact_success = None
    if request.session.has_key('contact_success'):
        contact_success = request.session.get('contact_success')
        del request.session["contact_success"]
    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'projects': projects,
        'email': email,
        'phone': phone,
        'form': form,
        'contact_success': contact_success
    }

    return render(request, 'index.html', context)
