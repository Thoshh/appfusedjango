Abans de començar
=================

Appfusedjango és un conjunt de troços de codi, exemples i experiments que anat
fent al llarg del temps i que pos a un repositori public per si poden servir
a algú més.

A cada directori hi ha un projecte complet en ell mateix. Per a posar-ho
en marxa (llevat de que s'indiqui el contrari a la documentació del projecte o
que m'hagi oblidat de documentar-ho) s'ha de copiar/reanomenar el arxius
que acaben amb l'extensió *.template* i configurar-los segons les nostres necessitats. 

En molts casos el document reanomenat ja ens servirà per poder executar l'exemple, però
tot i això convé fer-hi sempre una repassada.

Alguns exemples duen la BD ja creada, alguns no. Si no hi ha base de dades s'ha
crear amb::

    python manage.py syncdb

contestant a les preguntes. Normalment per als exmples utilitz com a usuari
*demo* i com a clau *demo*.