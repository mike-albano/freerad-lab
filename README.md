# freerad-lab

Get a WPA2-Enterprise 802.1X SSID/network up; using EAP-TLS...in as fast as possible.

## Requirements
Docker.

## TLDR;
The one-liner is this:
```
docker run -it -p 1812-1813:1812-1813/udp --mount type=bind,source=$PWD,target=/mnt/hostdir freerad-lab
```
Use the included "test-freerad-eaptls" .1X provile for OSX.

Use the included "useratexample.org.pfx" certificate in your Android or other clients.

## How to use this/What to modify to meet your needs
Step 1. Clone this repo.

Step 2. You only need to modify constants.py like so:

* TARGETIP Change this to match your gNMI Target.
* PORT = Change this to match your gNMI Targets TCP Port.
* USER = Change this to match your gNMI Username.
* PASSWORD Change this to match your gNMI Password.
* APMAC = Change this to your APs MAC address.
* APNAME = # Change this to whatever you want your APs hostname to be.
* WORKSTATIONIP = Change this to your laptops IP. This is RADIUS Server.

Your workstations will also be running FreeRADIUS.

Step 3. Run the above 'docker run' command (See TLDR;)

## What's happening in the background
When you 'run' the above docker run command, the following takes place on your machine:
* RADIUS ports 1812|3 are forwarded through your host to the Docker container (named freerad-lab)
* Your current directory is mounted inside the Docker container, as /mnt/hostdir
* Upon instantiation, the container provisions your AP; eg assigns the hostname & country-code to the MAC address.
* Next, the container configures your AP with both an OPEN and a WPA2-Enterprise SSID.
* You can connect to the WPA2-Enterprise SSID, using EAP-TLS. The certificate is "useratexample.org.pfx". This can be added to your Android or other device.

Note, some devices require the pfx certificate to be converted. If your using OSX, this has already been done for you; and you can install "test-freerad-eaptls.mobileconfig" (just double click it).
