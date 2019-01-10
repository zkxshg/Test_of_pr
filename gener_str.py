import numpy as np

#Generate the reference strings and corresponding dirty bits
#Random
def generate_rand():
    rand_str = np.random.randint(1, 501, size=1)
    rand_modi = np.random.randint(0, 2, size=1)
    while(rand_str.size<100000):
        anchor = np.random.randint(1, 496)
        cont = np.random.randint(5)
        for i in range(cont):
            rand_str = np.append(rand_str, anchor+i)
            rand_modi = np.append(rand_modi, np.random.randint(0,2))
    return rand_str,rand_modi

#Locality
def generate_local():
    local_str = np.random.randint(1, 501, size=1)
    rand_modi = np.random.randint(0, 2, size=1)
    sli = 1
    while (local_str.size < 100000):
        free_page = np.random.randint(1, 501, size=2500)
        local_str = np.append(local_str, free_page)
        loc_page = np.random.randint(sli, sli+25, size=2500)
        local_str = np.append(local_str, loc_page)
        rand_modi = np.append(rand_modi, np.random.randint(0, 2, size=5000))
        sli+=25
    return local_str,rand_modi

#own string
def generate_own():
    own_str = np.random.randint(1, 501, size=1)
    rand_modi = np.random.randint(0, 2, size=1)
    while (own_str.size < 100000):
        search_page = np.arange(1, 501)
        own_str = np.append(own_str, search_page)
        anchor = np.random.randint(1, 451)
        out_page = np.random.randint(anchor, anchor+50, size=500)
        own_str = np.append(own_str, out_page)
        rand_modi = np.append(rand_modi, np.random.randint(0, 2, size=1000))
    return own_str,rand_modi
