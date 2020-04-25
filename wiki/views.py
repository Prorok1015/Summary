from django.shortcuts import render
import json
from wiki.models import Page, settingUser, Categorys
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.http import HttpResponse
from django.template.loader import render_to_string
class MyRegisterFormView(FormView):

    form_class = UserCreationForm

    success_url = "settings/"

    template_name = "registration/register.html"

    def form_valid(self, form):
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)

@login_required
def main(request):
    pages = Page.objects.all()[:2]
    return render(request, 'main.html', {'pages': pages, 'titlepanel': "Главная"})

@login_required
def favorit(request):
    if Page.objects.filter(favorite = request.user).exists():
        pages = Page.objects.filter(favorite = request.user)
    else:
        pages = []
    return render(request, 'favorit.html', {'pages': pages,'titlepanel': "Избранное"})

@login_required
def history(request):
    if settingUser.objects.filter(User = request.user).exists():
            pages = settingUser.objects.get(User = request.user).history.all()[:10]
    else:
            pages = []
    return render(request, 'history.html', {'pages': pages, 'titlepanel': "История"})

@login_required
def settings(request):
    if not settingUser.objects.filter(User = request.user).exists():
        cat = Categorys.objects.get(id = 1)
        site = Sites.objects.get(SiteName = "Wikipedia")
        settingUser.objects.create(Category = cat, Site = site, User = request.user)
    return render(request, 'settings.html', {'titlepanel': "Настройки"})

@login_required
def ajax_favorite(request):

    title = request.POST.get('id', '')
    User = request.user
    result = True
    print(Page.objects.get(title = title).favorite.filter(username = User.username).exists())
    if not Page.objects.get(title = title).favorite.filter(username = User.username).exists():        
        page = Page.objects.get(title = title)
        page.favorite.add(User)
        page.save()
    else:
        Page.objects.get(title = title).favorite.remove(User)  
        result = False
    return HttpResponse(json.dumps({"result": result,}), content_type="application/json")

@login_required
def ajax_history(request):
    User = request.user
    title = request.POST.get('id', '')
    page = Page.objects.get(title = title)
    print(title)
    if not settingUser.objects.get(User = User).history.filter(title = title).exists():
        setting = settingUser.objects.get(User = User)
        setting.history.add(page)
        setting.save()
    
    return HttpResponse(json.dumps(
        {"notifications_list": render_to_string('page.html', {
            'page': page, 
            'back':request.META.get('HTTP_REFERER')
            }),
        }),
          content_type="application/json")
        
       
        
    