from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.views.generic import View
from django.http import HttpResponse
from django.template.loader import render_to_string
import json
from wiki.models import Page, settingUser, Categorys, Sites
from wiki.forms import settingsForm, MyUser

class MyRegisterFormView(FormView):

    form_class = MyUser

    success_url = "/"

    template_name = "registration/register.html"

    def form_valid(self, form):
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)



@login_required
def main(request):
    if not settingUser.objects.filter(User = request.user).exists():
            cat = Categorys.objects.get(id=1)
            site = Sites.objects.get(id=1)
            Usersettings = settingUser(User=request.user, category=cat, Site=site)
            Usersettings.save()

    pages = Page.objects.all()[:10]

    return render(request, 'main.html', {'pages': pages, 'titlepanel': "Главная"})

@login_required
def favorit(request):

    User = request.user

    if User.page_set.count() > 0:

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


class settingsView(View):
    def get(self, request):            
        form = settingsForm()
        form.fields['category'].initial = request.user.settinguser_set.get(User = request.user).category
        form.fields['category'].empty_label = None
        form.fields['Site'].initial = request.user.settinguser_set.get(User = request.user).Site
        form.fields['Site'].empty_label = None
        form.fields['Time_to_new_page'].initial = request.user.settinguser_set.get(User=request.user).Time_to_new_page
        form.fields['Time_to_new_page'].empty_label = None
        return render(request, 'settings.html', {'titlepanel': "Настройки", 'form': form, 'result': False})

    def post(self, request):
        print(request.POST)
        data = {
            'category' : request.POST.get('category'),
            'Site' : request.POST.get('Site'),
            'User' : request.user,
            'Time_to_new_page': request.POST.get('Time_to_new_page')
        }
        User = request.user
        instance = get_object_or_404(settingUser, User=User)
        form = settingsForm(data, instance=instance)
        result = False
        if form.is_valid():
            form.save()
            result = True
        form.fields['category'].empty_label = None
        form.fields['Site'].empty_label = None
        form.fields['Time_to_new_page'].empty_label = None
        return render(request, 'settings.html', {'titlepanel': "Настройки", 'form': form, 'result': result})



@login_required
def ajax_favorite(request):

    if request.is_ajax():

        if 'True' == request.POST.get('query'):

            title = request.POST.get('id')
            User = request.user
            result = True

            if not User.page_set.filter(title = title).exists():   

                page = Page.objects.get(title = title)
                page.favorite.add(User)
                page.save()
            else:

                Page.objects.get(title = title).favorite.remove(User)  
                result = False

        else:
            User = request.user
            title = request.POST.get('id')
            result = User.page_set.filter(title = title).exists()


        return HttpResponse(json.dumps({"result": result}), content_type="application/json")

@login_required
def ajax_history(request):

    User = request.user
    title = request.POST.get('id')
    page = Page.objects.get(title = title)

    if not settingUser.objects.get(User = User).history.filter(title = title).exists():

        setting = settingUser.objects.get(User = User)
        setting.history.add(page)
        setting.save()
    
    return HttpResponse(json.dumps(
        {"notifications_list": render_to_string('page.html', 
            {
            'page': page, 
            'back':request.META.get('HTTP_REFERER')
            }),
        }),
          content_type="application/json")
        
       
        
    