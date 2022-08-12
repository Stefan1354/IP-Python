'''11.Dat je trocifreni broj n. Ispisati najveci broj koji
se moze formirati od cifara broja n.'''

#n=int(input("Unesi trocifreni broj "))
#a=n//100  #cifra stotina
#b=n//10%10  #cifra desetica
#c=n%10  #cifra jedinica
#najveca=max(a,b,c)
#najmanja=min(a,b,c)
#srednja=a+b+c-najmanja-najveca
#nb=najveca*100+srednja*10+najmanja
#print("Najveci broj je", nb)

'''12.Dat je prirodan broj n>=100.Zameniti mesto cifri stotina
i cifri jedinica.'''
# 12345    345

#n=int(input("Unesite broj "))
#ost=n%1000  #uzimamo poslednje 3 cifre kao trocifreni broj
#a=ost//100
#b=ost//10%10
#c=ost%10
#ost1=c*100+b*10+a
#novbr=n//1000*1000+ost1
#print("Novi broj je ", novbr)

'''13.Dato je vreme u sekundama. Ispisati koliko je to sati,
minuta i sekundi u formatu sati:minuta:sekundi.'''
#primer: sek=3700

#sek=int(input("Unesite vreme u sekundama "))
#sati=sek//3600     #sati=3700/3600=1
#minuta=sek//60%60  #minute=3700/60=61/60=1
#sekunde=sek%60     #sekunde3700/60=40 ostatak
#print(sati, ":", minuta,":",sekunde)

'''14.Avion je poleteo u s sati i m minuta. Let je trajao
k minuta. Ispisati u koje vreme je avion sleteo (moze biti
i sledeceg dana).'''

#s,m=map(int,input("Unesite vreme poletanja ").split())
#k=int(input("Koliko je trajao let "))
#poleteo=s*60+m      #vreme poletanja
#sleteo=poleteo+k    #vreme sletanja
#sat=sleteo//60%24      #sat kada je sleteo
#minute=sleteo%60    #minute kada je sleteo
#print("Vreme sletanja ", sat, ":", minute)

'''15. Dat je prirodni broj N. Ispisati prvi veci broj od N
koji je deljiv sa 7.'''
     #23//7=3
     #4*7

#N=int(input("Unesite N "))
#a=N//7
#rez=(a+1)*7
#print(rez)

'''16. Dat je prirodan broj N. Ispisati najblizi broj broju N
koji je deljiv sa 7.'''
#23  -> 21         26  ->  28     21  ->  21
#23/7=3.28.. (primenio zaokruzivanje round, dobili smo 3 i
# opet pomnozimo  sa 7 dobijemo 21) 
#26/7=3.71.. zaokruzimo sa round na 4*7=28
#21/7=3  3*7=21

#n=int(input("Unesite broj "))
#rez=round(n/7)*7
#print("Najblizi broj je ", rez)

'''17. Dat je prirodan broj N. Ispisati prvi manji broj od N
ciji je kvadratni koren ceo broj.'''
#28  ->  25     34 -->  25    37 -->  36
#koren iz 27 (oduzimamo 1 od 28) je 5, 
#i zaokruzujemo na manji, 5 na kvadrat 25

#import math
#n=int(input("Unesite broj "))
#rez=math.floor(math.sqrt(n-1))**2
#print("Najblizi manji je ", rez) 
  #floor zaokruzuje na manji broj

'''18.Dat je prirodan broj N. Ispisati najblizi broj broju N
ciji je kvadratni koren ceo broj.'''
#30 ->  25   34 ->  36  36  ->  36

#import math
#n=int(input("Unesite broj "))
#rez=round(math.sqrt(n))**2   #zaokruzi taj kvadratni koren i
#opet ga kvadriraj nezaokruzenog
#print("Najblizi je ", rez)

'''19.Ispisati da li je broj paran ili neparan bez koriscenja
naredbe if.'''

#n=int(input("Unesite broj "))
#rez=(n%2==0)*"Broj je paran"+(n%2!=0)*"Broj je neparan"
#print(rez)

'''20.Data su 2 ugla trougla u obliku (stepeni minute sekunde).
Izracunati 3.ugao.'''

#s1,m1,se1=map(int,input("Unesite stepene, minute i
#sekunde 1. ugla ").split()
#s2,m2,se2=map,int(input("Unesite stepene, minute i
#sekunde 2. ugla ").split()
#ug1=s1*3600+m1*60+se1
#ug2=s2*3600+m2*60+se2
#ug3=180*3600-(ug1+ug2)  #treci ugao u sekundama
#s3=ug3//3600  #stepeni 3. ugla
#m3=ug3//3600//60  #minute 3. ugla
#se3=ug3%60
#print("Ugao je ", s3,m3,se3)


