import urllib2

GET_IP_URL_1 = "http://icanhazip.com/"
GET_IP_URL_2 = "http://myip.dnsdynamic.org/"

def get_ip():
    try:
        ret = urllib2.urlopen(GET_IP_URL_1)
        return ret.read().strip('\n').strip() \
                if ret.code == 200 \
                else urllib2.urlopen(GET_IP_URL_2).read().strip()
    except AttributeError:
        ret = urllib2.urlopen(GET_IP_URL_2)
        return ret.read().strip('\n').strip() if ret.code == 200 else None



if __name__ == '__main__':
    print get_ip()
