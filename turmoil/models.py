from django.db import models
from PIL import Image
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from image_cropping import ImageRatioField


class NavbarItem(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name

class Notice(models.Model):
    message = models.TextField()

    def __str__(self):
        return self.message[:50]  # Display the first 50 characters

class Thumbnail(models.Model):
    image = models.ImageField(upload_to='thumbnails/')
    alt_text = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.alt_text or "Thumbnail"

class SiteLogo(models.Model):
    image = models.ImageField(upload_to='logos/')
    alt_text = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.alt_text or "Site Logo"

class Advertisement(models.Model):
    image = models.ImageField(upload_to='ads/')
    url = models.URLField()
    alt_text = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.alt_text or "Advertisement"

class Article(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    date = models.DateField()
    author = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='images/')
    thumbnail_cropped = ImageSpecField(source='thumbnail',
                                       processors=[ResizeToFill(61, 47)],
                                       format='JPEG',
                                       options={'quality': 100})
    image = models.ImageField(upload_to='images/')
    image_cropped = ImageSpecField(source='image',
                                   processors=[ResizeToFill(598, 134)],
                                   format='JPEG',
                                   options={'quality': 100})
    cropping = ImageRatioField('image', '598x134')
    content = models.TextField()
    comments_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        # Resize thumbnail
        thumbnail_img = Image.open(self.thumbnail.path)
        if thumbnail_img.height > 47 or thumbnail_img.width > 61:
            output_size = (61, 47)
            thumbnail_img.thumbnail(output_size)
            thumbnail_img.save(self.thumbnail.path, quality=100)
        
        # Resize main image
        main_img = Image.open(self.image.path)
        if main_img.height > 134 or main_img.width > 598:
            output_size = (598, 134)
            main_img.thumbnail(output_size)
            main_img.save(self.image.path, quality=100)

class Slider(models.Model):
    slide_image = models.ImageField(upload_to='images/slides/')
    slide_image_cropped = ImageSpecField(source='slide_image',
                                         processors=[ResizeToFill(705, 298)],
                                         format='JPEG',
                                         options={'quality': 100})
    slide_title = models.CharField(max_length=200)
    slide_subtitle = models.CharField(max_length=200)
    side_image = models.ImageField(upload_to='images/')
    side_image_cropped = ImageSpecField(source='side_image',
                                        processors=[ResizeToFill(47, 50)],
                                        format='JPEG',
                                        options={'quality': 100})
    side_title = models.CharField(max_length=200)
    side_subtitle = models.CharField(max_length=200)
    cropping = ImageRatioField('slide_image', '705x298')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.slide_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        # Resize slide image
        slide_img = Image.open(self.slide_image.path)
        if slide_img.height > 298 or slide_img.width > 705:
            output_size = (705, 298)
            slide_img.thumbnail(output_size)
            slide_img.save(self.slide_image.path, quality=100)
        
        # Resize side image
        side_img = Image.open(self.side_image.path)
        if side_img.height > 50 or side_img.width > 47:
            output_size = (47, 50)
            side_img.thumbnail(output_size)
            side_img.save(self.side_image.path, quality=100)
