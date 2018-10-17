isikukood = "39506250234" # vale kood nt 39506250234

def kontrollsumma(isikukood):
    """tagastab isikukoodi kontrollsumma)"""
    
    ikood=list(isikukood)
    sum1=0

    for i in range (0,9):
       sum1= sum1+ (int(ikood[i])*(i+1))
    sum1 = sum1 + int(ikood[9]) # viimane kaal on 1 sp liidab siin
    kontrollnr= sum1 % 11


    sum1=0
    if kontrollnr == 10:
        for i in range (0,7):
           sum1 = sum1 + (int(ikood[i])*(i+3))
        sum1 = sum1 + int(ikood[7]) + ((int(ikood[8])*2)) + ((int(ikood[9])*3))
        kontrollnr=sum1 % (11)
        if kontrollnr == 10:
            kontrollnr == 0
    
            
    if kontrollnr == int(ikood[10]):
        kontroll = 0
    else:
        kontroll = 1
    
    
    return(kontroll)


print(kontrollsumma(isikukood))