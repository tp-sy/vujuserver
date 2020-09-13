from django.db import models

class Product(models.Model):
    drink_id = models.IntegerField(default=0)
    drink_name = models.CharField(max_length=100)
    drink_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.drink_name}:{self.drink_id}:{self.drink_price}"


class Song(models.Model):
    song_id = models.IntegerField()
    song_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.song_id}:{self.song_name}"

class UserInfo(models.Model):
    user_id = models.CharField(max_length=10)
    order_status = models.IntegerField(default=0)
    present = models.BooleanField(default=False)

    def __str__(self):
        return f"User {self.user_id}, status: {self.order_status}"