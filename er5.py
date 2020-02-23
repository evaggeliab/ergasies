with open('ergasia5.txt') as textfile:
    word_list=[word for line in textfile for word in line.split()]
    for i in range (len(word_list)):
        s=word_list[i]
        if len(s)>3:
             word_list[i]=s[1:]+s[0]+"ay"
             print (word_list[i])
               
               
 
