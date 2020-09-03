# zeroconfutilities
Zeroconf/Bonjour Utilities for discovering available zeroconf/bonjour services on your local network.

## List Services
Executing the script *listservices.py* will list all available zeroconf services on your local network, e.g. *_airplay._tcp.local.*, *_http._tcp.local.*, etc. Use the tool *browseservice.py* to get more information on what is using the specific service.

```bash
  python listservices.py
```

## Browse a Service
Executing the script *browseservice.py* will scan the network for the specified service (supplied as argument, see example below) for information and print it to the console.

```bash
  python browseservice.py _http._tcp.local.
```
