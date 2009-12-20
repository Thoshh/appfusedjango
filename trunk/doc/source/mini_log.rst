Mini Log
==========

Aquesta apliació és un mini log, que en servirà de tutorial per
a veure com podem crear una aplicació completa amb Django.

Reconeixements
---------------

Mini log està creat a partir d'un guió d'exemple que va fer servir `Ricardo Galli <http://twitter.com/gallir>`_
a un dels seus cursos i que amablement ha cedit. He mantingut més o manco
el codi font de Ricardo, els comentaris són meus i l'he adaptat per utilitzar
la configuració d'AppfuseDjango i per a que servesqui de petit tutorial.



Creant el projecte
-------------------

Crearem un projecte al que anomenarem mini-blog a partir del projecte project
d'appusedjango::

    svn export project mini-log

Això ens haurà creat una project exacament igual que project, però sense
configurar. Així que com el primer que farem serà copiar el properties.py.template
a properties.py i regenerar la base de dades sqlite.::

    cp properties.py.template properties.py
    python manage.py syncdb

Contestau a les preguntes i ens crearà una estrucutra mínima, que podrem
executar amb::

    python manage.py runserver

Per defecte al properties.py template hem configurat l'aplicació amb una base
de dades anomenada `db.sqlite`. Fitxem-nos que el que feim és configurar a
properties.py templates les variables que han de canviar del settings.py entre
l'entorn de desenvolupament i l'entorn de producció.::

    DATABASE_ENGINE = getattr(properties, 'database_engine', 'sqlite3')
    DATABASE_NAME = getattr(properties, 'database_name', 'db.sqlite')
    DATABASE_USER = getattr(properties, 'database_user', None)
    DATABASE_PASSWORD = getattr(properties, 'database_password', '')
    DATABASE_HOST = getattr(properties, 'database_host','')
    DATABASE_PORT = getattr(properties, 'database_port','')

És a dir, si a properties.py hi ha una variable anomenada ``database_name`` es
farà servir aquesta com a nom de la base de dades, en cas contrari es farà
servir el defecte, que en nostre cas hem establit com ``db.sqlite``

Encara que Django té el seu propi ORM (Object Relational Mapper) sempre podem
anar a baix nivell i obenir un cursor de base de dades::

    $ python manage shell
    >>> from django.db import connection
    >>> cursor = connection.cursor()
    >>> cursor.execute('select * from django_site')
    <django.db.backends.sqlite3.base.SQLiteCursorWrapper object at 0x1096c800>

    >>> for r in cursor.fetchall():
        ...:     print r
        ...:
        ...:
    (1, u'example.com', u'example.com')


Cream l'aplicació
------------------

Ara podem crear l'aplicació i afegir-la al nostre ``settings.py`` de manera
que quedi registrada al projecte::

    $ python manage.py startapp log

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',

        'django.contrib.admin',
        'log',
    )

La comanda ``startapp`` ens ha creat una estructura d'aplicació Django, si
hi entram veurem que realment no és més que un paquet Python

Dins aques registre veurem un mòdul anomenat ``models.py``, en aquest arxiu és
on definirem els models

Definim el model
-----------------

Editem ``log/models.py``::

    from django.db import models

    class Comment(models.Model):
        date = models.DateTimeField(auto_now_add=True)
        nick = models.CharField(max_length=20)
        comment = models.TextField()

La comanda ``validate`` en permet verificar el el nostre model s'ha creat
correctamente. Per un cas senzill com aquest no té molta utilitat, però convé
executar-la quan definim més d'una clase dins el mateix arxiu, d'aquesta manera
evitam crear taules amb relacions mal definides.::

    $ python manage.py validate

De la mateixa manera la comanda ``sqlall`` ens permet veure l'sql que es
generarà per la nostra base de dades::

    $ python manage.py sqlall log
    BEGIN;
    CREATE TABLE "log_comment" (
        "id" integer NOT NULL PRIMARY KEY,
        "date" datetime NOT NULL,
        "nick" varchar(20) NOT NULL,
        "comment" text NOT NULL
    )
    ;
    COMMIT;

Si tot és correcte executarem la comanda ``syncdb`` que ens crearà les taules
del model que he definit dins la base de dades.::

    $ python manage.py syncdb

Utilitzant l'administrador de Django
-------------------------------------

