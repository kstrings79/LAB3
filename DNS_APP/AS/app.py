import socket
import json

HOST = '0.0.0.0'
PORT = 53533

dns_records = {}

def register(name, value, type, ttl):
    key = f'{name}#{type}'
    dns_records[key] = {'value': value, 'ttl': ttl}

def get_record(name, type):
    key = f'{name}#{type}'
    if key in dns_records:
        return dns_records[key]
    return None

def handle_udp_request(data, addr):
    request = json.loads(data)
    name = request['name']
    type = request['type']
   




