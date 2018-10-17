isikukood = "39410204235"

def kontrollsumma(isikukood):
    """tagastab isikukoodi kontrollsumma)"""
    
    ikood=list(isikukood)
    sum1=0
    sum2=0

    for i in range (0,10):
       sum1= sum1+ (int(ikood[i])*(i+1))
    sum1 = sum1 + int(ikood[10])
    kontrollnr= sum1 % 10


    if kontrollnr == 10:
        for i in range (0,8):
           sum2= sum1+ (int(ikood[i])*(i+3))
        sum2 = sum1 + int(ikood[8]) + ((int(ikood[9])*2)) + ((int(ikood[10])*3))
        kontrollnr=sum2%(11)
        if kontrollnr == 10:
            kontrollnr == 0
            
    if kontrollnr == int(ikood[10]):
        kontroll = 0
    else:
        kontroll = 1
    
    print(kontrollnr)
    return(kontroll)

print(kontrollsumma(isikukood))