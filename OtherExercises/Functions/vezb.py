'''n = int(input("Enter n ")) # broj elemenata
postoji_negativan = False # da li među učitanim postoji negativan
for i in range(n): # obrađujemo n elemenata
    x = float(input("Enter x ")) # učitavamo element
    if x < 0: # ako je on negativan,
        postoji_negativan = True # onda među učitanim postoji negativan
print("da" if postoji_negativan else "ne") #ispisujemo rezultat'''

# • s.isdigit – проверава да ли су сви карактери ниске s цифре
# • s.islower – проверава да ли су сва слова у ниски s мала слова
# • s.isupper – проверава да ли су сва слова у ниски s велика слова

# c = input("Unesite c ")
# if c.islower():
#     print("MALO SLOVO")
# elif c.isupper():
#     print("VELIKO SLOVO")
# elif c.isdigit():
#     print("CIFRA")
# else:
#     print("OSTALO")

# ch = input("Enter ch ")[0]
# if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
#     ch = chr(ord(ch) - ord('a') + ord('A'))
# elif ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
#     ch = chr(ord(ch) - ord('A') + ord('a'))
# print(ch)

#print(ord("a")) #97
#print(ord("b")) #98