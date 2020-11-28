from django.db import models

class Project(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        """ This will allow the admin screen to output a more meaningful
            description for the project records. """

        return self.title
