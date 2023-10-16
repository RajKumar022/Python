

# n=int(input("Enter the size of the array  :-"))
# a=[]
# i=0
# while(i<n):
#     value=int(input("Insert the value of the list :-"))
#     a.append(value)
#     i+=1
# print("Orignal list :- ",a)
# i=0
# while(i<n-1):
#     j=i+1
#     while(j<n):
#         if a[i]>a[j]:
#            temp=a[i]
#            a[i]=a[j]
#            a[j]=temp
#         j+=1
#     i+=1
# print("Sorted array :-",a)

#a=int(input("enter no>>>>"))
#if a==0 or a==1:
#  print("not prime")
#elif a==2 or a==3 or a==5 or a==7 :
#  print("prime no")
#elif a%2==0 or a%3==0 or a%5==0 or a%7==0 :
# print("not prime")
#else:
# print("prime no")
# 
# a=int(input("enter no>>>>"))
# if a%4==0 and a%100!=0 or a%400==0:
#   print("leap year")
# else:
#   print("normal year")

#a="repair"
#b=(a.capitalize())
#c=(b.replace("r","R"))
#print(a.title())
#b=(a.swapcase())
#print(b)
#c=(a[5].replace("r", "R"))
#b=(a[0:5])
#print(b+c)l

#a="apple"
#b=(a[1].replace("p","a"))
#c=(a[2].replace("p","a"))
#d=(a[0].replace("a","p"))
#e=(a[3:5])
#print(d+b+c+e)

#a="apple"
#b=(a[1].replace("p","a"))
#c=(a[3:5])
#d=(a[2])
#f=(a[0])
#e=(d+f+b+c)
#print(e)

#print("\U0001F420")

#a="raj"
#print("#".join(a))

#a="raj"
#print(a.lstrip())

#a="raj"
#b=(a.ljust(20))
#print(b,(20))

#a="\u0035" # unicode for 0
#print(a.isdecimal())


#a=int(input('enter value'))
#if a==1 or a==0:
#  print('not prime not composit')
#elif(a==2)or(a==3)or(a==5)or(a==7)or(a==11)or(a==13)or(a==17)or(a==19):
#  print('prime number')
#elif(a%2==0)or(a%3==0)or(a%5==0)or(a%7==0)or(a%11==0)or(a%13==0)or(a%17==0)or(a%19==0):
#  print('composite number')
#else:
#  print('prime number')

#a=1012
#b=(a%100)*100
#print(b)

#a=23456
#b=a%100
#c=a%1000
#d=c//100
#e=a//1000
#print((e*1000+b*10)+d)

#a="raj\n"
#print((a)*100)

#a=8
#b=4
#c=a
#a=b
#b=c
#print (a)
#print(b)

#a=6
#b=5
#a=a+b
#b=a-b
#a=a-b
#print(a)
#print(b)

#a=6
#b=8
#a=a^b
#b=a^b
#a=a^b
#print(a)
#print(b)

#a=6
#b=4
#a, b=b, a
#print(a)
#print(b)

#a=20
#b=5
#c=a
#d=10
#e=b
#f=(a*b)*(d*e)
#b=(f*c*b)
#d=(f*a/b)
#print(e), (b), (f), (d), (c), (a)

#a=1200
#b=bool(a)
#print(b)

#a=6
#b=8
#a=a^b
#b=a^b
#a=a^b
#print(a)
#print(b)

#a=6
#b=4
#a, b=b, a
#print(a)
#print(b)

#a=20
#b=5
#c=a
#d=10
#e=b
#f=(a*b)*(d*e)
#b=(f*c*b)
#d=(f*a/b)
#print(e), (b), (f), (d), (c), (a)

#a=1200
#b=bool(a)
#print(b)

#num=int(input("enter number >>>>>>")
#if num > 1 
#  for i in range (2,num):
#        if num % i == 0 :
#           print("not prime")
#else :
#         print("prime")

 #CALCULATOR >>>>>>>>>>>>>>>>>>>>>>>>>>>>

