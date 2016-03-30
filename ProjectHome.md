### EN ###

The goal of this project is to create a minimum application that  goes beyond the Django tutorial and shows you how to use some of the normal practises you could find in a real application.

Some of the examples are also part of a blog post at http://trespams.com, my blog about Python and Django. The blog is in catalan, but it provides authomatic translation :)

Other samples comes from user request or from prototypes we have made at http://apsl.net our consulting Django company.

### CA ###

L'objectiu d'aquest projecte és crear una aplicació mínima que vagi un poc més enllà del tutorial de Django i mostri algunes de les pràctiques més habituals que hom es pot trobar en aplicacions reals.

Alguns dels exemples serveixen de suport a algún post del meu blog a http://trespams.com, per il·lustrar algún concepte de Python i Django.

Altres exemples provenen de prototis que hem anat fent a http://apsl.net, la nostra empresa consultora de Django i que hem trobat prou interessants i senzill per a posar-los aquí.

# How to run the examples #

On each folder you'll find an example which shows a "how-to-do" feature. To test it just copy/rename properties.py.template to properties.py, modify it to fit your needs (99% of time it would be ok) and run python manage.py runserver


# Sample applications #

  * **project**: start your project with this scheleton.

  * ajax like tail (for log display)

  * **Use imagekit** : upload your images and create thumbnails with imagekit, a practical example.

  * **upload images to a database** in batch mode.

  * performance test to compare with php. To support http://trespams.com/2009/05/10/django-vs-php-framewors/ post.

  * **appagenda** : Its a minimum application with html CRUD. Show also how you can use extjs to display a table and how to use jqgrid 3.2 to get the same as in extjs. Incluses extjs and jqgird libraries. I have had to patch jqgrid adding
` if(ts.p.jsonReader.cell) cur = cur[ts.p.jsonReader.cell]; ` the patch has been sent to jqgrid author but not feedback has been received.

  * **jqagenda**: Same example as above but just for jqgrid 3.3.1 with patch applied.
```
709d708
< 
770d768
< 					if(ts.p.jsonReader.cell) cur = cur[ts.p.jsonReader.cell];
```

  * **form\_test** Shows how can reuse multiple forms in an html page and then validate each form. Obvious but you have to get it!

  * **logsamples** Loggin configuration for your applications.

  * **project** Simple stub project. Just use svn export and you'll have a nearly configured project enabled to work in a multi-user environment.

  * **signals** Sample about using django signals.

  * **uploader** Sample uploader project.