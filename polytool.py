import math, itertools, random

poly  = 0xa195150d15*2+1
mask1 = 0x000000ffff
mask2 = 0xffffff0000

#poly = int('10111011101000100011111101011110000111011001011010101010110100101100110010111000010110010100101011000101001100000010000011000001'[::-1],2) # LILI-II
#poly = int('110000000000000000000000000000000000000100100000000001010000000000000000000000001001000001'[::-1],2) # LILI-128

def get_key_mask1(item): return item[0] & mask1
def get_key_mask2(item): return item[0]
def max_deg(item): return max(item[1])

def reverse_poly(p):
    return int(bin(p)[2:][::-1],2)

# generate multiples 1,x,...,x^n mod P(x) and put in table 
def gen_multiples(n, p, d):
    px = 1
    f = 2**d
    list_of_multiples = [(px,[1])]
    for i in xrange(0, n): 
        px = (px << 1)
        if (px & f): px ^= poly
        list_of_multiples.append((px,[i]))
    return sorted(list_of_multiples, key=get_key_mask1)
    #return list_of_multiples

# perform sort and match on table using mask
def sort_and_match(L, mask):
    J = []
    tot_size = 0
    tot_sets = 0
    i = 0
    while i < len(L):
        q = len(L)-1
        c = L[i]
        T = [c]
        j = i+1
        if j > q: break
        while((c[0] ^ L[j][0]) & mask == 0): 
            T.append(L[j])
            j += 1
            if j > q: break
        for s in itertools.combinations(T,2):
            J.append((s[0][0] ^ s[1][0], s[0][1] + s[1][1]))
        i = j
    return sorted(J, key=get_key_mask2)

# pick an random mask satisfying with d_p/3 bits set
def adjust_mask(deg):
    c1,c2 = deg/3,deg-deg/3
    mstr = ''.join(random.sample('1'*c1+'0'*c2, deg))
    return int(mstr,2), int('1'*deg,2)

def print_poly(p): 
    out = ''
    for i,x in enumerate(bin(p)[2:][::-1]):
        if x == '1':
            out += 'x^'+str(i)+' + '
    out = out.replace('x^0','1').replace('x^1 ','x ')[:-2]
    out = out.split(' ')
    out.reverse()
    out = ''.join(out)
    print out

degree = int(math.log(poly)/math.log(2))

print "\n" + "-"*60
print "POLYTOOL v0.1\tCarl Londahl 2014, grocid.net\n" + "-"*60
print "\nPolynomial (deg "+str(degree)+") :\t",
print_poly(poly)

print "\n[+] Generating initial list..."
mask1,mask2 = adjust_mask(degree)
L = gen_multiples(2**20, poly, degree)
print "[*]", len(L), "entries generated."

it = True
its = 0
while it:
    its += 1
    L.sort(key=get_key_mask1)
    L1 = sort_and_match(L, mask1)
    print "[*]", len(L1), "surviving entries using mask", hex(mask1), "("+str(its)+" iterations)"
    L1 = sort_and_match(L1, mask2)
    L1.sort(key=max_deg)
    mask1,mask2 = adjust_mask(degree)
    if len(L1) > 0:
        it = False
        print "[+] Listing candidate of lowest degree...\n"
        e = sorted(L1[0][1])
        mm = min(e)
        print "    x^" + str(e[3]-mm) + "+x^" + str(e[2]-mm)+ "+x^" + str(e[1]-mm) + "+1"
    else: it = True
    
print "\n" + "-"*60 + "\n"

