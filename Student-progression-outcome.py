#I declare that my work contains no examples of misconduct,such as plagiarism,or collusion.
#Any code taken from other sources is referenced within my code solution
#Student ID: 19115425
#Date: 18/04/2022

#Initializing Variables - integer
Pass=0
defer=0
fail=0
pro_count=0
promod_count=0
noprog_count=0
exc_count=0
tot_count=0
total=0
#Initializing variales - String
entry=""
prog_star=""
pro_mod_star=""
Noprog_star=""
exc_star=""
#Initializing variales - List
List=[]
#Initializing variales - Boolean
#At the start the variable boolean is set to True
boolean= True

while boolean:
    #Part1 
    try:
        print()
        #Validation
        #The program would run only if the inputs are in range
        Pass=int(input('Enter the credit at pass:'))
        while Pass in range (0,121,20):
            defer=int(input('Enter the credit at defer:'))
            if defer in range (0,121,20):
                fail=int(input('Enter the credit at fail:'))
                total=Pass+defer+fail
            elif defer not in range (0,121,20):
                print('Out of range')
            if fail not in range (0,121,20):
                print('Out of range')
            break
        
        #If inputs are out of range this message would print
        else:print("Out of range")
        
        #The program would only if the total of inputs are less than or equal to 120
        if total<=120:
            #Recheck on whether the inputs are in range
            while Pass in range (0,121,20) and defer in range (0,121,20) and fail in range (0,121,20):
                print()
                #Outputting the correct Progression outcome for the inputs
                if Pass==120:
                    print('Progress')
                    # adding star to print in horizontal histogram
                    prog_star+="*"
                    pro_count+=1
                    #Writing a List for the inputs 
                    pro_list=['Progress -',Pass,defer,fail]
                    #inserting the above list into another main list which will hold them together  
                    List.append(pro_list)
                    
                #The above written steps are continued for all the below Progression outcomes  
                elif Pass==100:
                    print('Progress(module trailer)')
                    pro_mod_star +="*"
                    promod_count+=1
                    promod_list=['Progress (module trailer) -',Pass,defer,fail]
                    List.append(promod_list)
                    
                #Reference
                #Refered 'Mayur Aravindh, 2019302 , L5 Cs group A' python code to find the solution to print "Do-not progress","Exclude".
                elif fail==0 or fail==20 or fail==40 or fail==60:
                    print("Do not Progress- module retriever")
                    Noprog_star +="*"
                    noprog_count +=1
                    noprog_list=['Do not Progress (module retriever) -',Pass,defer,fail]
                    List.append(noprog_list)

                    
                elif fail==80 or fail==100 or fail==120:
                    print("Exclude")
                    exc_star +="*"
                    exc_count +=1
                    exc_list=['Exclude -',Pass,defer,fail]
                    List.append(exc_list)
                   
                #the number of times the user input is kept record    
                tot_count +=1
                #break is used to leave the loop and continue with the next line
                break
        else:print("Total incorrect")
        
        print()
        #User input is taken    
        entry=input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q'to quit and view results:")
        
        while entry=='y' or entry=='q':
            if entry == "q":
                #the variable is changed to False so that the program would stop
                boolean = False
                #after the program stops the below would be printed
                #Horizontal Histogram
                print()
                print("Horizontal Histogram")
                print("Progress",  pro_count ,':',prog_star)
                print("Trailer",   promod_count ,':',pro_mod_star)
                print("Retriever", noprog_count ,':',Noprog_star)
                print("Excluded",  exc_count, ':',exc_star)
                print(tot_count, 'outcomes in total.')
            break
        #if the entered value is not "y" or "q" this message would print
        else:
            print ("Invalid entry")
            
# Part 2 Vertical histogram (extension)
        #Reference
        #Refered 'Mayur Aravindh, 2019302 , L5 Cs group A' python code to find the solution to print "Vertical Histogram". 
        while boolean==False:
            print()
            print("Vertical Histogram")
            print(f'{"Progress",pro_count} {"Trailing",promod_count} {"Retriever",noprog_count} {"Excluded",exc_count}')
            for count in range (0,tot_count):
                #if the count is more than 0 then a star would be printed 
                if pro_count>0:
                    print('*                   ',end='')
                    #Everytime after a star is printed the count would reduce
                    pro_count-=1
                else:
                    print('                    ',end='')
                if promod_count>0:
                    print('*                   ',end='')
                    promod_count-=1
                else:
                    print('                    ',end='')
                if noprog_count>0:
                    print('*                   ',end='')
                    noprog_count-=1
                else:
                    print('                    ',end='')
                if exc_count>0:
                    print('*                   ',end='\n')
                    exc_count-=1
                else:
                    print('                    ',end='\n')
            print(tot_count,'outcomes in total')
            break

#Part 3 and 4 List/Tuple/directory [extension]
        print()
        while boolean == False:
            #printing each index's value seperatly from the main List
            for i in List:
                print(i[0],i[1],i[2],i[3])
            break
        #Reference
        #Refered website:"https://www.google.com/url?sa=t&source=web&rct=j&url=https://www.adamsmith.haus/python/answers/how-to-write-a-list-to-a-file-in-python&ved=2ahUKEwiN_7H7wZH3AhXhyzgGHZ2iDf0QFnoECAQQBQ&usg=AOvVaw3OcDsOX05F-ksVH-tjQMJp"
        #Used the above link to find the solution to print each text in new line.
        def Textfile(filename):
            with open(filename,'w') as file:
                for i in List:
                    text=(i[0],i[1],i[2],i[3])
                    file.write(str(text)+'\n')
                   
        Textfile('CW text file.txt')

            
    #This is used so that error message would be printed if the entry is not the type integer                          
    except ValueError:
         print("Integer required")

