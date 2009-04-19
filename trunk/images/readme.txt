This project shows how to load an image onto a model using a script. 
This is not a complet project, it's own purpose is to ilustrate how can you
load images onto a model directly, withot a file.

$ python manage.py shell

>>>import base64
>>>from django.core.files.base import ContentFile
>>>from sample.models import Photo
>>># ja tenim tot el necessari
>>>raw_data = base64.b64decode(open('test/encoded_logo.b64').read())
>>># acabam de llegir les dades, podrien arribar directament
>>>foto = Photo()
>>>foto.image.save('the-image-name.gif', ContentFile(raw_data))
>>>foto.comments = "Django & Python rules!"
>>>foto.save()



