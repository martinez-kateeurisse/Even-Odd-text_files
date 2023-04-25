#Kate Eurisse L. Martinez_BSCPE 1-5_Even-Odd text files

#A Python program that reads a text file named numbers.txt that contains 20 integers. 
#The program will create two other text files;the first text file will be named even.txt, 
#which will contain all even numbers extracted from numbers.txt. 
#The second text file will be named odd.txt and will contain all odd numbers extracted from numbers.txt.

#Import certain modules for the program's design and text formatting
from colorama import Back, Fore, Style 
import prog_design

#Print header art for the program
prog_design.even_odd_header()

#Ask the user's name and printing a greeting
print("//" * 20)
name = input(f"{Fore.RED} Enter your name: "+ Fore.RESET)
print("//"*20, "\n\n") 
print(Back.LIGHTBLACK_EX, Fore.LIGHTCYAN_EX, ("Hello " + name).center(84, "*") + Back.RESET, "\n")

#Display the program's instructions
print(f"{Fore.GREEN} This program will write the integers you'll enter into a text file named number.txt.","\n",
      "Then, all even integers will be written in even.txt,","\n"+" while odd integers will be written in odd.txt", "\n",
      "The output will also be displayed in a tkinter window" +Fore.RESET)
print("="*85)

#Create a text file named numbers.txt 
#Ask the user to input 20 integers 

#Open the main text file
with open("numbers.txt", "w") as num_file:    
    #Initialize count
    number_count = 1
    #Loop condition
    while number_count <= 20:
        #Ask the user for input
        num_input = input(f"{Fore.RED}Please enter an integer: " + Fore.RESET)        
        #Write the input to the text file
        num_file.write(num_input+"\n")
        #Add one to the count
        number_count += 1

#Open and read the text files
with open("numbers.txt", "r") as num_file,open("even.txt", "w") as even_file, open("odd.txt","w") as odd_file:
    #Initialize lists
    #For each line
    for line in num_file:
        #Convert line to int
        integers = int(line)
        #If the integer is even
        if (integers % 2) == 0:
            #Write in new text file (even.txt)
            even_file.write(line)
            #Append into a list
            #Join as string
        #If the integer is odd
        else:    
            #Write in new text file (odd.txt)
            odd_file.write(line)
            #Append into a list
            #Join as string

#Outputs will be printed in new text files

#For output design
#Import modules

#Define the function for buttons
#Create a new window
#Add background image
#Add two buttons to the window (even, odd)
#Add a label to display output text
#main loop
#Output will also be displayed in the tkinter window.(Aside from the txt files)