Una de les eines que ens proporciona Django és un administrador que en permet
interactuar amb els models, amb les nostres dades, d'una manera molt potent i
amb un mínim de configuració i treball per la nostra part.

Per utilitzar-lo el primer que farem serà verificar que dins l'arxiu ``urls.py``
del projecte hi ha aquest línies de codi::

    admin.autodiscover()

i que a l'``urlpatterns`` tenim definit l'url de l'aplicació d'administració::

    urlpatterns = patterns('',
         # direct to template sample
         (r'^$',direct_to_template, {'template': 'index.html'}),
         # application url include
         #(r'^app/', include('app.urls')),
         # Administration
         (r'^admin/doc/', include('django.contrib.admindocs.urls')),
         (r'^admin/(.*)', admin.site.root),
    )

Dins l'aplicació ``log`` crearem també un arxiu anomenat ``admin.py`` aquest
arxiu és el que cerca Django per a registrar la nostra aplicació dins l'administrador
i permetre'ns modifcar i afegir registres.

Crearem l'arxiu de manera que quedi com::

    # -*- coding: UTF-8 -*-
    """
    Mòdul d'administració
    """

    from django.contrib import admin
    from log.models import Comment

    admin.site.register(Comment)

Si tot va bé ara podem tornar a excutar el ``python manage.py runserver`` i
aquesta vegada apuntar a `http://localhost:8000/admin/ <http://locahost:8000/admin>`_
En sotirà la pantalla de l'administrador i ens demanarà login i password, hem
de posar els que hem defint quan hem fet el primer ``syncdb``.

Veurem que ens apareix una secció anomenada ``Log``amb un ``Comments`` que és
precisament el que acabam de crear.

Podem començar a introduïr dades!

Mapejant URLs amb la nostra aplicació
-------------------------------------

Es considera una bonoa pràctica tenir les urls dins la aplicació i lligar
les aplicacions a nivell de projecta amb el ``urls.py`` de primer nivell.

Per això crearem un arxiu ``urls.py`` dins l'aplicació ``log`` i modificam
l'arxiu ``urls.py`` del projecte principal per a que inclogui les
urls quan la URI que se'ns passi comenci per ``log``. Aquest nom és arbitrari,
dependrà de la nomclatura que li donem al nostre projecte i no té perquè ser
el nom de l'aplicació.::

    urlpatterns = patterns('',
          # direct to template sample
          (r'^$',direct_to_template, {'template': 'index.html'}),
          # application url include
          (r'^log/', include('log.urls')),
          # Administration
          (r'^admin/doc/', include('django.contrib.admindocs.urls')),
          (r'^admin/(.*)', admin.site.root),
    )

L'arxiu ``urls.py`` que acaban de crear tindrà la forma::

    #!/usr/bin/env python
    # -*- coding: UTF-8 -*-

    from django.conf.urls.defaults import patterns, url


    urlpatterns = patterns("log.views",
        url(r'^$', 'index', name='main-log'),
        url(r'^time/([-+]{0,1}\d)*$', 'current_time', name='curent_time'),
    )

Django el que fa és anar processant les urls per ordre, quan arribi a una url
que comenci per *log* el que farà és processar les urls que estan dins l'arxiu
*urls.py* que hem creat, quan trobi una expressió que coincideix executarà
la funció el nom de la qual hem passat com a segon parametre (index, current_time),
que es troba a *log.views*, a aquest mapeig entre URL i funció li podem assignar
un nom que ens permetrà fer-hi referència en un futur.

Creant views.py
----------------

En aquest punt si se'ns acudís apuntar el nostre naveador cap a http://localhost:8000/log/
obtindríem un missatge d'error que ens indica que no existeix la funció index
dins el mòdul views de l'aplicació log. Encara no l'hem creat. Anem a fer-ho::

    from django.shortcuts import render_to_response
    from django.http import HttpResponseRedirect
    from django.core.urlresolvers import reverse
    from django import forms

    from log.models import Comment
    import datetime


    class CommentForm(forms.ModelForm):
        "Simple form for the Person model"

        class Meta:
            model = Comment


    def index(request):
        data = {}
        if request.method == 'POST':
            new_comment = CommentForm(request.POST)
            if new_comment.is_valid():
                new_comment.save()
                return HttpResponseRedirect(reverse('main-log'))
        else:
            new_comment = CommentForm()
        data['method'] = request.method
        data['comments'] = Comment.objects.order_by("-date")
        data['form'] = new_comment
        return render_to_response("log/log.html", data)


    def current_time(request, offset):
        if offset:
            offset = int(offset)
        else:
            offset = 0
        now = datetime.datetime.now()
        if offset > 0:
            now = now - datetime.timedelta(hours=offset)
        data = {"current_time": now, "offset": offset}
        return render_to_response("log/current_time.html", data)


