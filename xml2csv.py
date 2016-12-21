#!/usr/bin/python2.7
from xml.dom import minidom
xml_documento = minidom.parse('xml.xml')
lista = xml_documento.getElementsByTagName('row')
for nodo in lista:
    number = nodo.getAttribute("c1")
    geometry = nodo.getAttribute("c7")
    csv = number + ',' + geometry
    print(csv)
