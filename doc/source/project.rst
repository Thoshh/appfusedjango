Project
=======

Project vol ser una manera ràpida de començar un projecte. Ens dóna un esquelet mínim per a la nostra aplicació.

Com executar-lo:

* Feis un `svn export project nom-del-vostre-projecte`
* Copiar properties.py.template a properties.py
* Executa `python manage.py syncdb` i contesta a les preguntes
* Executa `python manage.py runserver`

Executant el navegador i anant a http://localhost:8000/ hauríeu de veure una plana de venvinguda.

Conceptes a destacar
--------------------

Separació de la configuració
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Es separa la configuració de l'aplicatiu del settings. Tot el que sigui susceptible de ser modificat en producció
s'ha de posar dins properties.py i utilitzat dins el settings via la variable de configuració::

    SITE_ROOT= getattr(properties, 'site_root', "http://localhost:8000/")

D'aquesta manera si a properties hi posam la variable site_root aquest tendrà preferència sobre el valor per defecte,
que en aquest cas és http://localhost:80000

El nivell de login es defineix al properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Al properties.py posam el logger::

    import logging
    logging.basicConfig(
        filename='the_filename_log_output.log',
        format="%(asctime)s-%(levelname)s-%(name)s-%(lineno)s-%(message)s",
        level = logging.INFO,
    )
    #logging.getLogger('app.module.file').setLevel(logging.INFO)
    #logging.getLogger('app2.module.file').setLevel(logging.ERROR)

D'aquesta manera podem configurar el loggin a diferents nivells a producció i desenvolupament. Això vol dir que
no hi ha cap excusa per fer servir print.

Als mòduls que requereixin loggin farem::

    import logging
    log = logging.getLogger(__name__)

D'aquesta manera el nom del nostre mòdul serà el del loggins i podrem fer-hi referència a la configuració de projecte.

