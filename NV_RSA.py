from os import TMP_MAX, read
import random

# extended euclidean algorithm
def Euclidean(a,b):
    if a == 0:
        return 0, 1
    else:
        x, y = Euclidean(b % a, a)
        return y - (b // a) * x, x

# Fast modular exponentiation
def modular(a,b,m) :
    p = 1
    while (b > 0) :
        if (b % 2 == 1) :
            p = (p * a) % m ; b = b - 1
        else :
            a = (a * a) % m ; b = b // 2
    return p

# Miller Rabin
def Miller(num) :
    a = random.randint(2,num-1)     
    b = num - 1 ; ex = 0

    while(b % 2 == 0) :
        b //= 2  ; ex +=1

    T = modular(a,b,num)
    if T == 1 or T == num -1:
        return True 
    else :
        for i in range(1,ex) :
            T = T**2 % num
            if T == num - 1 :
                return True
        return False

li = [num for num in range(2,1000) if num % 2 !=0]
def is_prime(num) :    
    while True : 
        num = random.getrandbits(1000)
        if any(num % i == 0 for i in li) :
                continue  
        if Miller(num) :
            return num

def Check_E(a,b):
    while (b!=0) :
        tmp = a ; a = b ; b = tmp%b
    if a == 1 :
        return True

# Select randomly two big unique prime numbers
P   = is_prime(1) # firts prime number
Q   = is_prime(2) # second prime number

# calculate N and P_N
N   = P * Q
P_N = (P-1)*(Q-1) 

# generate E
E = random.randint(2,999999999)
while Check_E(E,P_N) != True :
    E +=1
# by E valu Compute the value of D, Using the extended euclidean algorithm 
D = Euclidean(E,P_N)[0] % P_N
    
def Encryption(m) :
    return modular(m,E,N)

def Decryption_M(c) :
    return modular(c,D,N)

def Decryption_C(c) :
    dp = D % (P-1)          ; dq = D % (Q -1)
    mp = modular(c,dp,P)    ; mq = modular(c,dq,Q)
    yp = Euclidean(P,Q)[0]  ;  yq = Euclidean(P,Q)[1]

    return ((mp*yq*Q) + (mq*yp*P)) % (P*Q)

def main() :
    li = []
    with open('message.txt','r') as f :
        for line in f :
            for i in line :
                li.append(ord(i))

    with open('message.txt','w') as ff :
        print()
    with open('message.txt','a') as ff :
        for i in li :
            En = Encryption(i)
            print(En,file=ff)
            
    print()
    print('your message encrypted successfully')
    print()
    inp = int(input("Enter number 1 to decrypt your message by 'Fast modular exponentiation' or 2 by 'Chinese remainder theorem' : "))
 
    li2 = []
    with open('message.txt','r') as ff :
            if inp == 1 :
                for line in ff :
                    r2 = Decryption_M(int(line))
                    li2.append(r2)

                with open('message.txt','w') as ff :
                    print()
                with open('message.txt','a') as ff :
                        for i in li2 :
                            print(chr(i),end='',file=ff)

            if inp == 2 :
                for line in ff :
                    r2 = Decryption_C(int(line))
                    li2.append(r2)
                    
                with open('message.txt','w') as ff :
                    print()
                with open('message.txt','a') as ff :
                        for i in li2 :
                            print(chr(i),end='',file=ff)    

    print()
    print('your message decrypted successfully')
    print()

if __name__ == '__main__' :
    main()
