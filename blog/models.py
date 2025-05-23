from django.db import models

class Post(models.Model):  
    name= models.CharField(max_length=100, default='Anonymous')  
    title = models.CharField(max_length=50)  
    content = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)  
    picture=models.ImageField( upload_to="images/",default="images/default.PNG")

    def __str__(self):  
        return self.title
        
