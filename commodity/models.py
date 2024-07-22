from django.db import models

# Create your models here.

class Bag(models.Model):
    class meta:
        verbose_name = "کیف"
        verbose_name_plural = "کیف"

    bag_name = models.CharField(max_length=100, verbose_name="نام برند")
    bag_number = models.IntegerField(verbose_name="تعداد کیف")
    bag_price = models.PositiveIntegerField(verbose_name="قیمت کیف")
    School_bag = 1
    Club_bag = 2
    Wallet = 3
    Travel_bag = 4
    bag_type = (
        (School_bag, "کیف مدرسه"),
        (Club_bag, "کیف باشگاه"),
        (Wallet, "کیف پول"),
        (Travel_bag, "گیف مسافرتی"),
    )
    Type = models.IntegerField(choices=bag_type, verbose_name="نوع کیف")

    def __str__(self) -> str:
        return f"اسم برند : {self.bag_name}  -  تعداد کیف ها : {self.bag_number}عدد  -  قیمت کیف  : {self.bag_price} - ریال {self.bag_image}"
