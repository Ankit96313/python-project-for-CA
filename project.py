#Acronym Program
#Taking input from user
Take_input_from_user=str(input("Enter a Sentence: "))
#making list of words
text=Take_input_from_user.split()
#Creating empty string
b=''
#Acessing each word one by one using for loop
for j in text:
#Taking first letter of word and converting to uppercase 
    b=b+str(j[0]).upper()
#Printing Acronym
print(b)