Anem a estudir el que estam fent. El primer que hem fet és definir un
formulari que ens servirà per a que la gent pugui introduïr els comentaris.
Com que el formulari mapeja el model, farem servir una drecera que té Django
anaomenada ModelForm, fitxau-vos que n'és de fàcil, simplement li hem de dir
a partir de quin model generam el formulari::

    class CommentForm(forms.ModelForm):
        "Simple form for the Person model"

        class Meta:
            model = Comment

Ara ja podem fer servir el formulari dins la nostra plantilla, per això
l'instanciarem dins la funció *index*.::

    def index(request):
        data = {}
        if request.method == 'POST':
            new_comment = CommentForm(request.POST)
            if new_comment.is_valid():
                new_comment.save()
                return HttpResponseRedirect(reverse('main-log'))
        else:
            new_comment = CommentForm()
        data['method'] = request.method
        data['comments'] = Comment.objects.order_by("-date")
        data['form'] = new_comment
        return render_to_response("log/log.html", data)

*data* és el diccionari que contindrà les dades que presentarem a la plantilla.
Si el mètode amb el qual s'arriba a aquest funció és un POST vol dir que estam
intentant afegir un nou formulari, per tant omplirem el formulari amb les
dades del POST.

Comprovarem que les dades són vàlides, com que és un formulari molt senzill
lligat a un model el que comprovarà és que tots els camps obligatoris estiguin
plens i siguin dels tipus correcte.

Si tot és vàlid guardam les dades a la base de dades i feim un redirect per
evitar duplicitats degudes alr refresc de la pantalla. Fitxem-nos amb l'ús que
se fa del ``reverse``, d'aquesta manera evitam fer que les nostres urls estiguin
prefixades al codi i podríem canviar-les en qualsevol momet sense tocar res més.

Si el mètode d'entrada és un GET instanciam el formulari sense dades. Finalment,
tant si és GET com si és un POST invàlid, el que feim és obtenir totes les
dades del model ``Comment.objects.order_by("-date")``. Com podem veure no hem
utilitzat SQL per res, l'ORM de Django se n'encarrega de tot.

També passam a la plantilla el formulari d'entrada de comentaris i el mètode.

La funció *current_time* sols té interès per veure com no estam limitats a fer
servir un model, sinó que podem executar codi Python arbitrari i passar-ne
el resultat a una plantilla Django.

Les plantilles
---------------

Podem veure que les funcions de *views.py* fan referència a arxius html, aquests
arxius són les plantilles Django. Tal com estan definides a aquest exemple són
únicament arxius html on hem posat tags que fan referència a les variables
de Django que hem passat dins el diccionari de dades. Pel que ens interessa
veurem la plantilla ``log.html``

.. code-block:: html

    <html>
     <body>
     <p>hola, el mètode va ser {{ method }}</p>

    {% if comments %}
         {% for c in comments %}
         <p>
         <strong>nick:</strong> {{c.nick|escape}} <br/>
         <strong>comentari:</strong> {{c.comment|escape}}
         </p>
         {% endfor %}
    {% else %}
    <p>No hi ha comentaris! Sigues el primer en comentar!</p>
    {% endif %}

     <h2>Envía un comentari</h2>
     <form method="POST" action=".">
    <table>
    {{form}}
    </table>
     <BR/>
     <input type="submit" value="enviar">
     </form>
     </body>
     </html>

Les variables és referencien amb un doble claudator ``{{nom_variable}}`` i
els tags amb una clau i un tant per cent ``{% tag %}``

Fitxem-nos com amb una sola variable ``form``` Django renderitza el formulari
d'entrada de comentaris.

Django cerca les plantilles allà on li diguem al settings a la part de::

    TEMPLATE_DIRS = getattr(properties, 'template_dirs', ('templates',))

als nostre *properties* ho hem definit de tal manera que el directori de
cerca de plantilles sigui el del projecte.

Exercici per al lector
-----------------------

* Fer que totes les plantilles d'aquest tutorial heredin de *base.html*
* Modificar index.html per afegir enllaços a l'aplicació log
