#Kate Eurisse L. Martinez_BSCPE 1-5_Even-Odd text files

#A Python program that reads a text file named numbers.txt that contains 20 integers. 
#The program will create two other text files;the first text file will be named even.txt, 
#which will contain all even numbers extracted from numbers.txt. 
#The second text file will be named odd.txt and will contain all odd numbers extracted from numbers.txt.

#Create a text file named numbers.txt 
#Ask the user to input 20 integers 

#Open the main text file
with open("numbers.txt", "w") as num_file:    
    #Initialize count
    number_count = 1
    #Loop condition
    while number_count <= 20:
        #Ask the user for input
        num_input = input("Please enter an integer: ")        
        #Write the input to the text file
        num_file.write(num_input+"\n")
        #Add one to the count

#Open and read the text files
with open("numbers.txt") as num_file,open("even.txt", "w") as even_file, open("odd.txt","w") as odd_file:
    #For each line
    for line in num_file:
        #Convert line to int
        integers = int(line)
        #If the integer is even
        if (integers % 2) == 0:
            #Write in new text file (even.txt)
            even_file.write(line)
        #If the integer is odd
        else:    
            #Write in new text file (odd.txt)
            odd_file.write(line)
#Outputs will be printed in new text files