# print("<<<<< calculater>>>>>")
# a=float(input("enter the no>>>"))
# b=float(input("enter the no>>>"))
# print(''' press 1 for addition\n press 2 for Substrection\n press 3 for multiplication\n press 4 for division
# ''')
# choice= int(input("enter the choice 1 to 4>>>>>>"))
# if choice == 1:
#  print(a + b)
# elif choice == 2:
#  print(a - b )
# elif choice ==3:
#  print(a * b)
# elif choice == 4:
#  if  b==0:
#    print("divide by 0 error")
#  else:
#    print(a / b)
# else:
#  print("invalid choice")

#a=int(input("enter no"))
#if a%4==0 and a%100 !=0 or a%400==0:
#  print("leap year")
#else :
#  print("not leap year")

#import calendar
#year=int(input("enter the year"))
#month=int(input("enter the month>>"))
#print(calendar.month(year,month))

#a=int(input("enter no>>>>"))
#if a==2 or a==3 or a==5:
#  print("prime no")
#elif a==1 or a%2==0 or a%3==0 or a%5==0:
#  print("not prime no")
#else:
#  print("prime")

#a=input("enter username>>>>>>")
#if a=="raj":
#  b=input("enter your password>>>>>")
#  if b=="raj@123":
#    print("login success")
#  else:
#    print("incorrect password")
#else:
#  print("inccorect user name")

#import datetime
#x = datetime.datetime.now()
#print(x)

#a=int(input("enter no>>>>>"))
#b=int(input("enter no>>>>>"))
#c=int(input("enter no>>>>>"))
#d=int(input("enter no>>>>>"))
#if a==b and b==c and c==d and d ==a :
#  print("no one is second max")
#elif a==b and (b>c and c>d):
#  print(c)
#elif a>b and (b==c and c>d):
#  print(b)
#elif a>c and (c>b and c==d):
# print(d)
#elif b>c and (d>c and a==d):
# print(a)
#elif a==b and b==c and d>c:
#   print(a)
#elif a>b and b==c and c==d :
# print(b)
#elif a>b and b>c and c>d and d<a :
# print(b)
#elif c>b and b>d and d>a and a<c:
# print(b)
#elif d>b and b>a and a>c and c<d:
#  print(b)
#elif a<b and b<c and c<d and d>a:
#  print(c)
#elif a>c and c>d and d>b and b<a:
#  print(c)
#elif d>c and c>a and a>b and b<d:
#  print(c)
#elif b>d and d>c and c>a and a<b:
# print(d)
#elif a>d and d>c and c>b and b<a:
#  print(d)
#elif c>d and d>a and a>b and b<c:
#  print(d)
#elif c>d and d>b and b>a and a<c:
#  print(d)
#elif d>b and b>c and c>a and a<d:
#  prit(b)
#elif a>c and c>b and b>d and d<a:
#  print(c)
#elif a>d and d>b and b>c and c<a:
#  print(d)
#elif b>c and c>d and d>a and a<b:
#  print(c)
#elif b>c and c>a and a>d and d<b:
#  print(c)
#else :
#  print (a)

#a=int(input("enter no"))
#if a%3==0:
#  continue
#else :
# print("true")

#a=int(input("enter no"))
#if a%5==10:
#    break
#else:
#  print("true")

#"<<<<<<<ATM MACHINE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
#print("Welcome to ATM")
#print("insert your card")
#password=2403
#Amount=100000
#print('''1=check balance\n2=Deposite\n3=withdraw amount''')
#pin=int(input("enter pin>>>"))
#if pin==2403:
#     print ("choice option")
#     choice=int(input("enter no>>>"))
#     if choice==1:
#         print("check Balance=",Amount)
#     elif choice==2:
#       dep=int(input("enter  amount="))
#       print ("balance in bank=",Amount)
#       Amount= dep+Amount
#       print("deposite amount=",dep)
#       print ("TotalAmount=",Amount) 
#     elif choice==3:
#       wit=int(input("enter withdraw amount="))
#       if wit>100000:
#            print("please withdraw less than than Amount")
#       elif wit <=Amount:
#            Amount=Amount-wit
#            print("withdraw Amount=",wit)
#            print("check Amount=",Amount)
#            print("collect your Amount")
#       else:
#            print ("please withdraw less than Deposit Amount")
#     else:
#       print("invalid choice")
#else:
#  print("invalid pin")
#print("thank for visit")


