# freerad-lab

Get a WPA2-Enterprise 802.1X SSID/network up; using EAP-TLS...in as fast as possible.

## Requirements
Docker.

## TLDR;
The one-liner is this:
```
docker run -p 1812:1812/udp -it mike909/freeradius3:v1 freeradius -X
```
Use the included "useratexample.org.pfx" certificate in your Android or other clients.

Use the included "foo.bar" for OSX.
