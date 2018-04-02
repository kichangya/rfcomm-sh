from bluetooth import *

print "\n".join( [ "%s-%s" % (addr,lookup_name(addr)) for addr in discover_devices() ] )

