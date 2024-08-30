from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class DishType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(default=0)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='cook_set',
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups"
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='cook_set',
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions"
    )

    class Meta:
        verbose_name = "cook"
        verbose_name_plural = "cooks"

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("catalog:cook-detail", kwargs={"pk": self.pk})


class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(Cook, related_name="cooks")

    def __str__(self):
        return self.name
