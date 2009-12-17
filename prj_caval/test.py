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

url = "http://test.viajesurbis.com/serveis/caval/20091127/soap/HotelBookingService?wsdl"

client = Client(url)
#client.set_options(proxy={'http': 'localhost:8080'})
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
rq.removeHotelInfo ='true'
for attr in dir(rq):
    if not attr.startswith('_'):
        if not getattr(rq, attr): delattr(rq,attr)

Binding.replyfilter = (lambda s,r: ''.join([c for c in r if c in string.printable]))
log.info('Iniciam la consulta')
rs = client.service.getAvailableHotels(rq)
log.info('Fi de la consulta')
#for hotel in rs.availableEstablishments:
#    print hotel.establishmentName
