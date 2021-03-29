from lxml import html
import requests
import asyncio



def home_page():
    #site url
    site = "https://animeblkom.net/"
    # requesting
    page = requests.get(site)
    tree = html.fromstring(page.content)
    anime = tree.xpath('//div[@class="recent-episodes"]')
    for cc in anime:
        hh = cc.xpath('.//a/@href')
        name = cc.xpath('.//div[@class="name"]/text()')
        numb = cc.xpath('.//div[@class="episode-number"]/text()')

    return 1, hh, name, numb


def ep(url):
    search = requests.get("https://animeblkom.net" + url)
    trees = html.fromstring(search.content)
    name = trees.xpath('//div[@class="anime-name"]/a/text()')[0]
    epi = trees.xpath('//div[@class="episode-number"]/text()')[0]
    eplink = trees.xpath('//iframe/@src')
    dwlinks = trees.xpath('//div[@class="panel-body"]/a/@href')
    cal = trees.xpath('//div[@class="panel-body"]/a/text()')
    tit = trees.xpath('//div[@class="panel-body"]/a/@title')
    size = trees.xpath('//div[@class="panel-body"]/a/small/text()')
    for i in cal:
        if i.endswith("\n"):
            cal.remove(i)
    if len(eplink) == 0:
        return 0, "invalid ep"
    else:
        return 1, eplink[0], name, epi, dwlinks, cal, tit, size


def s_animes(namen):
  name = namen.replace(" ", "+")
  page = requests.get('https://animeblkom.net/search?query=' + name)
  tree = html.fromstring(page.content)
  anime = tree.xpath('//div[@class="name"]/a/@href')
  btbtlen = len(anime)
  return anime, btbtlen


def borba(ep, namen,cali):
    kbkb = s_animes(namen)
    anime = kbkb[0]
    if len(anime) == 0:
        return 3, "لا توجد نتائج في البحث",
    search = requests.get("https://animeblkom.net" + anime[0] + "/" + ep)
    trees = html.fromstring(search.content)
    name = trees.xpath('//div[@class="anime-name"]/a/text()')
    if len(name) == 0:
        return 0, "لا توجد نتائج في البحث"
    eplink = trees.xpath('//iframe/@src')
    dwlinks = trees.xpath('//div[@class="panel-body"]/a/@href')
    cal = trees.xpath('//div[@class="panel-body"]/a/text()')
    for i in cal:
      if i.endswith("\n"):
        cal.remove(i)
    calit = []
    for i in cal:
      calit.append(i.replace("\n", ""))
    for i in calit:
      if not "p" in i:
        calit.remove(i)
    for i in range(len(calit)):
      if cali in calit[i]:
        dwlinks = dwlinks[i]
        break

    if isinstance(dwlinks, list):
      dwlinks = dwlinks[0]


      

        
    if len(eplink) == 0:
        return 0, "invalid ep", 0
    else:
        return 1, dwlinks
























def multidw(namen , st, en,cali):
  links = []
  errs = []
  for i in range(st,en+1):
    lara = borba(str(i),namen,cali)
    if lara[0] == 0:
      errs.append(str(i))
    elif lara[0] == 1:
      links.append(lara[1])

  

  return links , errs

def star(ep, namen, ss = 0):
    kbkb = s_animes(namen)
    anime = kbkb[0]
    if len(anime) == 0:
        return 0, "لا توجد نتائج في البحث", 0
    search = requests.get("https://animeblkom.net" + anime[ss] + "/" + ep)
    trees = html.fromstring(search.content)
    name = trees.xpath('//div[@class="anime-name"]/a/text()')
    if len(name) == 0:
        return 0, "لا توجد نتائج في البحث", 0
    eplink = trees.xpath('//iframe/@src')
    dwlinks = trees.xpath('//div[@class="panel-body"]/a/@href')
    cal = trees.xpath('//div[@class="panel-body"]/a/text()')
    tit = trees.xpath('//div[@class="panel-body"]/a/@title')
    size = trees.xpath('//div[@class="panel-body"]/a/small/text()')
    for i in cal:
        if i.endswith("\n"):
            cal.remove(i)
    if len(eplink) == 0:
        return 0, "invalid ep", 0
    else:
        return 1, eplink[0], name[0], ep, dwlinks, cal, tit, size

print(star("1","monster",7))
def sta(namen):
    name = namen.replace(" ", "+")
    page = requests.get('https://animeblkom.net/search?query=' + name)
    tree = html.fromstring(page.content)
    anime = tree.xpath('//div[@class="name"]/a/@href')
    if len(anime) == 0:
        return 0, "لا توجد نتائج في البحث"
    search = requests.get("https://animeblkom.net" + anime[0])
    link = "https://animeblkom.net" + anime[0]
    aniname = anime[0].split("/")[2]

    anpage = html.fromstring(search.content)
    aniname = tree.xpath('//div[@class="name"]/a/text()')[0]
    poster = anpage.xpath('//meta/@content')
    posterlink = ""
    for a in poster:
        if 'https://animeblkom.net/img/' in str(a):
            posterlink = str(a)
    story = tree.xpath('//div[@class="story-text"]/p/text()')
    genres = anpage.xpath('//p[@class="genres"]/a/text()')
    test = anpage.xpath('//span[@class="head"]/text()')
    test1 = anpage.xpath('//span[@class="info"]/text()')
    test3 = anpage.xpath('//div[@class="info-cards"]/div[1]/span/text()')[0]
    test5 = anpage.xpath('//div[@class="info-cards"]//span/a/text()')
    
    if len(test5) == 0:
      nono = "-"
    else:
      nono = test5[0]
    test4 = anpage.xpath('//div[@class="info-cards"]/div[2]/span/text()')
    ratt = anpage.xpath(
        '//button[@class="rating-box pull-left dropdown-toggle"]/span/text()')
    return 1, posterlink, story[
        0], genres, test1, test, ratt, aniname, link, test3, test4, nono

