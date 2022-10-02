import matplotlib.pyplot as plt        #importing required modules
from random import randint as r
def die2coin(m ,N):                    #making a function
    H=0                                #make variable H & T to respectively
    T=0                                #initialise number of heads and tails from 0
    for i in range(N):                 #run a loop for number of throws
        n=r(1,6)                       #randomly take any number from 1 to 6 as in die
        if( m == 1):                   #checking the type of method
            if (n == 1) or(n == 2) or (n == 3):
                H = H+1                #H or T based on situation by 1
            else:
                T=T+1
        if(m==2):
             if (n == 1):
                  H = H+1
             elif(n == 2):
                  T=T+1   
        if(m==3):
            if (n == 2) or (n == 3):
                H = H+1
            elif (n==4) or (n==5):
                T=T+1
    print("Head occurs ",H,"times")    #printing total no. of H & T
    print("Tail occurs ",T,"times") 
    #Ploting the bar graph
    plt.bar(["Heads","Tails"],[H,T], color ='maroon')
    plt.xlabel("Outcomes")             #labelling the graph
    plt.ylabel("No. of outcomes")
    plt.show()
m=int(input("type of method:"))
N=int(input("no. of times to repeat:",))
die2coin(m,N)