#a=input("enter length>>>>>>")
#if len(a) ==8:
#  if (("a"in a) or ("b"in a) or ("c"in a) or ("d"in a) or ("e"in a ) or ("f"in a) or ("g"in a) or ("h"in a) or ("i"in a) or ("j"in a) or ("k"in a) or ("l"in a) or ("m"in a) or ("n"in a) or ("o"in a) or ("p"in a) or ("q"in a) or ("r"in a) or ("s"in a) or ("t"in a) or ("u"in a) or ("v"in a) or ("w"in a) or ("x"in a)or ("y"in a) or ("z"in a)) and (("A"in a) or ("B"in a) or ("C"in a) or ("D"in a) or ("E"in a) or ("F"in a) or ("G"in a) or ("H"in a)or ("I"in a) or ("J"in a) or ("K"in a) or ("L"in a) or ("M"in a) or ("N"in a) or ("O"in a) or ("P"in a) or ("Q"in a) or ("R"in a) or ("S"in a) or ("T"in a) or ("U"in a) or ("V"in a) or ("W"in a) or ("X"in a) or ("Y"in a) or ("Z"in a)) and (("0"in a) or ("1"in a) or ("2"in a) or ("3"in a) or ("4"in a) or ("5"in a) or ("6"in a) or ("7"in a) or ("8"in a) or ("9"in a)) and (("@"in a)or ("#"in a) or ("₹"in a) or ("&"in a) or ("?"in a) or ("/"in a)) :
#    print("correct password")
#else:
#  print("invalid password")

#if 2==2:
#  print("python is easy")

#a=b=true
#if(a and b):
#  print("hello")
#else:
#  print("know your program")

#i=1
#while i<=100:
#  print(i)
#  i+=1

#a=int(input("enter no>>>>>>"))
#print("last digit of number is",a%10)


#a=[" apple","banana"]
#b=["papaya","ape"]
#a.extend(b)
#print(a)

#a=["apple","banana"]
#a.clear()
#print(a)

#a=[1,2,4]
#b=[2,4]
#c=a+b
#print(c)

#a=[1, 2,3,4,5,6,7,8,9,11,12,13,14,15,16]
#l=0
#r=16
#x=int(input("enter no >>>"))
#while  l<r :
#  y=l-(r-l)//2
#  if x<y:
#    r==y
#    if x>y:
#      l==y
#  else:
#    print("x")
   


#a, b= map(int, input ().split())
#c=a*b
#d=a-b
#print(abs(c-d))

#t = int(input())
#for i in range(t):
#    l = list(map(int,input().split()))
#    alice = l[0:3]
#    bob = l[3:6]
#    alice.sort()
#    bob.sort()
#    if(alice[1] + alice[2] > bob[1] + bob[2]):
#        print("Alice")
#    elif(alice[1] + alice[2] < bob[1] + bob[2]):
#        print("Bob")
#    else:
#        print("Tie")



#T=int(input ())
#for i in range (T):
#    A, B= map(int, input (). split ()) 
#if A<B:
#    print ('<')
#elif A>B:
#    print ('>')
#else:
#    print ('=')

#n=int(input("enter no>>>>"))
#a=1
#while a<=n:
#  j=1
#  while j<=a:
#     print ( "*",end="")
#     j+=1
#  a+=1
#  print()


#n=int(input("enter no>>>>>>")) 
#while n>0:
#    j=1
#    while j<=n:
#       print('+', end=" ")
#       j+=1
#    n-=1
#  #  print( )

