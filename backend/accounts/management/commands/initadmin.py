from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            if not settings.ADMINS:
                raise RuntimeError(
                    f"There is no such superuser credentials provided  in settings for initiate the project")
            for user in settings.ADMINS:
                splitted = user.rpartition(":")
                username = splitted[0]
                password = splitted[-1]
                if username.__contains__(":"):
                    raise RuntimeError(
                        f"Username contains `:` sign. It should match schema: `name:pwd,name2:pwd` and go on")
                print('Creating account for %s' % username)
                admin = User.objects.create_superuser(username=username, password=password)
                admin.is_active = True
                admin.is_admin = True
                admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')
