alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def deszyfr(szyfr, klucz):
    deszyfr = ''

    for index, szyfr_litera in enumerate(szyfr):
        klucz_litera = klucz[index % len(klucz)]
        szyfr_litera_idx = alfabet.find(szyfr_litera)
        klucz_litera_idx = alfabet.find(klucz_litera)

        if szyfr_litera_idx >= klucz_litera_idx:
            przesuniecie = szyfr_litera_idx - klucz_litera_idx
        else:
            przesuniecie = len(alfabet) + szyfr_litera_idx - klucz_litera_idx
        
        deszyfr_litera_idx = przesuniecie


        deszyfr_litera = alfabet[deszyfr_litera_idx]

        deszyfr = deszyfr + deszyfr_litera

    return deszyfr

print(deszyfr('ZZGUAVCZI','LOGIA'))