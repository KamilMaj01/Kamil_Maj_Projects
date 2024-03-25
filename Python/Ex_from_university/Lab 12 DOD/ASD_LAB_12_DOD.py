# skończone

import math
import time

with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()

S = ' '.join(text).lower()

def prime_number(k, threshold = 2):
    set_prime = []
    number = threshold

    while len(set_prime) != k:
        if number == 2:
            set_prime.append(number)
        if number % 2 == 0 or number <= 1:
            number += 1 
            continue
        prime = int(number**0.5) + 1

        test = True
        for d in range(3,prime,2):
            if number % d == 0:
                test = False
                break
        if test == True:
            set_prime.append(number)
        number += 1
    return set_prime


def RabinKarpSet(text, patern, d = 256, P = 0.001, threshold = 2):

    counter = 0
    M = len(text)
    N = len(patern[0])
    n = len(patern)
    n = n if n != 1 else 2
    b = round(-n*math.log(P)/math.log(2)**2)
    k = round(b/n*math.log(2))
    primes = prime_number(k,threshold)
    hsubs = [0 for _ in range(b) ]   

    for el in patern:
        result_hash = Hash(el,primes,d, b)
        
        for idx in result_hash:
            hsubs[idx] = 1
    
    hs = Hash(text[:N],primes,d, b)

    

    found = []
    for m in range(1,M-N+1):
        check = True
        for hs_el in hs:
            if hsubs[hs_el] == 0:
                check = False
                break
        if check:
            if text[m-1:m+N-1] in patern:
                found.append(m)
            else:
                counter += 1

        for idx_hs, q in enumerate(primes):
            new_hs = (d * (hs[idx_hs] - ord(text[m-1]) * (d**(N-1) % q) ) + ord(text[m-1 + N])) % q
            new_hs = new_hs % b
            hs[idx_hs] = new_hs

    return len(found), counter


def Hash(word,primes, d, b): 
    N = len(word)
    result_hw = []
    for q in primes:
        hw = 0
        for i in range(N):  
            hw =  (hw*d + ord(word[i])) % q
        hw = hw %  b
        result_hw.append(hw)
    
    return result_hw

def main():
    patterns = ['gandalf', 'looking', 'blocked', 'comment', 'pouring', 'finally', 'hundred', 'hobbits',
                'however', 'popular', 'nothing', 'enjoyed', 'stuffed', 'relaxed', 'himself', 'present',
                'deliver', 'welcome', 'baggins', 'further']
 
    t_start = time.perf_counter()
    r, c = RabinKarpSet(S, ['gandalf'])
    t_stop = time.perf_counter()
    print("Rezultat dla jednego wzorca:\nCzas obliczeń:", "{:.7f}".format(t_stop - t_start))
    print(f'Wynik:, {r}, Kolizje:, {c}\n')

    t_start = time.perf_counter()
    r, c = RabinKarpSet(S, patterns)
    t_stop = time.perf_counter()
    print("Rezultat dla 20-stu wzorców:\nCzas obliczeń:", "{:.7f}".format(t_stop - t_start))
    print(f'Wynik:, {r}, Kolizje:, {c}\n')

    t_start = time.perf_counter()
    r, c = RabinKarpSet(S, patterns,threshold= 101)
    t_stop = time.perf_counter()
    print("Rezultat dla 20-stu wzorców przy lepiej dobranych liczbach pierwszych:\nCzas obliczeń:", "{:.7f}".format(t_stop - t_start))
    print(f'Wynik:, {r}, Kolizje:, {c}\n')

    
main()