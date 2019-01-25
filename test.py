import zeep
import xml.dom.minidom

wsdl = 'http://sparkgatetest.interfax.ru/iFaxWebService/iFaxWebService.asmx?WSDL'
client = zeep.Client(wsdl=wsdl)

print('Time:', client.service.Time())

rusult = client.service.Authmethod('LeruaGate', 'TdMfEte')
print('Authmethod:', rusult)

if rusult == 'True':
    result = client.service.GetCompanyExtendedReport(sparkId='', inn='7736577914', ogrn='')
    if result.GetCompanyExtendedReportResult:
        print("xmlData:", result.xmlData)
    client.service.End()
    dom = xml.dom.minidom.parseString(result.xmlData)
    print(dom.toprettyxml())

print(client.service.End())


