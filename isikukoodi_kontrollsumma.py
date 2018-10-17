isikukood = "39506250243"

def kontrollsumma(isikukood):
    """tagastab isikukoodi kontrollsumma)"""
    
    ikood=list(isikukood)
    sum1=0
    sum2=0

    for i in range (0,9):
       sum1= sum1+ (int(ikood[i])*(i+1))
    sum1 = sum1 + int(ikood[9]) # viimane kaal on 1 sp liidab siin
    print(sum1)
    kontrollnr= sum1 % 11
    print(kontrollnr)

    
    if kontrollnr == 10:
        for i in range (0,7):
           sum2 = sum2 + (int(ikood[i])*(i+3))
           print(sum2)
        sum2 = sum2 + int(ikood[7]) + ((int(ikood[8])*2)) + ((int(ikood[9])*3))
        kontrollnr=sum2 % (11)
        print(kontrollnr)
        if kontrollnr == 10:
            kontrollnr == 0
    
            
    if kontrollnr == int(ikood[10]):
        kontroll = 0
    else:
        kontroll = 1
    
    print(kontrollnr)
    return(kontroll)
print("hei")

print(kontrollsumma(isikukood))