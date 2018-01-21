from django.db import models

# the following lines added:
import datetime
from django.utils import timezone

class Question(models.Model):
   question_text = models.CharField(max_length=200)
   pub_date = models.DateTimeField('date published')
   #image = models.ImageField('img', upload_to='path/')
   image = models.FileField(upload_to='post_image',blank=True)

   def __str__(self):
       return self.question_text

   def was_published_recently(self):
       now = timezone.now()
       return now - datetime.timedelta(days=1) <= self.pub_date <= now

   def user_directory_path(instance, filename):
       # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
       return 'user_{0}/{1}'.format(instance.user.id, filename)

   was_published_recently.admin_order_field = 'pub_date'
   was_published_recently.boolean = True
   was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
   question = models.ForeignKey(Question,'')
   choice_test = models.CharField(max_length=200)
   votes = models.IntegerField(default=0)

   def __str__(self):
       return self.choice_test