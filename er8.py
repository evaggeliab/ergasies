import random
signal1=random.randint(0,20)
signal2=random.randint(0,20)
signal3=random.randint(0,20)
if (max(signal1,signal2,signal3)==signal1):
    green=random.randint(5,10)
    red2=random.randint(0,5)
    red3=random.randint(0,5)
    signal1=signal1-green
    signal2+=red2
    signal3+=red3
    print("το πρωτο φαναρι ειναι πρασινο.Πριν το αναμα ειχε",signal1+green,"αυτοκινητα.Μετα το αναμα εφυγαν",green,"αυτοκινητα.Το δευτερο και 3ο φαναρι ειναι κοκκινα.Πριν το αναμα ειχαν",signal2-red2,signal3-red3,"αυτοκινητα αντιστοιχα και μετα το αναμα  ηρθαν",red2,red3,"αυτοκινητα αντιστοιχα")
elif (max(signal1,signal2,signal3)==signal2):
    green=random.randint(5,10)
    red1=random.randint(0,5)
    red3=random.randint(0,5)
    signal2=signal2-green
    signal1+=red1
    signal3+=red3
    print ("το δευτερο φαναρι ειναι πρασινο.Πριν το αναμα ειχε" ,signal2+green, "αυτοκινητα.Μετα το αναμα εφυγαν",green,"αυτοκινητα.Το 1ο και 3ο φαναρι ειναι κοκκινα.Πριν το αναμα ειχαν",signal1-red1,signal3-red3,"αυτοκινητα αντιστοιχα και μετα το αναμα  ηρθαν",red1,red3,"αυτοκινητα αντιστοιχα")
elif(max(signal1,signal2,signal3)==signal3):
    green=random.randint(5,10)
    red1=random.randint(0,5)
    red2=random.randint(0,5)
    signal3=signal3-green
    signal1+=red1
    signal2+=red2
    print ("το τριτο φαναρι ειναι πρασινο.Πριν το αναμα ειχε",signal3+green,"αυτοκινητα.Μετα το αναμα εφυγαν",green,"αυτοκινητα.Το 1o και 2ο φαναρι ειναι κοκκινα.Πριν το αναμα ειχαν",signal1-red1,signal2-red2,"αυτοκινητα αντιστοιχα και μετα το αναμα  ηρθαν",red1,red2,"αυτοκινητα αντιστοιχα")
elif ((max(signal1,signal2,signal3)==signal1) and (max(signal1,signal2,signal3)==signal2)):
 if (random.choice("signal1","signal2")=="signal1"):
  green=random.randint(5,10)
  red2=random.randint(0,5)
  red3=random.randint(0,5)

  signal1=signal1-green
  signal2+=red2
  signal3+=red3
  print("το πρωτο φαναρι ειναι πρασινο.Πριν το αναμα ειχε",signal1+green,"αυτοκινητα.Μετα το αναμα εφυγαν",green,"αυτοκινητα.Το δευτερο και 3ο φαναρι ειναι κοκκινα.Πριν το αναμα ειχαν",signal2-red2,signal3-red3,"αυτοκινητα αντιστοιχα και μετα το αναμα  ηρθαν",red2,red3,"αυτοκινητα αντιστοιχα")
 else:
    green=random.randint(5,10)
    red1=random.randint(0,5)
    red3=random.randint(0,5)
    signal2=signal2-green
    signal1+=red1
    signal3+=red3
    print ("το δευτερο φαναρι ειναι πρασινο.Πριν το αναμα ειχε" ,signal2+green ,"αυτοκινητα.Μετα το αναμα εφυγαν",green,"αυτοκινητα.Το 1ο και 3ο φαναρι ειναι κοκκινα.Πριν το αναμα ειχαν",signal1-red1,signal3-red3,"αυτοκινητα αντιστοιχα και μετα το αναμα  ηρθαν",red1,red3,"αυτοκινητα αντιστοιχα")
elif ((max(signal1,signal2,signal3)==signal1) and (max(signal1,signal2,signal3)==signal3)):
      if (random.choice("signal1","signal2")=="signal1"):
       green=random.randint(5,10)
       red2=random.randint(0,5)
       red3=random.randint(0,5)
       signal1=signal1-green
       signal2+=red2
       signal3+=red3
       print("το πρωτο φαναρι ειναι πρασινο.Πριν το αναμα ειχε",signal1+green,"αυτοκινητα.Μετα το αναμα εφυγαν",green,"αυτοκινητα.Το δευτερο και 3ο φαναρι ειναι κοκκινα.Πριν το αναμα ειχαν",signal2-red2,signal3-red3,"αυτοκινητα αντιστοιχα και μετα το αναμα  ηρθαν",red2,red3,"αυτοκινητα αντιστοιχα")
      else:
       green=random.randint(5,10)
       red1=random.randint(0,5)
       red2=random.randint(0,5)
       signal3=signal3-green
       signal1+=red1
       signal2+=red2
       print ("το τριτο φαναρι ειναι πρασινο.Πριν το αναμα ειχε",signal3+green,"αυτοκινητα.Μετα το αναμα εφυγαν",green,"αυτοκινητα.Το 1o και 2ο φαναρι ειναι κοκκινα.Πριν το αναμα ειχαν",signal1-red1,signal2-red2,"αυτοκινητα αντιστοιχα και μετα το αναμα  ηρθαν",red1,red2,"αυτοκινητα αντιστοιχα")
elif ((max(signal1,signal2,signal3)==signal2) and (max(signal1,signal2,signal3)==signal3)):
 if random.choice("signal2","signal3")=="signal2":
    green=random.randint(5,10)
    red1=random.randint(0,5)
    red3=random.randint(0,5)
    signal2=signal2-green
    signal1+=red1
    signal3+=red3
    print ("το δευτερο φαναρι ειναι πρασινο.Πριν το αναμα ειχε" ,signal2+green, "αυτοκινητα.Μετα το αναμα εφυγαν",green,"αυτοκινητα.Το 1ο και 3ο φαναρι ειναι κοκκινα.Πριν το αναμα ειχαν",signal1-red1,signal3-red3,"αυτοκινητα αντιστοιχα και μετα το αναμα  ηρθαν",red1,red3,"αυτοκινητα αντιστοιχα")
 else:
      green=random.randint(5,10)
      red1=random.randint(0,5)
      red2=random.randint(0,5)
      signal3=signal3-green
      signal1+=red1
      signal2+=red2
      print ("το τριτο φαναρι ειναι πρασινο.Πριν το αναμα ειχε",signal3+green,"αυτοκινητα.Μετα το αναμα εφυγαν",green,"αυτοκινητα.Το 1o και 2ο φαναρι ειναι κοκκινα.Πριν το αναμα ειχαν",signal-red1,signal2-red2,"αυτοκινητα αντιστοιχα και μετα το αναμα  ηρθαν",red1,red2,"αυτοκινητα αντιστοιχα")
     
     

           
    
    



        
