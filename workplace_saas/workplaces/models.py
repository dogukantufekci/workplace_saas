from django.db import models

from businesses.models import Business
from workplace import tools
from workplace.constants import MaxLengths


class Workplace(models.Model):
    identifier = models.CharField(db_index=True, max_length=MaxLengths.IDENTIFIER, unique=True)
    recovery_email = models.EmailField(max_length=MaxLengths.EMAIL)
    
    email_key = models.CharField(blank=True, default='', max_length=MaxLengths.EMAIL_KEY)
    email_key_created_on = models.DateTimeField(blank=True, null=True)

    is_deleted = models.NullBooleanField()

    def get_business(self):
        return Business.objects.filter(workplace=self, workplace_business=True).get()

    def get_name(self):
        return self.get_business().name

    @staticmethod
    def generate_email_key(email):
        return tools.generate_key(
            length=MaxLengths.EMAIL_KEY,
            extra=email,
        )