from django.db import models

class News(models.Model):
    title = models.CharField("тема",max_length=100)
    image = models.ImageField(upload_to="img",verbose_name="сурот")
    description = models.TextField(max_length=1000,verbose_name="тушундурмо")
    date = models.DateTimeField(auto_now_add=True)
    bool = models.BooleanField()

    def _str_(self):
        return self.title
        


 