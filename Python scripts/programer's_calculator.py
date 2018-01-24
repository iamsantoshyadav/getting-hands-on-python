"""
#############################################################################################################
##
##              This is Decimal to binary conversion section
##
######################################################################################################
"""
#this program is about conversion of dcimal no into a binary no
def dec_to_binary(ip):
    try :
        dec = int(ip)
        binno = []
        #All the magic begins here
        while dec!=0:
            rem=dec%2
            binno.append(rem)
            dec=int(dec/2)
                
    except :
        #Error message for the users
        print("You did not entered a valid value Please try again")
    #List(reversed(list_name) is use for reverse the list)
    str_bin=""
    binno = list(reversed(binno)) 
    for no in range(len(binno)):
        string=str(binno[no])
        str_bin=str_bin+string
    return(str_bin)    
"""
#############################################################################################################
##
##              This is binary to decimal conversion section
##
######################################################################################################
"""
#this program is for performing binary to decimal conversion
def binary_to_dec(ip):
    deci=0
    data=[]
    ip = str(ip)
    length= len(ip)
    try :
        #Logic for converting n_bit no into a single no or single bit no
        for nos in range(length):
            integers=int(ip[nos])
            #Storing all the single bit into a single variable or list
            data.append(integers)
        i=0
        
        #All the magics begin here
        for nos in range(len(data)-1,-1,-1):
            if data[nos]not in {0,1}:
                print("Enter a valid binary no")
                deci=0
                break
            else :
                i=(len(data)-1)-nos
                deci=deci+((data[nos]*2)**i) #Logic for binary to decimal conversion
        if deci>0:
            print("Dcimal equivelent no of ",data,"is",deci)
            return(deci)
        else :
            print("For given no ",data,"operation can't perform PLEASE TRY AGAIN")
            
    except :
        print("You did not entered a valid value PLEASE ENTER BINBARY NO CAREFULLY")

"""
#############################################################################################################
##
##              This is Decimal to Octal conversion section
##
######################################################################################################
"""
# THis function is for converting decimal no into octal no
def dec_to_octal(ip):
    data=[]
    try :
        dec=int(ip)
        while dec!=0:
            rem=dec%8
            data.append(rem)
            dec=int(dec/8)
        data=list(reversed(data))
        strdata=""
        for no in range(len(data)):
            string=str(data[no])
            strdata=strdata+string
        print("Octal conversion of decimal no ",ip,"is",strdata)
        return(strdata)
    except :
        print("Enter a valid decimal value carefully");

"""
#############################################################################################################
##
##              This is octal to decimal conversion section
##
######################################################################################################
"""
def octal_to_decimal(ip):
    data=[]
    deci=0
    try :
        ip=str(ip)
        length=len(ip)
        for nos in range(length):
            data1=int(ip[nos])
            data.append(data1)
        for no in range(length-1,-1,-1):
            if data[no] not in {0,1,2,3,4,5,6,7}:
                print("Entered no. is not an octal no Please try again")
                deci=0
                break
            else :
                i=(length-1)-no
                deci=deci+(data[no]*(8**i))
        if deci>0 :
            return(deci)
        else :
            print("Operation can not be purform for no ",ip)
            
    except :
        print("You have not entered a valid value Please enter a valid octal no")

"""
#############################################################################################################
###
###             This is octal to binary conversion section
###
######################################################################################################
"""
def octal_to_binary():
    ip=input("Enter a octal no : ")
    try :
        ip=int(ip)
        check=str(ip)
        for nos in check :
            nos=int(nos)
            if nos not in {0,1,2,3,4,5,6,7} :
                print("Entered value is not an octal no : ")
                break
        dec=octal_to_decimal(ip)
        binary=dec_to_binary(dec)
        print("Binary  value is : ",binary)
    except :
        print("Entered no is not a valid value please enter carefully :")
