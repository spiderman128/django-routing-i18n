from django.db import models
from django.utils.text import slugify
from django_comments.moderation import CommentModerator, moderator

class Page(models.Model):

   title = models.CharField(max_length = 50)
   text = models.TextField()
   slug = models.CharField(max_length = 50, editable=False)

   def __unicode__ (self):
        return self.title

   def save(self):
        self.slug = slugify(self.title)
        super(Page, self).save()

   class Meta:
      db_table = "page"

class News(models.Model):

   title = models.CharField(max_length = 50)
   text = models.TextField()
   slug = models.CharField(max_length = 50, editable=False)

   def __unicode__ (self):
        return self.title

   def save(self):
        self.slug = slugify(self.title)
        super(News, self).save()

   class Meta:
      db_table = "news"
      verbose_name = "news"
      verbose_name_plural = "news"

class NewsModerator(CommentModerator):
    email_notification = True
    auto_close_field   = 'posted_date'
    close_after        = 7

moderator.register(News, NewsModerator)