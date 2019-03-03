import json, constants, subprocess

TARGET = constants.TARGETIP
USER = constants.USER
PASSWORD = constants.PASSWORD
PORT = constants.PORT
APMAC = constants.APMAC
APNAME = constants.APNAME
WORKSTATIONSIP = constants.WORKSTATIONIP

def mod_jsons():
  """Modifies JSON files according to whats in constants.py"""
  # Provision JSON.
  prov_json = json.load(open( '/mnt/hostdir/oc_provision.json', 'r'))
  prov_json['openconfig-ap-manager:mac'] = APMAC
  prov_json['openconfig-ap-manager:config']['mac'] = APMAC
  prov_json['openconfig-ap-manager:config']['hostname'] = APNAME

  f = open('oc_provision_new.json', 'w')
  f.write(json.dumps(prov_json))
  f.close()
  # Configuration JSON.
  conf_json = json.load(open('/mnt/hostdir/oc_config_1x.json', 'r'))
  conf_json['system']['aaa']['server-groups']['server-group'][0]['servers'][
    'server'][0]['address'] = WORKSTATIONSIP
  conf_json['system']['aaa']['server-groups']['server-group'][0]['servers'][
    'server'][0]['config']['address'] = WORKSTATIONSIP
  conf_json['hostname'] = APNAME
  f = open('oc_config_1x_new.json', 'w')
  f.write(json.dumps(conf_json))
  f.close()

def config_ap():
  """Provision and configure the AP."""
  # Provision the AP.
  if 'mist' in TARGET:
    subprocess.call('python /gnxi/gnmi_cli_py/py_gnmicli.py -t %s -p %s -m'
                    'set-update -x /provision-aps/provision-ap[mac=%s] '
                    '-user %s -pass %s -val @oc_provision_new.json' % (
                    TARGET, PORT, APMAC, USER, PASSWORD), shell=True)
    # Configure the AP.
    subprocess.call('python /gnxi/gnmi_cli_py/py_gnmicli.py -t %s -p %s -m'
                    'set-update -x /access-points/access-point[hostname=%s] '
                    '-user %s -pass %s -val @oc_config_1x_new.json' % (
                    TARGET, PORT, APNAME, USER, PASSWORD), shell=True)
    return
  # Not mist; assuming Arista. Change these options dependong on vendor.
  subprocess.call('python /gnxi/gnmi_cli_py/py_gnmicli.py -t %s -p %s -m'
                  'set-update -x /provision-aps/provision-ap[mac=%s] '
                  '-user %s -pass %s -val @oc_provision_new.json -g -o'
                  ' openconfig.mojonetworks.com' % (TARGET, PORT, APMAC, USER,
                                                    PASSWORD), shell=True)
  # Configure the AP.
  subprocess.call('python /gnxi/gnmi_cli_py/py_gnmicli.py -t %s -p %s -m'
                  'set-update -x /access-points/access-point[hostname=%s] '
                  '-user %s -pass %s -val @oc_config_1x_new.json -g -o'
                  ' openconfig.mojonetworks.com' % (TARGET, PORT, APNAME, USER,
                                                    PASSWORD), shell=True)

def start_radius():
  """Starts FreeRADIUS in debug mode"""
  # Replace "-X" with "-f" to run in foreground mode instead of Debug mode.
  subprocess.call('freeradius -X', shell=True)  # Start FreeRADIUS.

if __name__ == '__main__':
  # Comment out next two lines if you only want to run FreeRADIUS server.
  mod_jsons()  # Modifies JSON files according to what you put in constants.py.
  config_ap()  # This both provisions and configures AP with WPA2-Ent/EAP-TLS.
  start_radius()
