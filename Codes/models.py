from django.db import models
from SMS.models import CustomUser
import random

class Code(models.Model):
    number = models.CharField(max_length=10, blank=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.number


    def save(self, *args, **kwargs):
        number_list = [i for i in range(10)]
        code_items = []

        # getting 5 items from number_list by random
        for i in range(5):
            numbers = random.choice(number_list)
            code_items.append(numbers)
        code_str = "".join(str(codes) for codes in code_items)
        self.number = code_str
        return super().save(*args, **kwargs)
