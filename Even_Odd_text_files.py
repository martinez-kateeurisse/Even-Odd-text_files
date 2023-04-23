#Kate Eurisse L. Martinez_BSCPE 1-5_Even-Odd text files

#A Python program that reads a text file named numbers.txt that contains 20 integers. 
#The program will create two other text files;the first text file will be named even.txt, 
#which will contain all even numbers extracted from numbers.txt. 
#The second text file will be named odd.txt and will contain all odd numbers extracted from numbers.txt.

#Create a text file named numbers.txt 
#Input 20 integers to the text file

#Open and read the text files
with open("numbers.txt") as num_file,open("even.txt", "w") as even_file, open("odd.txt","w") as odd_file:
    #For each line
    for line in num_file:
        #Convert line to int
        integers = int(line)
        #If the integer is even
        if (integers % 2) == 0:
            #Write in new text file (even.txt)
        #If the integer is odd
            #Write in new text file (odd.txt)

#Outputs will be printed in new text files