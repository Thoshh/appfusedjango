Turistec ha presentat recentment la iniciativa [CAVAL](http://caval.travel) com una seria d'especificacions
per promoure la interoperabilitat de dades entre solucions TIC per al sector turístic.

Aquestes especificacions tenen una [implementació de referència](http://test.viajesurbis.com/caval/) a la web de 
proves de Viajes Urbis, on podem trobar la documentació, l'API de Java, els WSDL, els *endpoints* per REST i
una plana de proves que ens permet testejar el nostre client contra l'especifiació d'Urbis. 

Es d'agraïr l'especificació de referència d'Urbis, però la veritat, crec que estaria molt millor com a iniciativa de
Caval i no deixar l'especificació de referència a una web separada del domini principal. Tal com està pareix com si
s'hagués acabat la subvenció i no es pogués pagar el hosting o el desenvolupament. A més es podria posar el codi de 
la implementació a la web, donant la possibilitat de que la gent hi faci aportacions, encara que fos Caval l'entitat
encarregada de certificar finalment la solució.

Ara és cosa de no deixar-ho morir, falta una implementació real de referència (podria ser la d'Urbis però amb la
marca Caval), el codi font d'aquesta, poder tenir accés al codi des d'un control de versions i per què no poder
participar amb aportacions i correcció d'errors. En la implementació de referència crec que es tindria que tenir en
compte que la majoria de possibles consumidors de l'especificació són petites i mitjanes empreses. Això vol dir
fugir d'implementacions de referència que requereixin grans instal·lacions o coneixements tècnics avançats, la 
implementació ha de tenir un nivell d'entrada molt suau, amb pocs requeriments de servidor, de tal manera que
es pugui tocar molt ràpidament.

No sé si arribaré a fer una implementació de referència en Python, potser seria un bon exercici per futurs creant-bits,
però el que sí es pot fer és comença a jugar amb el que té Urbis.

Per això farem servir [Suds](https://fedorahosted.org/suds/), com que estam de proves, en lloc de la llibreria recomanada
farem servir la beta. Suds és una llibreria per a consumir serveis webs SOAP. A diferència d'altres eines com [ZSI](http://pywebsvcs.sourceforge.net/) no genera codi, sinó que construeix els objectes al vol.

Anem per feina!

El primer que farem es descarregar la beta i instal·lar-la al nostre entorn. En el meu cas faré servir un virtualenv de
manera que no tendré dependències amb altres paquets. 

Com que volem veure les cridades que es generen establirem el nivell de login de Suds a DEBUG

    import logging
    logging.basicConfig(level=logging.INFO)
    
    logging.getLogger('suds.client').setLevel(logging.DEBUG)


Per a fer les proves mapejarem el servei d'Hotels, que té per url `http://test.viajesurbis.com/serveis/caval/20091127/soap/HotelBookingService?wsdl`

    from suds.client import Client
    
    url = "http://test.viajesurbis.com/serveis/caval/20091127/soap/HotelBookingService?wsdl"
    client = Client(url)
    
ara podem fer un `print client` per tenir l'estructura de mapeig que ha fet Suds, 


    Suds ( https://fedorahosted.org/suds/ )  version: 0.3.8 (beta)  build: R627-20091211

    Service ( HotelBookingService ) tns="http://caval.travel/20091127/hotelBooking"
       Prefixes (1)
          ns0 = "http://caval.travel/20091127/hotelBooking"
       Ports (1):
          (HotelBookingServicePort)
             Methods (6):
                confirmHotelBooking(cavalHotelBookingConfirmRQ rq, )
                getAvailableHotels(cavalHotelAvailabilityRQ rq, )
                getDetailedValuation(cavalHotelBookingValuationRQ rq, )
                getEstablishmentDataSheets(cavalGetEstablishmentDataSheetsRQ rq, )
                getOffersList(cavalGetOffersListRQ arg0, )
                notifyHotelBookings(cavalHotelBookingNotificationRQ arg0, )
             Types (52):
                abstractAuthenticatedAgencyRQ
                abstractAuthenticatedRQ
                abstractRS
                ...
                roomOccupation
                roomType
                supplement
                valuatedLine
                valuatedOccupation
                zoneWithOffers
               
                
Fitxau-vos que ens està donant els mètodes del web service i els tipus que hi ha definits.

Per tractar amb arguments simples no necessitam gaire cosa més. Podríem cridar als mètodes directament. El problema
és que els arguments no són simples, així que tendrem que crear-los així com els necessitem.

Per a les nostres proves farem utilitzarem `getAvailableHotels`, com que a la web d'Urbis hi tenim [un client web](http://test.viajesurbis.com/caval/wsstaio/test/index.html) ens anirà bé per validar el que feim.

Cream l'objecte que contindrà la petició:

    rq = client.factory.create('cavalHotelAvailabilityRQ')
    
si feim un `dir(rq)` podrem veure les propietats que té l'objecte
    
    In [11]: dir(rq)
    Out[11]: 
    ['__contains__',
     '__delattr__',
     '__doc__',
     '__getitem__',
     '__init__',
     '__iter__',
     '__keylist__',
     '__len__',
     '__metadata__',
     '__module__',
     '__printer__',
     '__repr__',
     '__setattr__',
     '__setitem__',
     '__str__',
     '__unicode__',
     'agentId',
     'airportIds',
     'boardGroupFilter',
     'checkIn',
     'checkOut',
     'cityIds',
     'establishmentClassificationFilter',
     'establishmentIds',
     'establishmentNameFilter',
     'excludeOnRequest',
     'fromRow',
     'gzipResponse',
     'hotelCategoryGroupFilter',
     'language',
     'login',
     'numRows',
     'occupations',
     'onlyOffers',
     'password',
     'removeHotelInfo',
     'roomGroupFilter',
     'rqId',
     'stateIds']

Que podem comparar amb l'exemple de la web d'Urbis

    <?xml version="1.0" encoding="UTF-8"?>
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
    xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <soapenv:Body>
        <getAvailableHotels xmlns="http://caval.travel/20091127/hotel">
          <rq xmlns="">
            <login>xml</login>
            <password>xml</password>
            <agentId>1</agentId>
            <language>es</language>
            <gzipResponse>false</gzipResponse>
            <stateIds>569061</stateIds>
            <checkIn>01/1/2010</checkIn>
            <checkOut>05/1/2010</checkOut>
            <occupations>
              <adultsPerRoom>2</adultsPerRoom>
              <childrenPerRoom>0</childrenPerRoom>
              <numberOfRooms>1</numberOfRooms>
            </occupations>
    <removeHotelInfo>false</removeHotelInfo>
          </rq>
        </getAvailableHotels>
      </soapenv:Body>
    </soapenv:Envelope>

Però a més Suds ens dóna més informació damunt els paràmetres que el propi `dir`, així si feim un `print rq`


    In [13]: print rq
    -------> print(rq)
    (cavalHotelAvailabilityRQ){
       gzipResponse = None
       login = None
       password = None
       rqId = None
       agentId = None
       language = None
       airportIds[] = <empty>
       boardGroupFilter[] = <empty>
       checkIn = None
       checkOut = None
       cityIds[] = <empty>
       establishmentClassificationFilter[] = <empty>
       establishmentIds[] = <empty>
       establishmentNameFilter = None
       excludeOnRequest = None
       fromRow = None
       hotelCategoryGroupFilter[] = <empty>
       numRows = None
       occupations[] = <empty>
       onlyOffers = None
       removeHotelInfo = None
       roomGroupFilter[] = <empty>
       stateIds[] = <empty>
     }

Podem veure que ens dóna també informació sobre els objectes i sobre els alguns d'ells són col·leccions, llistes Python.

Assignem-hi valors:

    rq.login = 'xml'
    rq.password = 'xml'
    rq.agentId = 1
    rq.language = 'es'
    rq.gzipResponse='false'
    rq.stateIds=569061
    rq.checkIn='01/01/2010'
    rq.checkOut='05/01/2010'
    
Arribam ara a l'ocupació, aquí s'espera una llista del tipus `availRQOccupation` així que l'hem de crear l'objete primer
tal com he fet abans al la petició

    room = client.factory.create('availRQOccupation')
    room.adutlsPerRoom = 2
    room.childrenPerRoom = 0
    room.numberOfRooms = 1
    rq.removeHotelInfo ='true'
    client.service.getAvailableHotels(rq)
    
Si heu seguit els passos fins aquí veureu el log amb el SOAP-XML que s'ha generat, i que falla miserablement amb un error:
    
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body><soap:Fault><faultcode>soap:Client</faultcode>
    <faultstring>Unmarshalling Error: com/sun/xml/bind/v2/runtime/reflect/opt/Const </faultstring>
    </soap:Fault></soap:Body></soap:Envelope>

Dont' panic!

Si comparam el que hem enviat (per això tenim el log a DEBUG) i ho comparam amb l'exemple que ens dóna Urbis veim que
estam enviant tags buids i això a la implementació d'Urbis pareix que no li agrada gens

Com que Suds fa la generació automàticament pareix que ho tenim un tant pelut, però no és així, supòs que Suds (si no
ho ha fet ja) potser algun dia posarà l'opció de no generar tags buids, o potser la gent d'Urbis corregirà la implementació
de referència per no petar amb aquests tags (que hauríen de ser vàlids, per una altra banda), però mentre és el que
tenim, així que com a pas previ abans d'enviar-ho el que farem serà eliminar de la petició els atributs que estan
buids.


    for attr in dir(rq):
        if not attr.startswith('_') and not getattr(rq, attr): delattr(rq,attr)

si imprimirm el `rq` ara


    (cavalHotelAvailabilityRQ){
       gzipResponse = "false"
       login = "xml"
       password = "xml"
       agentId = 1
       language = "es"
       checkIn = "01/01/2010"
       checkOut = "05/01/2010"
       occupations[] = 
          (availRQOccupation){
             adultsPerRoom = 2
             childAges[] = <empty>
             childrenPerRoom = 0
             numberOfRooms = 1
          },
       removeHotelInfo = "true"
       stateIds = 569061
     }

Si ara ho tornam a enviar veurem que torna a pegar una petada, però aquest cop si ens fixam ens retorna la
resposta, la petada diu

    ERROR: An unexpected error occurred while tokenizing input
    The following traceback may be corrupted or invalid
    The error message is: ('EOF in multi-line statement', (129, 0))

Al tips de Suds ens avisa que alguns servidor posen caràcters de control a la responsta que fan que el parsejador
SAX que fa servir Suds doni una excepció (ara ja sabeu perquè la gent fa una rialla d'aquelles d'incredulitat
quan li dus que la S de SOAP ve de Simple), per això el permet Suds és afegir-hi un filtre a la resposta

    import string
    from suds.bindings.binding import Binding
    Binding.replyfilter = (lambda s,r: ''.join([c for c in r if c in string.printable]))

Ara sí:

    rs = client.service.getAvailableHotels(rq)
    print rs.totalRows
    
En el meu cas m'han sortit 76 hotels. Si feim un `print rs` en veurem l'estructura de dades, i amb un dir(rs) les
propietats i mètodes que tenim disponibles, ens fixam amb `availableEstablishments`

A partir d'aquí ja és sols cosa d'anar accedint als distints elements de l'estructura i decidir com presentam
la informació que hem obtingut. Per exemple i per no fer-me massa llarg, per imprimir els noms dels hotels que 
hem trobat basta fer:

    for hotel in rs.availableEstablishments:
        print hotel.establishmentName

Per acabar, si us demanau pel rendiment d'això, heu de saber que Suds manté el WSDL en caché, de manera que no
necessita demanar-lo cada vegada. La caché és configurable.

Pel nostre exemple, la disponibilitat de la tenim en poc més de 3 segons.

    2009-12-16 20:07:36,179-INFO-__main__-36-Iniciam la consulta
    2009-12-16 20:07:39,215-INFO-__main__-38-Fi de la consulta

Considerant que en el entorn de test via web d'URBIS la resposta l'obtenim entre 10 i 14 segons, doncs jo dira que 
està d'allò més bé.
    

Pos tot el codi per a que sigui més fàcil fer les proves:

    #!/usr/bin/env python
    # -*- coding: UTF-8 -*-

    import logging
    logging.basicConfig(level=logging.INFO,
            format="%(asctime)s-%(levelname)s-%(name)s-%(lineno)s-%(message)s",)
    logging.getLogger('suds.client').setLevel(logging.INFO)
    log = logging.getLogger(__name__)
    
    from suds.client import Client
    import string
    
    from suds.bindings.binding import Binding
    # Com que la resposta té problemes filtram 
    Binding.replyfilter = (lambda s,r: ''.join([c for c in r if c in string.printable]))
    
    url = "http://test.viajesurbis.com/serveis/caval/20091127/soap/HotelBookingService?wsdl"

    client = Client(url)
    rq = client.factory.create('cavalHotelAvailabilityRQ')
    rq.login = 'xml'
    rq.password = 'xml'
    rq.agentId = 1
    rq.language = 'es'
    rq.gzipResponse='false'
    rq.stateIds=569061
    rq.checkIn='01/01/2010'
    rq.checkOut='05/01/2010'
    room = client.factory.create('availRQOccupation')
    room.adultsPerRoom = 2
    room.childrenPerRoom = 0
    room.numberOfRooms = 1
    rq.occupations = (room, )
    rq.removeHotelInfo ='true' # no volem informació de l'hotel ara
    
    # bug? de la implementació de referencia, eliminam tags buids.
    for attr in dir(rq):
        if not attr.startswith('_'):
            if not getattr(rq, attr): delattr(rq,attr)
        
    log.info('Iniciam la consulta')
    rs = client.service.getAvailableHotels(rq)
    log.info('Fi de la consulta')
    # i la llista d'hotels
    for hotel in rs.availableEstablishments:
        print hotel.establishmentName    