"""
#############################################################################################################
###
###             This is Decimal to Hexadecimal conversion section
###
######################################################################################################
"""
def decimal_to_hex(ip):
    ip=str(ip)
    hex_no=[]
    try :
        ip=int(ip) #it will fail for string case for example argument id as334 etc
        data=ip
        while data!=0:
            rem=data%16
            hex_no.append(rem)
            data=int(data/16)
        hex_no=list(reversed(hex_no))
        for no in range(len(hex_no)):
            hex_no[no]=str(hex_no[no])
            if hex_no[no]=="10" :
                hex_no[no]="A"
            if hex_no[no]=="11":
                hex_no[no]="B"
            if hex_no[no]=="12":
                hex_no[no]="C"
            if hex_no[no]=="13":
                hex_no[no]="D"
            if hex_no[no]=="14":
                hex_no[no]="E"
            if hex_no[no]=="15":
                hex_no[no]="F"
        hex_str=""
        for no in hex_no:
            hex_str=hex_str+no
        return(hex_str)
    except :
        print("Enterde value is not a valid no Please try again ")
"""
#############################################################################################################
###
###             This is Hexadecimal to Decimal conversion section
###
######################################################################################################
"""
def hex_to_dec(ip):
    data=[]
    hexa=None
    ip=str(ip)
    for word in ip :
        if word not in {"a","b","c","d","e","f","A","B","C","D","E","F","0","1","2","3","4","5","6","7","8","9"}:
            print("Enter avalid hexadecimal no ")
            hexa=0
        else :
           data.append(word)
    for no in range(len(data)) :
        if data[no] in {"a","A"}:
            data[no]=10
        if data[no] in {"b","B"}:
            data[no]=11
        if data[no] in {"c","C"} :
            data[no]=12
        if data[no] in {"d","D"} :
            data[no]=13
        if data[no] in {"e","E"}:
            data[no]=14
        if data[no] in {"f","F"}:
            data[no]=15
        data[no]=int(data[no])
    data=list(reversed(data))
    sums=0
    for no in range(len(data)) :
        powr=16**no
        sums=sums+(data[no]*powr)
    if hexa==0:
        return(0)
    else :
        decimal=str(sums)
        return(decimal)

"""
#############################################################################################################
###
###             This is Hexadecimal to Binary conversion section
###
######################################################################################################
"""
def hex_to_bin():
    ip=input("Enter a Hexadecimal no : ")
    for word in ip :
        if word not in {"a","b","c","d","e","f","A","B","C","D","E","F","0","1","2","3","4","5","6","7","8","9"}:
            print("Enter avalid hexadecimal no ")
        else :
            deci=hex_to_dec(ip)
            deci=int(deci)
            binary=dec_to_binary(deci)
    print("binary : ",binary)

"""
#############################################################################################################
###
###             This is Binary to Hexadecimal conversion section
###
######################################################################################################
"""
def bin_to_hex() :
    ip=input("Enter a binary no : ")
    hex_str=None
    try :
        ip=str(ip)
        for word in ip :
            if word not in {"0","1",} :
                print(ip,"is not a binary no ")
                hex_str=0
                break
        if hex_str!=0 :
            deci=binary_to_dec(ip)
            hex_str=decimal_to_hex(deci)
            return(hex_str)
    except :
        print("Please enter a valid value")
"""
#############################################################################################################
###
###             This is hexadecimal to Octal conversion conversion section
###
######################################################################################################
"""
def hex_to_oct(ip) :
    ip=str(ip)
    for words in ip :
        if words not in {"a","b","c","d","e","f","A","B","C","D","E","F","0","1","2","3","4","5","6","7","8","9"}:
            print("Enter a valid hex no")
            ip=None
            break
    if ip!=None :
        dec=hex_to_dec(ip)
        octal=dec_to_octal(dec)
        return(octal)
#%%
"""
#############################################################################################################
###
###             This is Octal to Hexadecimal conversion conversion section
###
######################################################################################################
"""
def oct_to_hex() :
    ip=input("Enter a octal no : ")
    try : 
        ip=int(ip)
    except :
        ip=None
        print("Enter a valid octal no ")
    if ip!=None:
        ip=str(ip)
        for word in ip :
            if word not in {"0","1","2","3","4","5","6","7"}:
                print("Given no is not a ocatl no")
                break
        dec=octal_to_decimal(ip)
        hexa=decimal_to_hex(dec)
        return(hexa)
        
        