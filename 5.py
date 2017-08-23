import urllib.request 
import re  


def next_page(p):
     text = urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?'
                           'nothing=%s' % p).read()
     m = re.match('and the next nothing is ([0-9]+)', text)
     if not m: print (text)
     return m.group(1)
