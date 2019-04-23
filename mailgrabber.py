# -*- coding: utf-8 -*
#!/usr/bin/python
#####################################
##KILL THE NET##
#### PS: CHANGE Your Threads pool on line 136 to make script more faster :)
##############[LIBS]###################
import requests, re, urllib2, os, sys, codecs, random               
from multiprocessing.dummy import Pool                          
from time import time as timer  
import time
import json
from urlparse import urlparse
import warnings
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
reload(sys)  
sys.setdefaultencoding('utf8')
##########################################################################################
ktnred = '\033[31m'
ktngreen = '\033[32m'
ktn3yell = '\033[33m'
ktn4blue = '\033[34m'
ktn5purp = '\033[35m'
ktn6blueblue = '\033[36m'
ktn7grey = '\033[37m'
CEND = '\033[0m'        
#####################################
##########################################################################################
try:
    with codecs.open(sys.argv[1], mode='r', encoding='ascii', errors='ignore') as f:
        ooo = f.read().splitlines()
except IndexError:
    print (ktnred + '[+]================> ' + 'USAGE: '+sys.argv[0]+' listsite.txt' + CEND)
    pass
ooo = list((ooo))
##########################################################################################

def getemails(url):
    try:
        paths = ['/', '/faq', '/faq.php', '/faq.asp', '/faq-support', '/article', '/article.php', '/article.asp', '/support', '/support.php', '/support.asp', '/members', '/members.php', '/members.asp', '/detail', '/detail.php', '/detail.asp', '/contact', '/contact.php', '/contact.asp']
        for path in paths:
            try:
                pay = url + path
                Agent2 = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
                se2 = requests.session()
                ktn2 = se2.get(pay, headers=Agent2, verify=False, timeout=20, allow_redirects=True)
                if ktn2.status_code == 200:
                    kills = ktn2.content.encode('utf-8')
                    emails = re.findall(r"[A-Za-z0-9%&*+?^_`{|}~-]+(?:\.[A-Za-z0-9!#$%&*+?^_`{|}~-]+)*@(?:[A-Za-z0-9](?:[a-z0-9-]*[A-Za-z0-9])?\.)+(?:[A-Za-z]{2}|com|org|net|edu|gov|mil|biz|info|mobi|name|aer  o|asia|jobs|museum)\b", kills)
                    for email in emails:
                        print (ktn5purp + 'EMAIL FOUND: [' + email + ']' + CEND)
                        open('emails.txt', 'a').write(email+'\n')

                    pass
                pass
            except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout) as e:
                print (ktnred + 'TIME OUT AND RETRY: ' + url + CEND)
                pass
        pass
    except:
        pass

def check(url):
    try:
        Agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
        se = requests.session()
        ktn1 = se.get(url, headers=Agent, verify=False, timeout=20, allow_redirects=False)
        if ktn1.status_code == 200:
            print (ktngreen + 'SEARCHING FOR EMAILS ..... [' + url + ']' + CEND)
            getemails(url)
            pass
        else:
            print (ktnred + 'DEAD SITE: ' + url + CEND)

        pass
    except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout) as a:
        print (ktnred + 'TIME OUT: ' + url + CEND)
        check(url)
        pass
    except requests.exceptions.ConnectionError as b:
        print (ktnred + 'DEAD SITE: ' + url + CEND)
        pass
    pass

#####################################
def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]
    x = ''' 
         FEDERATION BLACK HAT SYSTEM | IG: @_gghost666_ 
                              ...
           s,                .                    .s
            ss,              . ..               .ss
            'SsSs,           ..  .           .sSsS'
             sSs'sSs,        .   .        .sSs'sSs
              sSs  'sSs,      ...      .sSs'  sSs
               sS,    'sSs,         .sSs'    .Ss
               'Ss       'sSs,   .sSs'       sS'
      ...       sSs         ' .sSs'         sSs       ...
     .           sSs       .sSs' ..,       sSs       .
     . ..         sS,   .sSs'  .  'sSs,   .Ss        . ..
     ..  .        'Ss .Ss'     .     'sSs. ''        ..  .
     .   .         sSs '       .        'sSs,        .   .
      ...      .sS.'sSs        .        .. 'sSs,      ...
            .sSs'    sS,     .....     .Ss    'sSs,
         .sSs'       'Ss       .       sS'       'sSs,
      .sSs'           sSs      .      sSs           'sSs,
   .sSs'____________________________ sSs ______________'sSs,
.sSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS'.Ss SSSSSSSSSSSSSSSSSSSSSs,
                        ...         sS'
                         sSs       sSs
                          sSs     sSs       - KTN
                           sS,   .Ss
                           'Ss   sS'
                            sSs sSs
                             sSsSs
                              sSs
                               s   
                                      KILL THE NET
                                     FB: fb/KtN.1990  
               Note! : PRIVATE EMAIL GRABBER '''

    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
        pass


logo()
##########################################################################################
def Main():
    try:
        
        start = timer()
        ThreadPool = Pool(150)
        Threads = ThreadPool.map(check, ooo)
        print('TIME TAKE: ' + str(timer() - start) + ' S')
    except:
        pass


if __name__ == '__main__':
    Main()