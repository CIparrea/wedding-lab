from django.db import models

# Create your models here.

STYLES = (
    ('M', 'Modern'),
    ('T', 'Traditional'),
    ('R', 'Rustic')
)

class Provider(models.Model):
  name = models.CharField(max_length=50)
  email = models.CharField(max_length=50)

  def __str__(self):
    return self.name
  
class Wedding(models.Model):
    date = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    providers = models.ManyToManyField(Provider)
    def __str__(self):
        return self.description
    
class Style(models.Model):
  style = models.CharField( "Wedding Style",
    max_length=1,
    # add the 'choices' field option
    choices=STYLES,
    # set the default value for meal to be 'B'
    default=STYLES[0][0]
  )
  wedding = models.ForeignKey(Wedding, on_delete=models.CASCADE)
  
  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_style_display()}"
  
