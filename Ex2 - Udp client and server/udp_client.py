from socket import socket, AF_INET, SOCK_DGRAM
from collections import defaultdict
import time

start_time = time.time()

class Cache:
    TYPE = 0
    VALUE = 1
    TTL = 2

def insertToCache(toCache):
    for lst in cache[toCache[0]]:
        if lst[Cache.TYPE].upper() == toCache[1].upper():
            cache[toCache[0]].remove(lst)
            break
    cache[toCache[0]].append(toCache[1:])

def clientCache(data):
    print "looking in client cache"
    data = data.split(' ')
    key = data[0] #bob.com NS
    requestType = data[1]
    if key in cache:
        value = cache[key]  ### the type, ip and TTL for the site/siyomet
        for x in value:
            if x[Cache.TYPE] == requestType:
                # NEED TO CHECK TTL AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                if (time.time()) < start_time + int(x[Cache.TTL]):
                    return key + ' ' + " ".join(x)
                else:
                    cache[key].remove(x)
    return False

class Ports:
    LOCAL = 12100
    ROOT = 12000

cache = defaultdict(list)

print "a"
s = socket(AF_INET, SOCK_DGRAM)
dest_ip = '127.0.0.1'
dest_port = Ports.LOCAL
msg = raw_input("Message to send: ")
while not msg == 'quit':
    if len(msg.split(' ')) < 2:
        print "Not accepted request. need 2 args"
        msg = raw_input("Message to send: ")
        continue
    answer = clientCache(msg)
    if answer != False:
        print answer
    else:
        s.sendto(msg, (dest_ip,dest_port))
        data, _ = s.recvfrom(2048)
        print "Server sent: ", data
        insertToCache(data.split(' '))

    msg = raw_input("Message to send: ")
s.close()
