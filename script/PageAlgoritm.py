from wiki.models import settingUser, Page, PageStatmant, randomUnicalPage


class Algoritm():
    RUN_EVERY_MINS = 1

    hour = 0

    def do(self):

        self.hour += 1
        settings = settingUser.objects.all()
        
        for setting in settings:
            print(setting.User.username + ": "+ setting.Time_to_new_page)

            if settingUser.One_hour == setting.Time_to_new_page:
                print(settingUser.One_hour + ": " + str(self.hour))
                PageStatmant.objects.create(User = setting.User, Pages = randomUnicalPage(User=setting.User))

            if settingUser.Two_hour == setting.Time_to_new_page:
                if self.hour%2 == 0:
                    print(settingUser.Two_hour + ": " + str(self.hour))
                    PageStatmant.objects.create(User = setting.User, Pages = randomUnicalPage(User=setting.User))

            if settingUser.Six_hour == setting.Time_to_new_page:
                if self.hour%6 == 0:
                    print(settingUser.Six_hour + ": " + str(self.hour))
                    PageStatmant.objects.create(User = setting.User, Pages = randomUnicalPage(User=setting.User))

            if settingUser.One_day == setting.Time_to_new_page:
                if self.hour == 24:
                    print(settingUser.One_day + ": " + str(self.hour))
                    PageStatmant.objects.create(User = setting.User, Pages = randomUnicalPage(User=setting.User))
                    
        if self.hour == 24:
            self.hour = 0
        print("COUNTER: " + str(self.hour))


    