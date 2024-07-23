import os.path
import json
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from confic import settings
from customer.models import Customer
from django.core.mail import send_mail



@receiver(post_save, sender=Customer)
def customer_save(sender, instance, created, **kwargs):
    if created:
        subject = f'Hi{instance.full_name}'
        message = 'Your customer has been created. Thank you!'
        from_email = (settings.EMAIL_HOST_USER)
        email_to = [instance.email]
        try:
            send_mail(subject, message, from_email, email_to)
            print(f'Email sent to {instance.email}!')
        except Exception as e:
            raise f'Error sending email: {e}'
    else:
        print('Product Update')


@receiver(pre_delete, sender=Customer)
def customer_delete(sender, instance, **kwargs):
      file = os.path.join('delete_customer', f'customer_{instance.id}.json')
      customer_data = {
          'id': instance.id,
          'full_name': instance.full_name,
          'email': instance.email,
          'phone': instance.phone,
          'address': instance.address,
          'image': instance.image,
      }
      with open(file, mode='w') as file_json:
          json.dump(customer_data, file_json, indent=4)

      print(f'{instance.full_name} was deleted !')


