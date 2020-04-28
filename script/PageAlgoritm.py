from wiki.models import settingUser, Page
from django_cron import CronJobBase

class Algoritm(CronJobBase):
    RUN_EVERY_MINS = 1

    hour = 0

    def do(self):
        self.hour += 1
        Users = settingUser.objects.all()

        for user in Users:
            if settingUser.One_hour == user.Time_to_new_page:
                print(settingUser.One_hour + ": " + str(self.hour))
            if settingUser.Two_hour == user.Time_to_new_page:
                if self.hour%2 == 0:
                    print(settingUser.Two_hour + ": " + str(self.hour))
            if settingUser.Six_hour == user.Time_to_new_page:
                if self.hour%6 == 0:
                    print(settingUser.Six_hour + ": " + str(self.hour))
            if settingUser.One_day == user.Time_to_new_page:
                if self.hour == 24:
                    print(settingUser.One_day + ": " + str(self.hour))
                    self.hour = 0


    