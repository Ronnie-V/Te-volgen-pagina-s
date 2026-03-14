#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pywikibot
#import datetime
#from pywikibot import pagegenerators as pg
#import sys
#import time

#select the right page
site = pywikibot.Site('nl', 'wikipedia')

import time

# Track start time across calls
#_start_time = time.time()


def handletitel(titel):
  count = 0
  extratext = ''
  datetimes = []
  editors = []
  remarks = []
  page = pywikibot.Page(site, titel)
  for rev in page.revisions(total=50):
##      if 'bot' in rev.user.groups():
##        continue
      user = pywikibot.User(site, rev.user)
      if 'bot' in user.groups():
        continue
      count += 1
      datetimes.append( str(rev.timestamp)[:16] )
      editors.append ( rev.user )
      remarks.append (rev.comment)
      if count >= 5:
        break
        
  extratext = f"|-\n| rowspan={count} | [[{titel}]] |"
  for c in range(0,count):
    if c > 0:
      extratext += "|-\n"
    extratext += f"| {editors[c]} || {datetimes[c]} || {remarks[c]}\n"
  return(extratext)

def main():
  text = '{| class="vatop wikitable sortable"\n!Titel!!Bewerker!!Tijdstip!!Samenvatting\n'
#  handletitel( "Jan Terlouw")
#  handletitel("Amsterdam")
##  for verzoekpage in site.search('intitle:"Te volgen pagina\'s"', namespaces = [2]): #nazoeken
  verzoekpagetitel = "Gebruiker:RonnieV/Te volgen pagina's"
  verzoekpage = pywikibot.Page(site, verzoekpagetitel)

#  print (verzoekpage.title())
  for titel in verzoekpage.text.splitlines():
      text += handletitel(titel)
  text += '|}\n'
  print (text)
  targetpage = pywikibot.Page(site, f'{verzoekpagetitel}/Resultaat')
  targetpage.text = text
  targetpage.save('Bijgewerkt')


if __name__ == '__main__':
    main()
