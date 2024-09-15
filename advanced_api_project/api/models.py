from django.db import models
class Author(models.Model):
    name = models.CharField(max_length=100)

    # Detailed comment explaining the Author model
    # Purpose: Store information about authors.
    # Fields:
    # - name: The name of the author.
