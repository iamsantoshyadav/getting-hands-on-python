#%%
"""
Created on Fri Dec 26 13:23:14 2017
Devloper: Santosh yadav
Title - User to G-code Interface
"""
def rectangular(unit,length,width):
#Simple program for plotting a rectangular
#3 Inputs we are going to take from the user length width and unit (Inch or MM)

    try :
        unit=str(unit)
        length=str(length)
        width =str(width)
        gc_file = open("rectangular.gcode","w")
        if unit in {"in","In","IN"}:
            gc_file.write("G90\n")
            gc_file.write("G20\n")
            gc_file.write("G1 F300\n")
            gc_file.write("G1 "+"X0 "+"Y"+width+"\n")
            gc_file.write("G1 "+"X"+length+" Y"+width+"\n")
            gc_file.write("G1 "+"X"+length+" Y0"+"\n")
            gc_file.write("G1 "+"X0"+" Y0"+"\n")

        gc_file.close()
    
    except :
        print("Enter valid input PLEASE TRY AGAIN"  )
