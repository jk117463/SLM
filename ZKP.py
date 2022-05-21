import sys
import random
import hashlib
n=997
text="Hello"
g= 3
print("Password:\t",text)
x = 7 #int(hashlib.md5(text).hexdigest()[:8], 16) % n
y= pow(g,x,n)
v = random.randint(1,n)
c = random.randint(1,n)
t = pow(g,v,n)
r = (v - c * x)
Result = ( pow(g,r,n) * pow(y,c,n))  % n
print ('======Agreed parameters============')
print ('P=',n,'\t(Prime number)')
print ('G=',g,'\t(Generator)')
print ('======The secret==================')
print ('x=',x,'\t(Prover\'s secret)')
print ('======Random values===============')
print ('c=',c,'\t(Verifier\'s random value)')
print ('v=',v,'\t(Prover\'s random value)')
print ('======Shared value===============')
print ('g^x mod P=\t',y)
print ('r=\t\t',r)
print ('=========Results===================')
print ('t=g**v % n =\t\t',t)
print ('( (g**r) * (y**c) )=\t',Result)
if (t == Result):
 print ('Prover has proven he knows password')
else:
 print ('Prover has not proven he knows password')