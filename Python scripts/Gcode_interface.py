#%%
"""
Created on Fri Dec 29 16:12:11 2017
Devloped by : Santosh Yadav
"""
"""
######################################################################################################
#####
#####             Rectangular Shape section
#####
######################################################################################################
"""
def rectangular():
    unit = input("Enter unit (In or Mm) : ")
    length=input("Enter the length of the Rectangular : ")
    width = input("Enter the width of the Rectangular : ")
    #Here sp_x,sp_y and sp_z is starting point cordinates of the shape and gc_unit is used for unit of shape which is inches or milimeter
    sp_x="0"
    sp_y="0"
    sp_z=""
    gc_unit =""
    feedrate = "F3000"
    gc_file=open("example.gcode","w")
    try :
        length=int(length)
        width=int(width) 
        x_cor=int(sp_x)+length
        y_cor=int(sp_y)+width
        x_cor=str(x_cor)
        y_cor=str(y_cor)
        if unit not in {"IN","in","In","iN","MM","Mm","mm","mM"}:
            print(unit,"is not a valid unit")
        else :
            if unit in {"IN","in","In","iN"}:
                gc_unit="G20"
            else :
                gc_unit="G21"
            gc_file.write("G90\n")
            gc_file.write(gc_unit+"\n")
            gc_file.write("G01 "+feedrate+"\n")
            gc_file.write("G01 "+"X"+sp_x+" "+"Y"+sp_y+" "+"\n")
            gc_file.write("G01 "+"X"+sp_x+" "+"Y"+y_cor+" "+"\n")
            gc_file.write("G01 "+"X"+x_cor+" "+"Y"+y_cor+" "+"\n")
            gc_file.write("G01 "+"X"+x_cor+" "+"Y"+sp_y+" "+"\n")
            gc_file.write("G01 "+"X"+sp_x+" "+"Y"+sp_y+" "+"\n")
            
    except :
        print("Enter value carefully : ")
#%%
"""
######################################################################################################
#####
#####             Circle Shape section
#####
######################################################################################################
"""
def circle():
#this section of program is for get GCODE for circle
    unit = input("Enter unit of measurments : ")
    rad= input("Enter radious here : ")
    radious=rad
    sp_x="0"
    sp_y="0"
    sp_z="0"
    feed_rate="300" #set feedrate here
    gc_file=open("Circle.gcode","w")
    try :
        rad=int(rad)
        print(unit)
        if unit not in {"IN","in","In","iN","MM","mm","Mm","mM"}:
            print(unit,"is not a valid measurment ")
        else:
            if unit in {"IN","in","In","iN"}:
                gc_file.write("G20"+"\n")
            else :
                gc_file.write("G21"+"\n")
            gc_file.write("G90"+"\n")
            gc_file.write("G01 "+"X"+sp_x+" "+"Y"+sp_y+" "+"F"+feed_rate+"\n")
            gc_file.write("G02 "+"X"+sp_x+" "+"Y"+sp_y+" "+"I"+radious+" "+"J0"+"\n")
        gc_file.close()
    except :
        print("Enter a valid value ")