import requests as r
from bs4 import BeautifulSoup as bs
#Coded by Nubzbie
import requests as r
from bs4 import BeautifulSoup as bs
import json,re,os
banner = """
   __  ___                __  __ 
  /  |/  /__ ____ _______/ /_/ /_
 / /|_/ / _ `(_-<(_-<___/ __/ __/
/_/  /_/\_,_/___/___/   \__/\__/ 
                                 
coded by Nubzbie\n"""
class ngentod:
  def __init__(self):
    self.url = ('https://ttonlineviewer.com/user/')
    self.video = ('https://ttonlineviewer.com/p/')
  def jancok(self):
    tok = r.get(self.url+user).text
    print ("-"*50)
    print ("Deskripsi User : ")
    ink = bs(tok,'html.parser')
    inka = ink.find('p',attrs={'class':'username mb-2'})
    stats = ink.findAll('p',attrs={'class':'stats mb-2'})
    inl = ink.findAll('div',attrs={"class":"media-item-body"})
    inkl = ink.findAll('p',attrs={"class":"desc"})[0]
    print ("User : ",inka.text)
    for yi in stats:
      print (yi.text)
    print ("Deskripsi : ",inkl.text)
    for x in inl:
      indah = (x.text)
      print (indah)
    tod = bs(tok,'html.parser') 
    tok = tod.findAll('p')
    tt = tod.findAll('a',attrs={'class':"cover-link"})
    #k = re.findall('<a class=.*? href="(.*?)"',str(tod))
    print ("-"*50)
    print ("Video id info : \nnb: Jika video kosong tekan ctrl+z\n")
    for jj in tt:
      uk = (jj['href']).replace("https://ttonlineviewer.com/","").replace("p/","")
      print (uk)  
    
  def kntlmanis(self):
    tk = r.get(self.video+li).text
    kt = bs(tk,'html.parser')
    ktq = kt.findAll("div",attrs={"class":"video-container float-left"})
    for lt in ktq:
      kt1 = re.findall('<source src="(.*?)"',str(lt))
      print ("Link video : ",kt1)

main=ngentod()
os.system("clear")
print (banner)
print("-"*50)
user=input("Nama User : ") 
main.jancok()
li = input("\nID video : ")
main.kntlmanis()
#except:
  #pass