#n=int(input(" enter no >>>>>>"))
#a=1
#b=" "
#b=n-1
#while a<=n:
#  j=1
#  while j<=a:
#     print("b","#",end=" ")
#     j+=1
#   
#   print()

#n=int(input("enter no>>>>"))
#a=[]
#i=0
#while i<=n:
#    m=0
#    p=i
#    x=i 
#    while p>0:
#      b=p%10
#      m+=1
#      p=p//10
#    sum=0
#    while x>0:
#      c=x%10
#      sum=sum+(c**10)
#      x=x%10
#    if sum==i:
#      a+=[i]
#    i+=1
#print(a)

#for i in range(int(input())):
#    a=list(map(int,input().split()))
#    alice=a[:3]
#    bob=a[3:]
#    alice.remove(min(alice))
#    bob.remove(min(bob))
#    a_score=sum(alice)
#    b_score=sum(bob)
#    if(a_score>b_score):
#        print("Alice")
#    elif(b_score>a_score):
#        print("Bob")
#    else:
#        print("Tie")


# a=[44,3,88,2,89,24,11,76]
# i=0
# l=8
# while i<=l:
#    j=i+1
#    while j<l:
#      if (a[i]>a[j]):
#        t=a[i]
#        a[i]=a[j]
#        a[j]=t
#      j+=1
#    i+=1
# print(a[l-2])


#a=[1,5,6,8,12,85,7,18,11,3,2]
#h=11
#l=0
#k=11
#m=l+((h-l)/2)
#while l<h:
#         if m==k:
#           print(m)
#             while k<=m:
#               h=m-1
#             l=m+1
#print(k)       

# 
#n=int(input("enter no >>>"))
#i=0
#a=[]
#while i<n:
#      b=int(input("enter no>>>>"))
#      a.append (b)
#      i+=1
#a. sort()
#print(a[2])

#for i in range (1,10):
#     print(i)
#     if i==4:
#       continue 
#       break
#       I+=1

     
          
#i=1
#while i<10  :
#       if i==4:
#           continue
#       print(i)
#       i+1


#i=3
#while i<6:
#  print(i)
#  i+=1
#else:
#  print("i is no longer less than 6")


#n=int(input ("enter the value of number>>>>>"))
#i=2
#while i<=n:
#  i+=2
#  print(i)

#a=int(input("enter no>>>>>>>>"))
#for i in range(11):
#   print(2*i)

#a=int(input("enter no>>>>>>"))
#i=1
#while i<=10:
#  print(a*i)
#  i+=1

#n=int(input("enter no>>>>"))
#i=2
#while n>=i:
#  a=0
#  for m in range (2,i):
#    if i%2==0:
#      a=1
#      break
#  i+=1
#if a==0:
#  print(i)

#i=1
#while (i<=10):
#  i+=1
#  if (i==5):
#    continue
#  print(i)

#i=int(input("enter no>>>>>>>"))
#while(i<21):
#   print(i)
#   i+=2

#n=int(input("enter no>>>>"))
#i=1
#while i<=2:
#  dig=n%10
#  n=n//10
#  i=i+1
#if dig==7:
#  print("yes")
#else:
#  print("no")

#for i in range(2,21,2):
#  print (i)




#n=int(input("enter the number>>>.."))
#i=2
#while n>=1:
#  flag=0
#  for x in range(2,i):
#    if i%2==0:
#       flag=1
#       break
#  i=i+1
#if flag==1:
#  print(i)


#i=1
#while i <=100:
#  if i%7==0:
#    print(i)
#  i+=1

#i=1
#while i<=100:
#  if i%2==0:
#    print(i*-1,end="")
#  else:
#    print(i,end="")
#  i+=1

#i=10
#while i<=100:
#  print(i)
#  i+=1

#i=5
#while i<=50:
#    print(i)
#    i+=5

#i=50
#while i<=50:
#  if i%2==0:
#    print(i)
#  i+=5

