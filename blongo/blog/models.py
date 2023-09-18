from typing import Any

from django.contrib.auth.models import User
from django.db import models
from django.db.models.query import QuerySet
from django.urls import reverse
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        print("getting...")
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

    def create(self, **kwargs: Any) -> Any:
        print("creating...")
        return super().create(status=Post.Status.PUBLISHED, **kwargs)


class Post(models.Model):
    class Status(models.TextChoices):
        PUBLISHED = "PB", "published"
        DRAFT = "DF", "draft"

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.DRAFT
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )

    objects = models.Manager()  # the default manager
    published = PublishedManager()  # Custom published manager

    class Meta:
        ordering = ["-publish"]
        indexes = [models.Index(fields=["-publish"])]

    def get_absolute_url(self):
        return reverse(
            "blog:post_detail",
            args=[
                self.publish.year,
                self.publish.month,
                self.publish.day,
                self.slug,
            ],
        )

    def __str__(self):
        return self.title
