from bluetooth import *

for addr in discover_devices():
    print addr, lookup_name(addr)
    services = find_service(address = addr)
    for ser in services:
        print ser,"\n"
