from PIL import Image
import os
import urllib
from django.contrib.auth import models
from django.core.files import File


class Thumbnail(models.Model):
    # Set the upload_to parameter to the directory where you'll store the
    # thumbs
    thumb = models.ImageField(upload_to='thumbs', null=true)

    """ Pulls image, converts it to thumbnail, then
saves in thumbs directory of Django install """
    def create_thumb(self):

        if self.url and not self.thumb:

            image = urllib.urlretrieve(self.url)

            # Create the thumbnail of dimension size
            size=128,128
            t_img = Image.open(image[0])
            t_img.thumbnail(size)

            # Get the directory name where the temp image was stored
            # by urlretrieve
            dir_name = os.path.dirname(image[0])

            # Get the image name from the url
            img_name = os.path.basename(self.url)

            # Save the thumbnail in the same temp directory
            # where urlretrieve got the full-sized image,
            # using the same file extention in os.path.basename()
            t_img.save(os.path.join(dir_name, "thumb" + img_name))

            # Save the thumbnail in the media directory, prepend thumb
            self.thumb.save(os.path.basename("thumb" + self.url),File(open(os.path.join(dir_name, "thumb" + img_name)))
 

