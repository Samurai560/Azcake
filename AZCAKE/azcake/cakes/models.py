from django.db import models

# Create your models here.
class Cake(models.Model):
    name = models.CharField(max_length=32)
    price = models.PositiveSmallIntegerField(default=0)
    weight = models.FloatField(verbose_name="çəki", default=0, help_text="in kqs")
    description = models.TextField(max_length=3000)
    baked_at = models.DateTimeField(auto_now_add=True)
    stock_amount = models.PositiveSmallIntegerField(default=0)
    rating = models.FloatField(default=0)
    image_url = models.URLField(null=True)
    image = models.ImageField(upload_to="photos/%Y/%m/%d", null=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.price} AZN)"
    


