from django.contrib.auth.signals import user_logged_in , user_logged_out , user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init, pre_save, pre_delete, post_init, post_delete, post_save
from django.core.signals import request_started, request_finished, got_request_exception
from django.db.models.signals import pre_migrate, post_migrate
from django.db.backends.signals import connection_created



@receiver(user_logged_in , sender=User)           #second way to connect
def login_success(sender , request , user , **kwargs):
    print('----------------user loged in signal---------------------------')
    print(f'sender : {sender}')
    print(f'request :{request} ')
    print(f'user : {user}')
    print(f'kwargs : {kwargs} ')
# user_logged_in.connect(login_success , sender=User)       #first way to connect



@receiver(user_logged_out , sender=User)
def logout(sender , request , user , **kwargs):
    print('----------------user loged out signal ---------------------------')
    print(f'sender : {sender}')
    print(f'request :{request} ')
    print(f'user : {user}')
    print(f'kwargs : {kwargs} ')
# user_logged_out.connect(logout , sender=User)


@receiver(user_login_failed)
def login_fail(sender , credentials , request , **kwargs):
    print('----------------user loged failed signal ---------------------------')
    print(f'sender : {sender}')
    print(f'request :{request} ')
    print(f'credentials : {credentials}')
    print(f'kwargs : {kwargs} ')
# user_login_failed.connect(login_fail)



@receiver(pre_save , sender=User)#sender = models name
def at_pre_save(sender, instance, **kwargs):
    print('----------------pre save signal ---------------------------')
    print(f'sender : {sender}')
    print(f'instance :{instance} ')
    print(f'kwargs : {kwargs} ')
# pre_save.connect(at_pre_save , sender=User)


@receiver(post_save , sender=User)#sender = models name
def at_post_save(sender, instance, created, **kwargs):
    if created:
        print('----------------post save signal ---------------------------')
        print('new reccord created')
        print(f'sender : {sender}')
        print(f'instance :{instance} ')
        print(f'created :{created} ')
        print(f'kwargs : {kwargs} ')
    else:
        print('----------------post save signal ---------------------------')
        print('update')
        print(f'sender : {sender}')
        print(f'instance :{instance} ')
        print(f'created :{created} ')
        print(f'kwargs : {kwargs} ')
# post_save.connect(at_post_save , sender=User)





@receiver(pre_delete , sender=User)#sender = models name
def at_pre_delete(sender, instance, **kwargs):
    print('----------------pre delete signal ---------------------------')
    print(f'sender : {sender}')
    print(f'instance :{instance} ')
    print(f'kwargs : {kwargs} ')


@receiver(post_delete , sender=User)#sender = models name
def at_post_delete(sender, instance, **kwargs):
    print('----------------post delete signal ---------------------------')
    print(f'sender : {sender}')
    print(f'instance :{instance} ')
    print(f'kwargs : {kwargs} ')



@receiver(pre_init , sender=User)#sender = models name
def at_pre_init(sender, *args, **kwargs):
    print('----------------pre init signal ---------------------------')
    print(f'sender : {sender}')
    print(f'args :{args} ')
    print(f'kwargs : {kwargs} ')


@receiver(post_init , sender=User)#sender = models name
def at_post_init(sender, *args, **kwargs):
    print('----------------post init signal ---------------------------')
    print(f'sender : {sender}')
    print(f'args :{args} ')
    print(f'kwargs : {kwargs} ')




@receiver(request_started)
def at_start_request(sender, enviorn , **kwargs):
    print('----------------pre request signal ---------------------------')
    print(f'sender : {sender}')
    print(f'enviorn :{enviorn} ')
    print(f'kwargs : {kwargs} ')


@receiver(request_finished)
def at_finish_request(sender, **kwargs):
    print('----------------post request signal ---------------------------')
    print(f'sender : {sender}')
    print(f'kwargs : {kwargs} ')


@receiver(got_request_exception)
def before_install_app(sender,request , **kwargs):
    print('----------------pre migrate signal ---------------------------')
    print(f'sender : {sender}')
    print(f'request : {request}')
    print(f'kwargs : {kwargs} ')



@receiver(pre_migrate)
def at_pre_migrate(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print('----------------pre migrrate signal ---------------------------')
    print(f'sender : {sender}')
    print(f'app_config : {app_config}')
    print(f'verbosity : {verbosity} ')
    print(f'interactive : {interactive} ')
    print(f'using : {using} ')
    print(f'plan : {plan} ')
    print(f'apps : {apps} ')
    print(f'kwargs : {kwargs} ')


@receiver(post_migrate)
def at_end_migrate_flush(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print('----------------post migrrate signal ---------------------------')
    print(f'sender : {sender}')
    print(f'app_config : {app_config}')
    print(f'verbosity : {verbosity} ')
    print(f'interactive : {interactive} ')
    print(f'using : {using} ')
    print(f'plan : {plan} ')
    print(f'apps : {apps} ')
    print(f'kwargs : {kwargs} ')



@receiver(connection_created)
def db_conn(sender, connection, **kwargs):
    print('-----------initial connection to database/ at time of runserver --------------')
    print(f'sender : {sender} ')
    print(f'connection : {connection} ')
    print(f'kwargs : {kwargs} ')