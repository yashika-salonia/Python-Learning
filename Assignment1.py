#Import the necessary library
import numpy as np

#Manually add the Summer Olympics, London 2012 dataset as arrays
countries = np.array([
    "United States", "China", "Great Britain", "Russia", "South Korea",
    "Germany", "France", "Italy", "Hungary", "Australia"
])

gold = np.array([46, 38, 29, 24, 13, 11, 11, 8, 8, 7])
silver =  np.array([28, 27, 17, 26, 8, 19, 11, 9, 4, 16])
bronze =  np.array([29, 23, 19, 32, 7, 14, 12, 11, 5, 12])

#Use the argmax() method to find the highest number of gold medals
# gold_medal_winner = 
print(f"Highest no of gold won are: {gold[np.argmax(gold)]} by {countries[np.argmax(gold)]}")

#Print the name of the country with more than 20 gold medals

#Use Boolean indexing technique to find the required output
print("Countries with more than 20 gold medals:")
print(countries[(gold) > 20])

# Evaluate the dataset and print the name of each country with its gold medals and total number of medals
#Use a for loop to create the required output
for i in range(len(countries)):
    total_medal= gold[i] + silver[i] + bronze[i]
    print(f"{countries[i]} won: {gold[i]} gold medals & total medals: {total_medal}")

# Output of the code
# Highest no of gold won are: 46 by United States
# Countries with more than 20 gold medals:
# ['United States' 'China' 'Great Britain' 'Russia']
# United States won: 46 gold medals & total medals: 103
# China won: 38 gold medals & total medals: 88
# Great Britain won: 29 gold medals & total medals: 65
# Russia won: 24 gold medals & total medals: 82
# South Korea won: 13 gold medals & total medals: 28
# Germany won: 11 gold medals & total medals: 44
# France won: 11 gold medals & total medals: 34
# Italy won: 8 gold medals & total medals: 28
# Hungary won: 8 gold medals & total medals: 17
# Australia won: 7 gold medals & total medals: 35