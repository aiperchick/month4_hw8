from django.db import models


class CustomerCl(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TagCl(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProductCl(models.Model):
    class Meta:
        verbose_name = "Одежда"
        verbose_name_plural = "Одежды"

    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(TagCl)

    def __str__(self):
        return self.name


class OrderCl(models.Model):
    STATUS = (
        ("На обработке", "На обработке"),
        ("Выехал", "Выехал"),
        ("Доставлен", "Доставлен"),
    )
    customer = models.ForeignKey(CustomerCl, on_delete=models.CASCADE)
    product = models.ForeignKey(
        ProductCl, on_delete=models.CASCADE, related_name="order_cloth"
    )
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS)

    def __str__(self):
        return self.product.name
