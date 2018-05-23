from socket import socket, AF_INET, SOCK_DGRAM
import string
from collections import defaultdict
import time

start_time = time.time()

#root
#com
#google
#local
server_name = "local"

class Mapping:
    KEY = 0
    TYPE = 1
    VALUE = 2
    TTL = 3

class Ports:
    ROOT = 12000
    LOCAL = 12100
    COM = 12351
    google = 12380
    facebook = 12353
    subFacebook = 12354

class Cache:
    TYPE = 0
    VALUE = 1
    TTL = 2
def port(name):
    name = name.lower()
    if name == "root":
        return Ports.ROOT
    if name == "com":
        return Ports.COM
    if name == "local":
        return Ports.LOCAL
    if name == "google":
        return Ports.google
    if name == "facebook":
        return Ports.facebook
    if name == "subFacebook":
        return Ports.subFacebook

#Connect to other server
def connect_to_server(value, msg):
    s = socket(AF_INET, SOCK_DGRAM)
    ## split it because it comes as:   ip:port
    value = value.split(':')

    dest_ip = '127.0.0.2'
    dest_port = value[1]
    dest_port = int(dest_port)
    print "Connect to Server: ", dest_port
    ###Send the message to server
    s.sendto(msg, (dest_ip, dest_port))
    ###Gets message to server
    data, _ = s.recvfrom(2048)
    print "Server ", dest_port, "sent: ", data
    msg = data
    s.close()
    return msg

#Reading mapping
def fillCache(cache):
    with open(server_name + '_mapping.txt', 'r') as _:
        for line in _:
            line = line.strip()
            if line:
                if not line[0] == '#':
                    line = line.split(' ')
                    #listoflists.append(mapping)
                    cache[line[0]].append(line[1:])
def containsKey(value, type):
    for lst in value:
        if lst[Cache.TYPE] == type:
            return lst
    return value[0]

def localContains(value, type):
    for lst in value:
        if lst[Cache.TYPE].upper() == type:
            return lst
    return False

def localCache(data):
    print "looking in local cache"
    print "Income data: " + data
    data = data.split(' ')
    if len(data) < 2:
        return "Not accepted request. need 2 args"
    key = data[0] #bob.com NS
    requestType = data[1]
    first = True
    count = 1
    changed = False
    ttlPassed = False
    while '.' in key or count:  ##as long we didn't throw all the words in site name
        if key in cache:
            value = cache[key]  ### the type, ip and TTL for the site/siyomet
            # NEED TO CHECK TTL AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            answer = localContains(value, requestType)
            if first:
                if answer != False:
                    if changed == False: ##if requestType is the original
                        if (time.time() - start_time) < int(answer[Cache.TTL]):
                            return (key + ' ' + answer[Cache.TYPE].upper() + ' ' + answer[Cache.VALUE]+ ' ' + answer[Cache.TTL])
                        else:
                            cache[key].remove(answer)
                            answer = False
                            ttlPassed = True
                    else:
                        nsAdress = answer[Cache.VALUE]
                        if nsAdress in cache:
                            nsHelper = cache[nsAdress]
                            nsIP = nsHelper[0]
                            nsIP = " ".join(nsIP)
                            return (key + ' ' + requestType + ' ' + nsAdress + ',' + nsAdress + ' ' + nsIP)

                if answer == False:
                    if ttlPassed:
                        ttlPassed = False
                        continue
                    if requestType == 'A': ##because answer = false it means that the value in cache was NS
                        requestType = 'NS'
                        print "a"
                        changed = True
                        continue
                        """nsName = value[0][Cache.VALUE]
                        if nsName in cache:
                            a = cache[nsName]
                            if a[0][Cache.TYPE].upper() == 'A':
                                if (time.time() - start_time) < a[0][Cache.TTL]:
                                    return connect_to_server(data, a[0][Cache.VALUE])"""
            else: ##if its not first time
                if answer != False: ##if NS appears
                    if (time.time() - start_time) < int(answer[Cache.TTL]): ## if TTL is ok
                        nsAdress = answer[Cache.VALUE]
                        if nsAdress in cache:
                            nsHelper = cache[nsAdress]
                            nsIP = nsHelper[0]
                            nsIP = " ".join(nsIP)
                            return (key + ' ' + requestType + ' ' + nsAdress + ',' + nsAdress + ' ' + nsIP)

        first = False
        if '.' not in key:
            count = count - 1
        else:
            key = key.split(".", 1)[1]
    ##After While
    return "notFound"

