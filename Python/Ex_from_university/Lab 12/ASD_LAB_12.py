#  Skończone
import time

with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()

S = ' '.join(text).lower()


def naiwna(text, pattern, S = 0):
    found = []
    counter = 0
    
    m = S
    i = 0
    n = len(text)
    n_p = len(pattern)
    while m != n - n_p +1:
        counter += 1
        if text[m] == pattern[0]:
             check = True
             current_m = m + 1
             i = 1
             while check:
                counter +=1
                if i == n_p-1 and text[current_m] == pattern[i] :
                    found.append(m)
                    check = False
                elif i <= n_p-1 and text[current_m] != pattern[i]:
                    check = False
                current_m += 1
                i += 1
        m += 1
    

    return (len(found),counter) 

def RabinKarp(text, patern, d = 256, q = 101):
    

    found = []
    N = len(patern)
    hW, h = Hash(patern, N,d,q)
    M = len(text)
    counter = 0
    colision = 0
    hS = None
    for m in range(M-N+1):

        toHash = text[m : (m+N)]
        if hS is None:
            hS, _ = Hash(toHash, N,d,q)
        else:
            hS = (d * (hS - ord(text[m-1]) * h) + ord(text[m-1 + N])) % q
        if hS < 0:
            hS += q
        counter += 1
        if hW == hS:
            if text[m : (m+N)] == patern:
                found.append(m)
            else:
                colision += 1
    
    return len(found), counter, colision



def Hash(word, N, d, q): 

    hw = 0
    for i in range(N):  # N - to długość wzorca
        hw = (hw*d + ord(word[i])) % q  # dla d będącego potęgą 2 można mnożenie zastąpić shiftem uzyskując pewne przyspieszenie obliczeń
    
    h = 1
    for i in range(N-1):  # N - jak wyżej - długość wzorca
        h = (h*d) % q

    return hw, h

def kmp_search(text, pattern, S = 0):
    M = len(text)
    N = len(pattern)
    m = S
    i = 0
    T = kmp_table(pattern)
    P = []
    nP = 0
    counter = 0

    while m < M:
        counter +=1
        if pattern[i] == text[m]:
            m += 1
            i += 1
            if i == N:
                P.append(m -1)
                nP += 1
                i = T[i]
        else:
            i = T[i]
            if i < 0 :
                m += 1
                i += 1
    return len(P), counter, T

def kmp_table(patern):
    N = len(patern)
    pos = 1
    cnd = 0
    T = [None for _ in range(N + 1)]
    T[0] = -1
    while pos < N:
        if patern[pos] == patern[cnd]:
            T[pos] = T[cnd]
        else:
            T[pos] = cnd
            while cnd >= 0 and patern[pos] != patern[cnd]:
                cnd = T[cnd]
        pos += 1
        cnd += 1

    T[pos] = cnd

    return T
    


def main():
    t_start1 = time.perf_counter()
    result1 = naiwna(S,"time.")
    print(f'Metoda naiwna: {result1[0]}; {result1[1]}')
    t_stop1 = time.perf_counter()
    print("Czas obliczeń 'Metoda naiwna':", "{:.7f}".format(t_stop1 - t_start1))

    
    t_start2 = time.perf_counter()
    result2 = RabinKarp(S, 'time.')
    print(f'\nRabinKarp: {result2[0]}; {result2[1]}; {result2[2]}')
    t_stop2 = time.perf_counter()
    print("Czas obliczeń 'RabinKarp':", "{:.7f}".format(t_stop2 - t_start2))

    t_start3 = time.perf_counter()
    result3 = kmp_search(S, 'time.')
    print(f'\nKnutha-Morrisa-Pratta: {result3[0]}; {result3[1]}; {result3[2]}')
    t_stop3 = time.perf_counter()
    print("Czas obliczeń 'Knutha-Morrisa-Pratta':", "{:.7f}".format(t_stop3 - t_start3))

main()