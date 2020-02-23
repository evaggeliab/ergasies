with open('ergasia2.txt') as textfile:
    word_list=[word for line in textfile for word in line.split()]
    for i in range (len(word_list)):
        c=0
        c1=0
        s=word_list[i]
        for j in range(len(s)):
            y=s[j]
            if (y=="f"or y=="c" or y=="r" or y=="k"):
                c=c+1
            else :  
                c1=c1+1
        if (c>c1):
            print ("kakh leksh!!")
        else:
            print ("kalh leksh!!")