def insertToCache(toCache):
    for lst in cache[toCache[0]]:
        if lst[Cache.TYPE].upper() == toCache[1].upper():
            cache[toCache[0]].remove(lst)
            break
    cache[toCache[0]].append(toCache[1:])

def findInCache(data):
    print "Income data: " + data
    data = data.split(' ')
    key = data[0] #bob.com NS
    requestType = data[1].upper()
    count = 1
    while '.' in key or count:  ##as long we didn't throw all the words in site name
        # case that name is in cache
        if key in cache:
            # NEED TO CHECK TTL AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            value = cache[key]  ### the type, ip and TTL for the site/siyomet
            value = containsKey(value, requestType)
            if value[Cache.TYPE].upper() == requestType:  # NEED TO CHECK TTL AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                return (key + ' ' + value[Cache.TYPE] + ' ' + value[Cache.VALUE] + ' ' + value[Cache.TTL])
            else:
                nsSite = value[Cache.VALUE]
                glue = cache[nsSite]
                if glue[0][Cache.TYPE].upper() == 'A':
                    glue = glue[0]
                return (key + ' ' + value[Cache.TYPE] + ' ' + value[Cache.VALUE] + ' ' + value[Cache.TTL] + ","
                        + value[Cache.VALUE] + " " + " ".join(glue))  ## -1 to exclude TTL
        if requestType == 'NS': #if it didn't find google.com NS, we don't want com NS, but we want to ask com NS what is google NS
            requestType = 'A'
        if '.' not in key:
            count = count - 1
        else:
            key = key.split(".", 1)[1]
    ##After While
    return "notFound"


def Resolver(data): ### data = name (' ') type
    msg = localCache(data)
    print "local cache msg: " + msg
    if msg == "notFound":  ##means that it's not in LOCAL-cache, or maybe also in unresolver-server cache
            rootIP = source_ip + ':' + str(Ports.ROOT)
            msg = connect_to_server(rootIP, data)
            #print "Connect to server msg", msg


    while True:
                ## now msg = *,* or just *. if just *, so we found the ip
        if msg == "notFound": ##means that it's not in unresolver-server cache
            return "Error 404 not found"

        if ',' not in msg: ##in case we got 1 massage so its the IP
            toCache = msg.lower()
            toCache = toCache.split(' ') ##Save to cache
            notConatins = True
            """            for lst in cache[toCache[0]]:
                if lst[Cache.TYPE].upper() == toCache[1].upper():
                    notConatins = False
            if notConatins:
                cache[toCache[0]].append(toCache[1:]) ##add to key 'toCache[0]' the value of the type/ip/ttl
            return msg
            """
            insertToCache(toCache) ##add to key 'toCache[0]' the value of the type/ip/ttl
            return msg

        msg = msg.split(',') ## case we got msg like *,* so we take the second msg
        insertToCache(msg[0].split(' '))
        helper = msg[1].split(' ') #our msg is like domain.com A 1.2.3.4:12351
        insertToCache(helper)
        ip = helper[2] ## the ip:port
        msg = connect_to_server(ip, data)

def notResolver(data):
    msg = findInCache(data)
    print "The msg in cache:", msg
    return msg

def fixIncome(data):
    #print data
    helper = data.split(' ')
    #print helper
    helper[0] = helper[0].lower()
    x = helper[0]
    #print x
    if x.startswith( 'www.' ):
        helper[0] = x[4:]
    data = (" ").join(helper)
   # print data
    return data
################################################################################################main
print server_name

isResolver = raw_input("Are you a Resolver server? (y/n)")
if isResolver == 'y':
    isResolver = True
else:
    isResolver = False
print "Processing..."

cache = defaultdict(list)
fillCache(cache)
print cache
"""
cache["google.com"].append("A 1.2.3.4 1000")
valut = cache["google.com"]
t = localContains(valut, 'A')
if t:
    print "Yes"
else: print "no"
"""
###     Listens to income messages
s = socket(AF_INET, SOCK_DGRAM)
source_ip = '0.0.0.0'
source_port = port(server_name)               ### Which server runs               99999999999999999999999999999
s.bind((source_ip, source_port))
while True:
    print "Waiting for a massage"
    data, sender_info = s.recvfrom(2048)
    data = fixIncome(data)
    print "Message: ", data, " from: ", sender_info ###data = incomeMSG, sender_info = the ip of sender

    if isResolver:
        data = Resolver(data)
        print "cache:"
        print cache
    else:
        data = notResolver(data)
###Answer the client
    print "Answer: ", data
    s.sendto(data, sender_info)

#After while
s.close()
