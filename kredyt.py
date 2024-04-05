import math

def rata(k,n,s):
    q = 1+s/12
    return k*pow(q,n)*(q-1)/(pow(q,n)-1)

def symulacja():
    kwota_kredytu = 272444.83 #280000
    stop_bazowa = 5.32/100
    marza = 1.92/100
    liczba_miesiecy = 299 - 6
    current = 272444.83
    k = kwota_kredytu
    n = liczba_miesiecy
    s = marza + stop_bazowa 

    budzet = 3000
    
    ratka = rata(k,n,s)
    print("ratka: ",ratka) 
    print("odsetki: ", k*s/12)
    print("capital: ", ratka - k*s/12)
    print(f' Kwota\tRatka\tOdsetki\tKapital\tNadplata')
    iter_kredyt(k,s,n,budzet, count=0)

def iter_kredyt(kwota, procent, mies, budzet, count):
    if kwota <=0:
        ratka = rata(kwota,1,procent)
        odsetki = kwota*procent/12
        kapital = ratka - odsetki
        print(f'{count} Kwota {kwota:.2f}\tRatka {ratka:.2f}\tOdsetki {odsetki:.2f}\tKapital {kapital:.2f}')
        print(f"koniec {count/12} lat {count} mies")
    else:
        ratka = rata(kwota,mies,procent)
        odsetki = kwota*procent/12
        nadplata = budzet - ratka
        kapital = ratka - odsetki 
        print(f'{count} {kwota:.2f}\t{ratka:.2f}\t{odsetki:.2f}\t{kapital:.2f}\t{nadplata:.2f}')

        iter_kredyt(kwota-kapital-nadplata,procent,mies-1,budzet,count+1)
        




if __name__ == "__main__":
    symulacja()