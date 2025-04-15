name = input("What is your name? ")
print(f"Hello, {name}!")

# ask the user for their favorite fruit
fruit = input("What is your favorite fruit? ")  
print(f"Your favorite fruit is {fruit}.")

# if fruit is from list then print "fruit is in the list" 
if fruit in ["watermelon", "banana", "orange", "grape", "kiwi"]:
    print(f"{fruit} is also my favorite.") 
else:
    print(f"{fruit} is not my favorite.")       

# ask for favorite indian male singer
Msinger = input("What is your favorite male singer? ")  
print(f"Your favorite male singer is {Msinger}.")

# if singer is from list then print "singer is in the list" 
if Msinger in ["Arijit Singh", "Sonu Nigam", "Kumar Sanu", "Mohammed Rafi", "Kishore Kumar"]:
    print(f"{Msinger} is also my favorite.") 
else:
    print(f"{Msinger} is not my favorite.")  

# ask for favorite female singer
Fsinger = input("What is your favorite female singer? ")  
print(f"Your favorite female singer is {Fsinger}.")

# if singer is from list then print "singer is in the list" 
if Fsinger in ["Shreya Ghoshal", "Lata Mangeshkar", "Asha Bhosle", "Alka Yagnik", "Sunidhi Chauhan"]:
    print(f"{Fsinger} is also my favorite.")
else:
    print(f"{Fsinger} is not my favorite.") 

# ask for favorite place to visit in india
place = input("What is your favorite place to visit in India? ")
print(f"Your favorite place to visit in India is {place}.")

# if place is from list then print "place is in the list"
if place in ["Goa", "Kerala", "Jaipur", "Agra", "Varanasi", "Shimla", "Manali"]:
    print(f"{place} is also my favorite.")
else:
    print(f"{place} is not my favorite.")

# ask for why they like the place
reason = input(f"Why do you like {place}? ")
print(f"I agree on your answer that you like {place} because '{reason}'.")

# ask to thanks for the user for their time
print("Thank you for your time!")
# ask to say goodbye to the user
print("Goodbye!")












