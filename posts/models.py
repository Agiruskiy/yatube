from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Groups(models.Model):
    title = models.TextField(max_length=100)
    slug = models.SlugField()
    description = models.TextField

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сообщество'
        verbose_name_plural = 'Сообщества'


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    group = models.ForeignKey(Groups, on_delete=models.CASCADE, related_name="group", blank=True, null=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
