from pysnmp.hlapi import *

transport = UdpTransportTarget(('45.32.13.245',161))
comm_data=UsmUserData('laozi','MeiPeiYoh3','MeiPeiYoh3')
data = (
        ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysObjectID',0)),
        )

errorIndication, errorStatus, errorIndex, varBinds = nextCmd(
            SnmpEngine(),
            comm_data,
            transport,
            ContextData(),
            *data
            )

if errorIndication:
    print(errorIndication)
elif errorStatus:
    print(errorStatus)
else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))
