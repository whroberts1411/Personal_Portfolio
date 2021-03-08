from django.db import models
from django_resized import ResizedImageField

class Project(models.Model):

    # This crops and resizes images that are uploaded to keep the stored
    # image within a reasonable size. 
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = ResizedImageField(size=[640, 512], crop=['middle','center'],
                              keep_meta=False, quality=75,
                              upload_to='portfolio/images/' )
    url = models.URLField(blank=True)

    def __str__(self):
        """ This will allow the admin screen to output a more meaningful
            description for the project records. """

        return self.title
