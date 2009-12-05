Eines
=====

Al directori *tools* hi ha petites utilitats que ens fan la vida més senzilla
a l'hora de fer aplicacions.

correu.py
---------

Es un servidor de correu smtp mínim. En lloc d'enviar el missatge el que
fa és deixar-ho a un arxiu que podrem consultar després, per exemple obrint-lo
amb el nostre client de correu preferit i veure com queda.

Per a executar-lo, i donat que per defecte s'executa a un prot privilegiat
és necessari tener privilegis de root. 

console.py
----------

Posat al nostre projecte ens permet crear fàcilment comandes que estan 
integrades amb Django.

Amb la incorporació a Django de un mètodo per crear comandes i gestionar-les
des de el manager aquesta utilitat no té tant de sentit, però tot i això
ens pot servir per fer aplicacions de consola que integrin tant una aplicació
Django com altres utilitats.