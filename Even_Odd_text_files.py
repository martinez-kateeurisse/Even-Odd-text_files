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
    even_int = []
    odd_int = []
    #For each line
    for line in num_file:
        #Convert line to int
        integers = int(line)
        #If the integer is even
        if (integers % 2) == 0:
            #Write in new text file (even.txt)
            even_file.write(line)
            #Append into a list
            even_int.append(line.strip())            
            #Join as string
            even_string = "\n".join(even_int)
        #If the integer is odd
        else:    
            #Write in new text file (odd.txt)
            odd_file.write(line)
            #Append into a list
            odd_int.append(line.strip())
            #Join as string
            odd_string = "\n".join(odd_int)

#Outputs will be printed in new text files

#For output design
#Import modules
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

#Define the function for buttons
#Define the function for button clicks
def button_click(button_number):
    #If button 1
    if button_number == 1:
        output_text.set("Even Integers are: \n" + even_string)
    #If button 2
    elif button_number == 2:
        output_text.set("Odd Integers are: \n" + odd_string)

#Create a new window
root = tk.Tk()
root.geometry("200x300")  # Size of the window 
root.title("File Handling - Even, Odd")  # Adding a title

#Add background image
canvas = tk.Canvas(root, width=200, height=300)
image = ImageTk.PhotoImage(Image.open("C:\\Users\\Kate\\Desktop\\OOP\\progtest\\background_image.jpg"))
canvas.create_image(0,0, anchor=NW, image=image)
canvas.pack()

#Add two buttons to the window (even, odd)
button1 = tk.Button(root, text="Even", command=lambda: button_click(1), fg="red")
button1.place(x=80, y=30)
button2 = tk.Button(root, text="Odd", command=lambda: button_click(2), fg="blue")
button2.place(x=80, y=60)

#Add a label to display output text
output_text = tk.StringVar()
output_label = tk.Label(root, textvariable=output_text)
output_label.place(x=50, y=100)

#main loop
#Output will also be displayed in the tkinter window.(Aside from the txt files)

