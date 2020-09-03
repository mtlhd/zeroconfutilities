import sys
from zeroconf import ServiceBrowser, Zeroconf

class MyListener:

    def remove_service(self, zeroconf, type, name):
        print("Service %s removed" % (name,))

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        print("Service %s added, service info: %s" % (name, info))

try:
    arg = sys.argv[1]
except IndexError:
    raise SystemExit("Usage: {sys.argv[0]} <service to browse>")

zeroconf = Zeroconf()
listener = MyListener()
browser = ServiceBrowser(zeroconf, arg, listener)
try:
    input("Press enter to exit...\n\n")
finally:
    zeroconf.close()