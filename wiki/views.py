from django.shortcuts import render
from wiki.models import Page, settingUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView

class MyRegisterFormView(FormView):

    form_class = UserCreationForm

    success_url = "/"

    template_name = "registration/register.html"

    def form_valid(self, form):
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)

@login_required
def main(request):
    pages = Page.objects.all()[:2]
    return render(request, 'main.html', {'pages': pages})
@login_required
def favorit(request):
    return render(request, 'favorit.html', {})

@login_required
def history(request):
    print(request)
    pages = settingUser.objects.get(id = 1).history.all()
    return render(request, 'history.html', {'pages': pages})
@login_required
def settings(request):
    return render(request, 'settings.html', {})
    
# Create your views here.
