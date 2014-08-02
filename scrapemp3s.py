
# Extracts (downloads) all MP3 files listed at the given URL to the current directory.

import sys, re, os, urllib
from mechanize import Browser
from cookielib import LWPCookieJar
from BeautifulSoup import BeautifulSoup

if len(sys.argv) != 2: # require a URL to scan
    sys.exit("Must specify a URL")

url = sys.argv[1]
print "Scanning: %s " % url
print

mech = Browser()
cj = LWPCookieJar()
mech.set_cookiejar(cj)
mech.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
mech.set_handle_robots(False)
mech.set_handle_equiv(True)
mech.set_handle_gzip(True)
mech.set_handle_referer(True)
mech.set_debug_http(True)
mech.set_debug_redirects(True)
mech.set_debug_responses(True)
page = mech.open(url)
html = page.read()
soup = BeautifulSoup(html)
 
# Extract all anchors on the page that include the string ".mp3"
anchors = soup.findAll(attrs={'href' : re.compile(".mp3")})
for a in anchors:
    mp3link = a['href'] # Get the value of the href, not the whole tag/container!
    
    # To get an output filename, split the URL on slashes and grab the last array item
    urlfrags = mp3link.split('/')
    save_as = urlfrags[len(urlfrags)-1] # Resolves to e.g. urlfrags[4]
    print mp3link
    print "Saving: %s" % save_as
    print
    # The actual download
    urllib.urlretrieve(mp3link, save_as)

# for f in mesh.forms():
#     print f
#     mech.select_form(nr=1)
#     mech.form['username'] = 'username'
#     mech.form['password'] = 'password'
#     mech.submit()


# for f in br.forms():
#     print f
# br.select_form(nr=0)
# #google search
# br.form['q'] = 'football'
# br.submit()
# print br.response().read()
# #baidu search
# br.form['wd'] = 'football'
# br.submit()
# print br.response().read()

# return back
# br.back()
# print br.geturl()

# set proxy
# br.add_password('http://xxx.com', 'username', 'password')
# br.open('http://xxx.com')

# br.set_proxies({"http":"username:password@proxy.com:8888"})