# n=input("enter no>>>>>")
# sum=0
# i=0
# while (i<=n):
#   a=input("enter no>>>>>>")
#   sum+=i
#   i+=1
# print(sum)

# n=int(input("enter no>>>>"))
# x=0
# while(n>0):
#     a=" "
#     a+=x*" "
#     a+=str((2*n-1)*"*")
#     print(a)
#     a=" "
#     n-=1
#     x+=1

# n=int(input("enter no>>>>"))
# i=0
# while(i<n):
#     j=0
#     while (j<i):
#       print(" ",end="")
#       j+=1
#     a=0
#     while(a<2*(n-i)-1):
#       print("*",end="")
#       a+=1
#     print("")
#     i+=1

# n=int(input("enter no>>>>"))
# i=1
# while(i<=n):
#     count=0
#     j=1
#     while(j<=i):
#       if (i%j==0):
#          count+=1
#       j+=1
#     if count==2:
#        print ("prime no>>>>>",i)
#     i+=1


# n=int(input("enter no>>>>"))
# i=1
# count=0
# while(i<=n):
#     if(n%i==0):
#       count+=1
#     i+=1
# if count==2:
#    print ("prime no")
# else:
#    print("not a prime no")


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# a=int(input("enter no>>>>"))
# b=int(input("enter no>>>>"))
# c=int(input("enter no>>>>"))
# d=int(input("enter no>>>>"))
# max=0
# sndmax=0
# if (a>b):
#     max=a
#     sndmax=b
# if(b>a):
#     max=b
#     sndmax=a
# if (max>c):
#     if(sndmax>c):
#         sndmax=sndmax
#     else :
#         sndmax=c
# else:
#     sndmax=max
#     max=c
# if (max>d):
#     if (sndmax>d):
#         sndmax=max
#     else :
#         sndmax=d
# else :
#     max=d
        

# a=int(input("enter no"))
# i=1
# sp=a-1
# while i<=a:
#     print(" "*sp+"*"*i)
#     sp-=1
#     i+=1

# N, R = map(int, input().split())
# ratings = list(map(int, input().split()))

# # Process each contestant's rating
# for rating in ratings:
#     if rating >= R:
#         print("Good boi")
#     else:
#         print("Bad boi")

# class Solution:
#     def intToRoman(self, num: int) -> str:
#         # Creating Dictionary for Lookup
#         num_map = {
#             1: "I",
#             5: "V",    4: "IV",
#             10: "X",   9: "IX",
#             50: "L",   40: "XL",
#             100: "C",  90: "XC",
#             500: "D",  400: "CD",
#             1000: "M", 900: "CM",
#         }
        
#         # Result Variable
#         r = ''
        
        
#         for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
#             # If n in list then add the roman value to result variable
#             while n <= num:
#                 r += num_map[n]
#                 num-=n
#         return r



    
 

# n,m,p=map(int,input().split())
# count=0
# a=1
# b=1
# if n>=m:
#     while b<=n:
#         b=m+(p*a)
#         count+=1
#         a+=1
#     print(count)
# print(0)

# for i in range (int(input())):
#     x,h=map(int,input().split())
#     d=h//x+3
#     if (x<h and h%x!=0):
#         print(x)
#     elif(h<x):
#         print(h)
#     else:
#         print(d)

# ALL EVEN NUMBER AND ODD NUMBER >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
# num = int(input("Enter a number: "))
# even_numbers = ""
# odd_numbers = ""
# natural_numbers = ""
# i = 1
# while i <= num:
#    natural_numbers += str(i) + " "
#    if i % 2 == 0:
#        even_numbers += str(i) + " "
#    else:
#        odd_numbers += str(i) + " "
#    i += 1

# print("Even numbers from 1 to", num, ":", even_numbers)
# print("Odd numbers from 1 to", num, ":", odd_numbers)
# print("Natural numbers from 1 to", num, ":", natural_numbers)


# a=[34,46,55,83,11,49]
# a.sort(reversed=True)
# print(a)
