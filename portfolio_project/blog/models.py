from django.db import models

class Blog(models.Model):

    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    blog = models.TextField()

    def __str__(self):
        """ This will allow the admin screen to output a more meaningful
            description for the blog records. """

        return self.title
