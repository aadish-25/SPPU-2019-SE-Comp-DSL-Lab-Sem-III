'''
Problem Statement: In second year computer engineering class, group A student's play cricket, group B students play badminton and group C students play football.
Write a Python program using functions to compute following:
a) List of students who play both cricket and badminton
b) List of students who play either cricket or badminton but not both
c) Number of students who play neither cricket nor badminton
d) Number of students who play cricket and football but not badminton.
(Note- While realising the group, duplicate entries should be avoided, Do not use SET built-in functions)

'''

cricket = []
badminton = []
football = []
all_players = []

def remove_duplicates(sport_list):
	unique_list = []
	for player in sport_list:
		if player not in unique_list and not player =="":
			unique_list.append(player)
	return unique_list

def take_input(sport_list, sport_name):
	print(f"Enter the number of students playing {sport_name}")
	n = int(input())
	print(f"Enter the names of students playing {sport_name}")
	for i in range (n):
		sport_list.append(input())

	# Check for duplicates
	sport_list = remove_duplicates(sport_list)

    # Make a list to store all the players
	for player in sport_list : 
		if player not in all_players:
			all_players.append(player)
	return sport_list	

def both_cricket_and_badminton(cric, bad):
	result = []
	for player in cric:
		if player in bad and player not in result:
			result.append(player)
	
	print(f"The students playing both cricket and badminton are : {result}")

def either_cricket_and_badminton_but_not_both(cric, bad):
	result = []
	for player in cric:
		if player not in bad:
			result.append(player)
	for player in bad:
		if player not in cric:
			result.append(player)
			
	
	print(f"The students playing cricket and badminton but not both are : {result}")

def neither_cricket_nor_badminton(cric, bad):
	result = []
	for player in all_players:
		if player not in cric and player not in bad:
			result.append(player)

	print(f"The students playing neither cricket nor badminton are : {result}")

def cricket_and_football_but_not_badminton(cric, foot, bad):
	result = []
	for player in cric:
		if player not in bad:
			result.append(player)

	for player in foot:
		if player not in bad:
			result.append(player)

	print(f"The students playing cricket and football but not badminton are : {result}")


def main():
	print("\n\nEnter data for students : ")
	print("--------------------------\n")

	unique_cricket = take_input(cricket, "cricket")
	unique_badminton = take_input(badminton, "badminton")
	unique_football = take_input(football, "football")

	print("----------------- UNQIUE LIST OF STUDENTS -----------------\n")
	print(f"All students : {all_players}")
	print(f"The students playing cricket are : {unique_cricket}")
	print(f"The students playing badminton are : {unique_badminton}")
	print(f"The students playing football are : {unique_football}\n")
	
	chr = "Y"
	while(chr=="y" or chr=="Y"):
		print("----------------------- MENU -----------------------")
		print("1. Students who play both cricket and badminton")
		print("2. Students who play either cricket and badminton but not both")
		print("3. Students who play neither cricket nor badminton")
		print("4. Students who play cricket and football but not badminton")
		print("5. Exit")

		print("Enter your choice between (1-5) :")
		option = int(input())

		if(option == 1): 
			both_cricket_and_badminton(unique_cricket, unique_badminton)
			
		if(option == 2): 
			either_cricket_and_badminton_but_not_both(unique_cricket, unique_badminton)
			
		if(option == 3): 
			neither_cricket_nor_badminton(unique_cricket, unique_badminton)
			
		if(option == 4): 
			cricket_and_football_but_not_badminton(unique_cricket, unique_football, unique_badminton)
			
		if(option == 5): 
			print("Exiting the program")
			
		print("Do you want to continue (y/n)")
		x = input()[0]
		if(x=='N' or x=='n'):
			chr = 'N'
			print("Exiting the program")

main()