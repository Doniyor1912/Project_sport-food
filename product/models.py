from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    price = models.DecimalField(max_digits=19,decimal_places=10)
    image = models.CharField()
    category_id = models.ForeignKey('Category', models.CASCADE, null=True)
    stock = models.IntegerField()
    rating = models.DecimalField(max_digits=5,decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'products'
        ordering = ('name',)

    def __str__(self):
        return f"{self.name}"



class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.CharField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Category'
        ordering = ('name',)

    def __str__(self):
        return self.name



class Testimonial(models.Model):
    customer_name = models.CharField(max_length=20)
    review = models.TextField()
    rating = models.DecimalField(max_digits=5,decimal_places=2)
    product_id = models.ForeignKey('Products', models.PROTECT, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Testimonial'
        ordering = ('customer_name',)

    def __str__(self):
        return self.customer_name


class Updateimage(models.Model):
    image = models.ImageField(upload_to=" ")