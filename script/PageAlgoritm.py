from wiki.models import settingUser, Page, PageStatmant, randomUnicalPage


class Algoritm():
    hour = 0

    def do(self):
        self.hour += 1
        settings = settingUser.objects.all()

        for setting in settings:
            
            if settingUser.One_hour == setting.Time_to_new_page:
                PageStatmant.objects.create(User = setting.User, Pages = randomUnicalPage(User=setting.User))

            if settingUser.Two_hour == setting.Time_to_new_page:
                if self.hour%2 == 0:
                    PageStatmant.objects.create(User = setting.User, Pages = randomUnicalPage(User=setting.User))

            if settingUser.Six_hour == setting.Time_to_new_page:
                if self.hour%6 == 0:
                    PageStatmant.objects.create(User = setting.User, Pages = randomUnicalPage(User=setting.User))

            if settingUser.One_day == setting.Time_to_new_page:
                if self.hour == 24:
                    PageStatmant.objects.create(User = setting.User, Pages = randomUnicalPage(User=setting.User))
                    
        if self.hour == 24:
            self.hour = 0


    