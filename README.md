# freerad-lab

Get a WPA2-Enterprise 802.1X SSID/network up; using EAP-TLS...in as fast as possible.

## Requirements
Docker.

## TLDR;
The one-liner is this:
```
docker run -it -p 1812-1813:1812-1813/udp --mount type=bind,source=$PWD,target=/mnt/hostdir mike909/freerad-lab:v1
```
Use the included "test-freerad-eaptls" .1X provile for OSX.

Use the included "useratexample.org.pfx" certificate in your Android or other clients.

## How to use this/What to modify to meet your needs
Step 1. Clone this repo.

Step 2. You only need to modify constants.py like so:

* TARGETIP Change this to match your gNMI Target (openconfig.mist.com or Arista AP IP)
* PORT = Change this to match your gNMI Targets TCP Port.
* USER = Change this to match your gNMI Username. (Arista AP default is admin)
* PASSWORD Change this to match your gNMI Password. (Arista AP default is admin)
* APMAC = Change this to your APs MAC address.
* APNAME = Change this to whatever you want your APs hostname to be.
* WORKSTATIONIP = Change this to your laptops IP. This will be your RADIUS Server.

Your workstations will also be running FreeRADIUS.

Step 3. Run the above 'docker run' command (See TLDR;)

## What's happening in the background
When you 'run' the above docker run command, the following takes place on your machine:
* RADIUS ports 1812|3 are forwarded through your host to the Docker container (named freerad-lab)
* Your current directory is mounted inside the Docker container, as /mnt/hostdir
* Upon instantiation, the container provisions your AP; eg assigns the hostname & country-code to the MAC address.
* Next, the container configures your AP with both an OPEN and a WPA2-Enterprise SSID.
* You can connect to the WPA2-Enterprise SSID (test_wpa2ent), using EAP-TLS. The certificate is "useratexample.org.pfx". This can be added to your Android or other device.

Note, some devices require the pfx certificate to be converted. If your using OSX, this has already been done for you; and you can install "test-freerad-eaptls.mobileconfig" (just double click it).

If you want to modify the container so it doesn't provision or configure your AP when it starts, simple modify "runner.py" (see main function at bottom.)
