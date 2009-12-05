Què és un decorador
===================

Un decorador és el nom d'un *patró de disseny*. Els decoradors alteren de manera dinàmica la funcionalitat d'una funció,
mètode a classe sense tenir-ne que fer subclasses o canviar el codi font de la classe decorada. En el sentit de Python
un decorador és quelcom més, inclou el patró de disseny, però van més allà, Bruce Eckel els assimila a les macros de Lisp.

Els decoradors i la seva manera d'utilitzar-se ens ajuden a fer el nostre codi més net, a autodocumentar-lo i a
diferència d'altres llenguatges de programació no requereixen que ens aprenguem un altre llenguatge de programació
(com passa amb les anotacions de Java per exemple). En la seva utilització podem atracar-nos a la programació orientada
a aspectes (AOP) o utilitzar-los per a afegir sistemes de control a les nostres funcions, de log, caché, ...
Les possibilitats són infinites. El decoradors formen part de Python des de la versió 2.4 i com
diu `Michele Simionato <http://www.phyast.pitt.edu/~micheles/>`_ ens aporten el següent: 
    * Redueixen el codi comú i repetitiu (l'anomenat codi _boilerplate_).
    * Afavoreixen la separació de responsabilitats del codi
    * Augmenten la legibilitat i la mantenibilitat
    * Els decorador són explícits.

Aquesta potència té un preu: en rendiment (que s'haurà d'avaluar per a cada aplicació) i en complexitat a l'hora de
desenvolupar-los. Un decorador típic veurem que és molt bo d'escriure, però la cosa es complica un poc quan volem passar
paràmetres o mantenir la signatura del mètode. Aquesta complexitat no és tant pel codi que s'ha d'escriure sinó perquè
hem de recordar com s'ha d'escriure el decorador per a cada cas.

Afortunadament veurem que gent com `Michele Simionato <http://pypi.python.org/pypi/decorator/3.1.2>`_ han desenvolupat
paquets que ens simplifiquen molt la vida. Tot i això i abans de fer servir aquestes utilitats convé saber què són i
desenvolupar-los sense ajuda. És un poc com aprendre's les taules de multiplicar i després ja utilitzar la calculadora.

Classificació dels decoradors
-----------------------------

Podem dividir els decoradors en grups:

    * Segons els paràmetres que admeten:
        * No admeten paràmetres
        * Sí admeten paràmetres
    * Segons si preserven la signatura del mètode al que decoren:
        * Decoradors no que preserven la signatura
        * Decoradors que si la preserven

Els decoradors més senzill són aquells que no admeten paràmetres i no preserven la signatura

Un decorador que no fa res
--------------------------

Per començar crearem un decorador que el que farà es convertir qualsevol funció en un /dev/null, és a dir, no retornarà
res i no farà res amb la funció.::

    def forat_negre(f):
        def none():
            pass
        return none

    @forat_negre
    def di_hola():
        return "hola"

Si executam `di_hola()` no tendrem cap resultat, millor dit tindrem `None`

La sintaxi @ del decorador de Python és el que s'anomena **syntactic sugar**, és a dir, una manera d'escriure les coses
que ens simplifica la legibilitat, però fet i fet es podria escriure perfectament com::

    di_hola = forat_negre(di_hola)
    di_hola()

i tendríem el mateix que fa el decorador. Recordem que les funcions són objectes i que es poden assignar i passar com
a paràmetres a Python.

Tot i la senzillesa de l'exemple ens serveix per veure que un decorador no és més que un envolcall cap a una funció i
per tant ha de retornar una funció, més concretament un *callable*, per a entendre'ns, qualsevol cosa que posant-hi
un doble parèntesi al costat () no peti.::

    def retorna_objecte(f):
       ....:     def obj():
       ....:         return object()
       ....:     return obj
       ....:

    In [17]: def di_hola():
       ....:     return "Hola"
       ....:

    In [18]: di_hola = retorna_objecte(di_hola)

    In [19]: di_hola()
    Out[19]: <object object at 0xf7f745e8>

Al nostre decorador `forat_negre` li hem passat una funcició sense paràmetres, però si li passam paràmetres ens trobarem
una sorpreseta::

    #!python
    @forat_negre
    def suma(a,b):
        return a,b

    suma(2,3)

    TypeError Traceback (most recent call last)
    TypeError: none() takes no arguments (2 given)

que per una altra banda és del tot normal, hem definit el `forat_negre` de tal manera que retorna una funció sense
paràmetres, així que si li intentam passar els paràmetres que tenia la funció decorada senzillament es queixa i peta.

Anem a definir un poc millor el nostre decorador per a que no ens passi així i poder admetre el mateixos paràmetres que
la funció decorada::

    #!python
    def forat_negre(f):
        "d'aquí no surt res"
        def none(*args, **kw_args):
            pass
        return none

    @forat_negre
    def suma(a,b):
        "suma dos parametres qualsevols si pot"
        return a+b

    suma(2,2)

Ara ja no dona error. Així doncs *una altra conclusió*: a més de tornar una funció, hem de procurar que la definició de
la funció que tornam admeti al manco els mateix nombre de paràmetres que la funció que volem decorar. Si no sabem
quants són aquests ens curam en salut amb \*args i \*\*kw_args.

Fixem-nos que no hem mantingut la signatura de la funció i com a experiment intentau fer un help(suma). Tornarem damunt
això un poc més endavant. Ara per ara ja sabem com crear decoradors simples a partir d'una funció.

Fent decoradors no intrusius
----------------------------

Si heu fet un `help(suma)` o un `suma.__name__` potser un haureu sorprés en veure que le nom de la funció és *none* en
lloc de l'esperada `suma`. Si pensau amb el que hem fet tampoc és d'extranyar, fet i fet hem substituït la funció
original per una altra, recordem que el decorador f aplicat damunt la funció g és equivalent a fer g = f(g).

El que és aconsellable és que el decorador sigui capaç de mantenir la documentació i el nom de la funció que decora,
ja que d'aquesta manera es simplifica l'ús de la funció i els autocompletadors de codi no es tornen bojos.

Això ho podem fer de dues maneres: la llarga i la curta

**La manera llarga**::

    #!python
    def forat_negre(f):
        def none(*args, **kw_args):
            pass
        none.__doc__= f.__doc__
        none.__dict__= f.__dict__
        none.__name__= f.__name__
        return none

Amb les tres instruccions adicionals que hem posat tornar a recuperar les metadades de la funció original que passam
al decorador. Si hara feim un help veurem que es fa damunt el nom de la funció correcta __suma__ i que l'ajuda també
és la seva.::

    Help on function suma in module __main__:

    suma(*args, **kw_args)
        Suma dos parametres qualsevols si pot

Fixem-nos en la signatura de la funció no s'ha preservar. Abans admetia dos paràmetres i ara n'admet un nombre
qualsevol. Per la majoria de casos això no té més importància, però al final de l'article veurem com es pot resoldre.

**La manera curta**

Com que el tema de reservar les metadades és força interessant i comú, al mòdul functools hi trobam la funció `wraps`
que és en sí mateixa un decorador i que fa aquesta funció. D'aquesta manera el codi anterior quedaria::
    
    from functools import wraps

    def forat_negre(f):
        @wraps(f)
        def none(*args, **kw_args):
            pass
        return none

Fixau-vos que hem fet servir un decorador per crear un altre decorador. Insistirem en aquest tema més tard.


Un decorador amb arguments
--------------------------

El decorador que hem fet a l'apartat anterior era prou simple, feia ben poca cosa i no tenia paràmetres. Si volem fer
decoradors hem de fer primer de tot que siguin útils, i també ens trobarem amb la necessitat de que aquests decoradors
admetin paràmetres.

A Django, per exemple, podeu trobar que el `decorador de cache <http://docs.djangoproject.com/en/dev/topics/cache/>`_
admet paràmetres que ens permet dir-li durant quan de temps ha de cachejar els resultats, o el decorador
vary_on_headers, que ens permet modificar el contingut de la resposta de les vistes afegint les capçaleres que indiquem.

Anem a veure com ho podem aconseguir nosaltres. També hi ha dues maneres de fer-ho, la clara i la complexa.
La manera clara és la que recoman i utilitza una classe per a fer el decorador, la complexa requereix més esforça
per a entendre què està fent el decorador, és més curta, però personalment preferesc un codi més legible.

De la mateixa manera els decoradors que hem fet com a funcions es poden crear com a classes, però en aquest cas,
crec que la definició en forma de funcions és més bona de seguir, i ens permetrà distingir clarament entre els dos
tipus de decoradors: el que no admeten paràmetres que es construeixen preferentment mitjançant funcions i els que
admeten paràmetres, que es construeixen preferentment fent servir classes.

Per seguir amb el forat negre, ara el nostre exemple el que farà es mostrar el resultat o no segons li roti.
Per això el que farem serà passar-li una funció com a paràmetre que en ser executada determinarà si s'ha de mostrar
el resultat de la funció decorada o no


El mètode clar de fer decoradors amb arguments
-----------------------------------------------

Anem primer a veure l'exemple::

    #!python
    #!/usr/bin/env python
    # -*- coding: UTF-8 -*-
    import random

    class forat_negre_sonat(object):
        "Un decorador amb fam"
        def __init__(self, mostrar):
            self.mostrar = mostrar

        def __call__(self, f):
            def none(*args, **kw_args):
                if self.mostrar():
                    return f(*args, **kw_args)
                else:
                    return "Nop"
            return none

    @forat_negre_sonat(mostrar = lambda :random.choice((True, False)))
    def suma(a, b):
        "Suma dos elements que li passam com a paràmetre"
        return a+b


    if __name__=="__main__":
        print suma(2,3)
        print suma(5,6)
        print suma(9,5)


Fitxem-nos amb que hem fet:

1. Hem creat una classe Python que al seu constructor (l'__init__) agafa el paràmetre o paràmetres que vulguem.
   És un constructor normal, així que admet paràmetres per defecte per exemple.

2. Recordem que el decorador hem dit que ha de ser un objecte cridable (callable), a una classe, la cridabilitat
   la dóna el mètode \_\_call\_\_. Aquesta classe la  definirem de manera que agafi la funció a decorar com a paràmetre.
   D'aquesta manera tenim accés tant als paràmetres del decorador, que hem passat al constructor, com a la funció
   decorada, que hem passat com a paràmetre al call.

Després d'això ja sols en queda encapsular la cridada com ho fèiem al cas anterior, retornant el decorador en lloc
de la funció decorada.

A l'exemple el que he fet és mostrar que el paràmetre pot ser el que nosaltres vulguem, en concret he passat una
funció anònima, creada amb lambda que és la que s'encarrega d'establir l'aleatoritat del resultat.

Si voleu podem fer aquest decorador una mica més complet, fent que admeti a més de funcions valors i que preservi
el nom i documentació de la funció decorada.::

    #!/usr/bin/env python
    # -*- coding: UTF-8 -*-
    import random

    class forat_negre_sonat(object):
        "Un decorador amb fam"
        def __init__(self, mostrar=None):
            self.mostrar = mostrar

        def __call__(self, f):
            def none(*args, **kw_args):
                if callable(self.mostrar):
                    opcion = self.mostrar()
                else:
                    opcion = self.mostrar
                if opcion:
                    return f(*args, **kw_args)
                else:
                    return "Nop"
            none.__name__ = f.__name__
            none.__doc__ = f.__doc__
            return none

    @forat_negre_sonat(mostrar = lambda :random.choice((True, False)))
    def suma(a, b):
        "Suma dos elements que li passam com a paràmetre"
        return a+b

    @forat_negre_sonat(mostrar=True)
    def resta(a,b):
        return a-b


    if __name__=="__main__":
        print "Exemple amb %s " % suma.__name__
        print suma(2,3)
        print suma(5,6)
        print suma(9,5)
        print "Exemple amb %s " % resta.__name__
        print resta(2,3)
        print resta(5,6)

El mètode enrevessat de fer decoradors amb arguments
-----------------------------------------------------

El nostre exemple::

    def forat_negre_dos(mostrar):
        def wrap(f):
            @wraps(f)
            def wrapped_function(*args, **kw_args):
                if callable(mostrar):
                    opcion = mostrar()
                else:
                    opcion = mostrar
                if opcion:
                    return f(*args, **kw_args)
                else:
                    return "Nop"
            return wrapped_function
        return wrap

Bé, enrevessat, el que es diu enrevessat no ho és, per una cosa tan simple no té massa història, però fixau-vos que
és un poc més mal de seguir.

El primer que hem fet és definir la nostra funció, on hi hem posat els paràmetres que admet. Aquest funció retorna
una altra funció que admet un argument, que és la funció decorada, que a la seva vegada admet un nombre indeterminat
d'arguments (recordem que això ho estam forçant nosaltres).

Com que la segona funció, `wrapped_function` està definida dins `wrap`, té accés al paràmetre del decorador i pot
actuar en conseqüència.

Encadenant decoradors
---------------------

Els decoradors es poden encadenar, és a dir, una funció pot tener tans decoradors com faci falta i necessitem,
sols limitats pel nostre sentit comú i la legibilitat del programa. Dos decoradors són habituals, tres no es veuen
gaire, quatre o més són per pensar-s'ho.

Per a l'exemple manllevaré un dels decoradors més útils, el memoize, que ens permet cachejar una funció segons
els seus paràmetres. Al Python Decorator Library hi ha una implementació del patró memoize prou senzilla de seguir
amb el que ara sabem i a més ens servirà per completar la construcció de decoradors sense paràmetres fent servir
una classe.::

    
    class memoized(object):
       """Decorator that caches a function's return value each time it is called.
       If called later with the same arguments, the cached value is returned, and
       not re-evaluated.
       """
       def __init__(self, func):
          self.func = func
          self.cache = {}
       def __call__(self, *args):
          try:
             return self.cache[args]
          except KeyError:
             self.cache[args] = value = self.func(*args)
             return value
          except TypeError:
             # uncachable -- for instance, passing a list as an argument.
             # Better to not cache than to blow up entirely.
             return self.func(*args)
       def __repr__(self):
          """Return the function's docstring."""
          return self.func.__doc__


A diferència de la construcció amb paràmetres, al constructor de la classe memoized s'hi posa com a paràmetre
la funció a decorar, i al mètode __call__ hi van els paràmetres de la funció, en lloc de la funció a decorar
com es feia a l'altre mètode.

Per què s'ha fet servir aquesta manera si l'altra és més senzilla? Dons perquè necesitam mantenir en memòria
la caché i el que fa és mantenir-la en un diccionari dins de la mateixa classe. Si la caché fos externa
(amb memcached per exemple),això s'hauria pogut fer perfectament en forma de funció.

A més definirem un decorador que ens servirar per indicar quan entram a la funció i comprovar el decorador memoized::

    def log(f):
        "Registra l'execució de la funció"
        def wrap(*args):
            print "Excutant %s, args: %s" % \\
               (f.__name__, ",".join(str(x) for x in args))
            return f(*args)
        return wrap

    @memoized
    @log
    def fibonacci(n):
        "Return the nth fibonacci number."
        if n in (0, 1):
            return n
        return fibonacci(n-1) + fibonacci(n-2)

    print fibonacci(12)

Provau d'executar aquest codi amb i sense la funció memoized. Amb els dos decoradors activus veureu que el cada
decorador agafa com a entrada la funció ja decorada que surt del decorador que té més avall. Així el memoized agafa
com a entrada la funció fibonacci ja decorada amb el log.

Podeu fer la prova amb un exemple més simple::

    #!python
    #!/usr/bin/env python
    # -*- coding: UTF-8 -*-

    def uppercase(f):
        "Dada una función f que devuelve un string lo pasa todo a mayúsculas"
        def wrap():
            return f().upper()
        return wrap

    def make_bold(f):
        "Dada una función f que devuelve un string le añade los tags de bold"
        def wrap():
            return "<strong>%s</strong>" % f()
        return wrap

    @make_bold
    @uppercase
    def say_hello():
        return "Hello world"


    print say_hello()

Provau canviant l'ordre dels decoradors i veureu perfectament com es van aplicant els decoradors des de la funció per
amunt. A l'exemple primer es converteix el "Hello word" a majúscules i després se li apliquen els tags de negreta.


La signatura pendent
--------------------

Abans d'acabar ens queda un tema pendent: la signatura. Els decoradors que hem creat poden preservar el nom i la
documentació de la funció que decoren, però no preserven la signatura, és a dir, el nombre de paràmetres que li passam.

Michele Simionato ha escrit un mòdul excel·lent anomenat *decorator* que extén la utilizació dels decoradors,
mantén la signatura de la funció, el nom i la documentació, i a més ens dona la possibilitat de crear factories de
decoradors. Una eina per a tenir sempre a mà. Amb aquest mòdul podríem escriure el codi de l'exemple anterior com::

    #!python
    from decorator import decorator

    @decorator
    def uppercase(f, *args):
        "Donada una funció f que retorna un string ho passa a majúscules"
        return f(*args).upper()

    @decorator
    def make_bold(f, *args):
        "Afegeix el tag strong a la sortida de la funció"
        return "<strong>%s</strong>" % f(*args)

    @uppercase
    @make_bold
    def say_hello(nom):
        "Di hola, home!"
        return "Hello world %s" % nom

    if __name__=="__main__":
        from inspect import getargspec
        print say_hello('World')
        print say_hello.func_name
        print say_hello.__doc__
        print getargspec(say_hello)


Si executau el codi podem veure que no ens ha fet falta recore a wraps o a reasignar nom, la pròpia llibreria de
Simionato ho ha fet. A més, si ens fixam en la sortida de l'exemple::


    <STRONG>HELLO WORLD WORLD</STRONG>
    say_hello
    Di hola, home!
    ArgSpec(args=['nom'], varargs=None, keywords=None, defaults=None)

La primera línea correspon a la sortida de la funció que hem decorat. La segona és el nom d'aquesta funció. Ens surt
el nom de la funció original i no el del decorador. La documentació també s'ha mantingut i per acabar, podem veure
que la signatura de la funció és correcta, ens diu que té un argument obligatori anomenat nom.


Conclusió
---------

Esper haver deixat un poc més clar el tema dels decoradors. Crear-los no és difícil, utilitzar-los és simple,
sols hem de tenir clar què són i quan fer-los servir. Són una eina potent que ens permet fer el nostre codi més legible
i cohesionat. Fora por i a disfrutar amb els decoradors.

Com tot en aquesta vida, usau-los amb coneixement i moderació.



Referències
-----------

Per escriure aquest article m'he basat en múltiples fonts, les més importants i útils han estat:

* `PEP 318 <http://www.python.org/dev/peps/pep-0318>`_
* `Decorators I : Introduction to Python Decorators <http://www.artima.com/weblogs/viewpost.jsp?thread=240808>`_
* `Decorators II: Decorator Arguments <http://www.artima.com/weblogs/viewpost.jsp?thread=240845>`_
* `PYthon Decorators <http://wiki.python.org/moin/PythonDecorators>`_
* `Understanding decorators <http://uswaretech.com/blog/2009/06/understanding-decorators/>`_
* `Charming Python: Decorators make magic easy <http://www.ibm.com/developerworks/linux/library/l-cpdecor.html>`_
* `Decorator 3.1.2 <http://pypi.python.org/pypi/decorator/3.1.2 "Package to simplify decorators">`_
* `Decorator Pattern <http://en.wikipedia.org/wiki/Decorator_pattern>`_
* `Python decorator Library <http://wiki.python.org/moin/PythonDecoratorLibrary>`_