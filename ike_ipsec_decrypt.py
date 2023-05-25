#!/bin/python

'''
script to filter out ike and ipsec keys from main.log
and add them to wireshark table
'''

import argparse
import os

IKE_KEY_FILTER   = 'SECURITY IKE_KEY:'
IPSEC_KEY_FILTER = 'JuIpsecServer: Server Recv: {"ZIpsecCmd":"ZIpsecIpCmd","Cmd":"ip xfrm state add '

WIRESHARK_IKEV2_FILE  = '\Wireshark\ikev2_decryption_table'
WIRESHARK_ESP_SA_FILE = '\Wireshark\esp_sa'

IPSEC_AUTH_TABLE = {
'md5'        : '"HMAC-MD5-96 [RFC2403]"',
'sha1'       : '"HMAC-SHA-1-96 [RFC2404]"',
'sha384'     : '"HMAC-SHA-384-192 [RFC4868]"',
'sha512'     : '"HMAC-SHA-512-256 [RFC4868]"',
'sha256-128' : '"HMAC-SHA-256-128 [RFC4868]"',
'unkown'     : '"NULL"'
}

IPSEC_ENC_TABLE = {
'aes'         : '"AES-CBC [RFC3602]"',
'des'         : '"DES_CBC [RFC2045]"',
'des3_ede'    : '"TripleDES-CBC [RFC2451]"',
'cast5'       : '"CAST5-CBC [RFC2144]"',
'blowfish'    : '"BLOWFISH-CBC [RFC2451]"',
'cipher_null' : '"NULL"'
}


def add_in_wireshark_table(wireshark_file, decryption_keys):
  wiresahrk_table = os.getenv('APPDATA') + wireshark_file
  with open(wiresahrk_table, 'r') as table_obj:
    keys_in_table = table_obj.readlines() 
    for key in decryption_keys:
      print 'Adding key : {}'.format(key)
      if key in keys_in_table:
        print 'key already exist'
        continue
      else:
        keys_in_table[1:1] = key

  with open(wiresahrk_table, 'w') as table_obj:
    table_obj.writelines(keys_in_table)  
    print 'Keys updated successfully'


def decrypt_ike(logfile):
  ike_keys_list = []
  with open(logfile, "r") as fobj:
    for line in fobj:
      if IKE_KEY_FILTER in line:
        ike_keys_list.append(line.split(IKE_KEY_FILTER)[1])

  if len(ike_keys_list) > 0:
    add_in_wireshark_table(WIRESHARK_IKEV2_FILE, ike_keys_list)


def decrypt_ipsec(logfile):
  ipsec_keys_list = []
  with open(logfile, "r") as fobj:
    for line in fobj:
      if IPSEC_KEY_FILTER in line:
        ipsec_tokens = line.split(IPSEC_KEY_FILTER)[1].split(' ')
        src_ip = ipsec_tokens[1]
	dest_ip = ipsec_tokens[3]
	if ':' in src_ip:
          ip_type = '"IPv6"'
        else:
          ip_type = '"IPv4"'
        spi = ipsec_tokens[7]
        auth_type = IPSEC_AUTH_TABLE[ipsec_tokens[11]]
        auth_key = ipsec_tokens[12]
        enc_type = IPSEC_ENC_TABLE[ipsec_tokens[14]]
        enc_key = ipsec_tokens[15]
           
        ipsec_key = ip_type + ',' + '\"' + src_ip + '\"' + ',' + '\"' + dest_ip + '\"' + ',' + '\"' + spi + '\"' + ',' + \
                    enc_type + ',' + '\"' + enc_key + '\"' + ',' + auth_type + ',' + '\"' + auth_key + '\"' + '\n'
        ipsec_keys_list.append(ipsec_key)

  if len(ipsec_keys_list) > 0:
    add_in_wireshark_table(WIRESHARK_ESP_SA_FILE, ipsec_keys_list)


def parse_arg():
  parser = argparse.ArgumentParser()
  parser.add_argument('opt_args', nargs='*', help='To Decrypt IKE and IPSEC Logs')

  return parser.parse_args()


def main():
  args = parse_arg()

  #currenlty we are considering only 'main.log' file and assuming it to be in current directory
  logfile = 'main.log'

  if len(args.opt_args) > 0:
    for decrypt in args.opt_args:
      if decrypt == 'ike':
        decrypt_ike(logfile)
      elif decrypt == 'ipsec':
        decrypt_ipsec(logfile)
  else:
    decrypt_ike(logfile)
    decrypt_ipsec(logfile)

  print 'Press any key to Exit...'
  userInput = raw_input()  
	

if __name__ == '__main__':
  main()

