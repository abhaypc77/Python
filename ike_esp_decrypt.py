#!/bin/python
#version 1: Abhay-2017/9/29

'''
script to filter out ike and esp keys from main.log
and add them to wireshark table
'''

import argparse
import os

IKE_KEY_FILTER   = 'SECURITY IKE_KEY:'
ESP_KEY_FILTER = 'JuIpsecServer: Server Recv: {"ZIpsecCmd":"ZIpsecIpCmd","Cmd":"ip xfrm state add '

WIRESHARK_IKEV2_FILE  = '\Wireshark\ikev2_decryption_table'
WIRESHARK_ESP_SA_FILE = '\Wireshark\esp_sa'

ESP_AUTH_TABLE = {
'md5'        : '"HMAC-MD5-96 [RFC2403]"',
'sha1'       : '"HMAC-SHA-1-96 [RFC2404]"',
'sha384'     : '"HMAC-SHA-384-192 [RFC4868]"',
'sha512'     : '"HMAC-SHA-512-256 [RFC4868]"',
'sha256-128' : '"HMAC-SHA-256-128 [RFC4868]"',
'unkown'     : '"NULL"'
}

ESP_ENC_TABLE = {
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


def decrypt_esp(logfile):
  esp_keys_list = []
  with open(logfile, "r") as fobj:
    for line in fobj:
      if ESP_KEY_FILTER in line:
        esp_tokens = line.split(ESP_KEY_FILTER)[1].split(' ')
        src_ip = esp_tokens[1]
	dest_ip = esp_tokens[3]
	if ':' in src_ip:
          ip_type = '"IPv6"'
        else:
          ip_type = '"IPv4"'
        spi = esp_tokens[7]
        auth_type = ESP_AUTH_TABLE[esp_tokens[11]]
        auth_key = esp_tokens[12]
        enc_type = ESP_ENC_TABLE[esp_tokens[14]]
        enc_key = esp_tokens[15]
           
        esp_key = ip_type + ',' + '\"' + src_ip + '\"' + ',' + '\"' + dest_ip + '\"' + ',' + '\"' + spi + '\"' + ',' + \
                    enc_type + ',' + '\"' + enc_key + '\"' + ',' + auth_type + ',' + '\"' + auth_key + '\"' + '\n'
        esp_keys_list.append(esp_key)

  if len(esp_keys_list) > 0:
    add_in_wireshark_table(WIRESHARK_ESP_SA_FILE, esp_keys_list)


def parse_arg():
  parser = argparse.ArgumentParser()
  parser.add_argument('opt_args', nargs='*', help='To Decrypt IKE and ESP Logs')

  return parser.parse_args()


def main():
  args = parse_arg()

  #currenlty we are considering only 'main.log' file and assuming it to be in current directory
  logfile = 'main.log'

  if len(args.opt_args) > 0:
    for decrypt in args.opt_args:
      if decrypt == 'ike':
        decrypt_ike(logfile)
      elif decrypt == 'esp':
        decrypt_esp(logfile)
  else:
    decrypt_ike(logfile)
    decrypt_esp(logfile)


if __name__ == '__main__':
  main()
