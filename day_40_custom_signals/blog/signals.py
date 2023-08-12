from django.dispatch import Signal , receiver

#creating signal x
notification = Signal()

#reciver 
@receiver(notification)
def show_noti(sender , **kwargs):
    print(sender)
    print(f'{kwargs}')