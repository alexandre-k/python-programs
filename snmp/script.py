from pysnmp.hlapi import *
from pysnmp.proto import rfc1902

transport = UdpTransportTarget(('45.32.13.245',161))
comm_data=UsmUserData('laozi','MeiPeiYoh3','MeiPeiYoh3')
data = (
        ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr',0)),
        )
data_set = ((1,3,6,1,2,1,1,1,0), rfc1902.OctetString('new system'))

result = setCmd(
            SnmpEngine(),
            comm_data,
            transport,
            ContextData(),
            data_set
            )

for errorIndication, errorStatus, errorIndex, varBinds in result:

    if errorIndication:
        print(errorIndication.prettyprint())
    elif errorStatus:
        print(errorStatus.prettyPrint())
    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))
