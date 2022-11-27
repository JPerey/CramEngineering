from django.db import models
import uuid

# Create your models here.


class Formula(models.Model):
    title = models.CharField(max_length=200)
    featured_image = models.ImageField(null=True, blank=True)
    formula = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField("Tag", blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self) -> str:
        return self.name
