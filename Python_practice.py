# #print("Hello World!")

# #counties = ["Arapahoe","Denver","Jefferson"]
# #if counties[1] == 'Denver':
# #    print(counties[1])

# #if counties[2] != "Jefferson":
# #   print(counties[2])

# #temperature = int(input("What is the temperature outside? "))

# #if temperature > 80:
# #    print("Turn on the AC.")
# #else:
# #   print("Open the windows.")

# #What is the score?
# #score = int(input("What is your test score? "))

# # Determine the grade.
# #if score >= 90:
# #    print('Your grade is an A.')
# #else:
# #    if score >= 80:
# #       print('Your grade is a B.')
# #   else:
# #       if score >= 70:
# #           print('Your grade is a C.')
# #       else:
# #           if score >= 60:
# #               print('Your grade is a D.')
# #           else:
# #               print('Your grade is an F.')

# # What is the score?
# #score = int(input("What is your test score? "))

# # Determine the grade.
# #if score >= 90:
# #    print('Your grade is an A.')
# #elif score >= 80:
# #    print('Your grade is a B.')
# #elif score >= 70:
# #    print('Your grade is a C.')
# #elif score >= 60:
# #    print('Your grade is a D.')
# #else:
# #    print('Your grade is an F.')  

# #counties = ["Arapahoe","Denver","Jefferson"] 
# #if "Arapahoe" in counties: 
# #    print("True") 
# #else: 
# #    print("False") 

# #counties = ["Arapahoe","Denver","Jefferson"] 
# #if "El Paso" not in counties: 
# #    print("True") 
# #else: 
# #    print("False")  

# #counties = ["Arapahoe","Denver","Jefferson"]
# #if "El Paso" in counties:
# #    print("El Paso is in the list of counties.")
# #else:
# #    print("El Paso is not in the list of counties.")  

# # x = 5
# # y = 6
# # if x == 5 and y == 5:
# #     print("True") 
# # else:
# #     print("False")   

# # x = 5
# # y = 5
# # if x == 3 or y == 5:
# #     print("True")
# # else:
# #     print("False")     

# # x = 5
# # y = 5
# # if not(x > y):
# #     print("True") 
# # else:
# #     print("False")

# #This prints "True" because x is not greater than y. 
# #If x = 6, then it would print "False" because x IS greater than y.

# # counties = ["Arapahoe","Denver","Jefferson"] 
# # if "Arapahoe" in counties and "El Paso" in counties:
# #     print("Arapahoe and El Paso are in the list of counties.")
# # else:
# #     print("Arapahoe or El Paso is not in the list of counties.")

# # if "Arapahoe" in counties or "El Paso" in counties:
# #     print("Arapahoe or El Paso is in the list of counties.")
# # else:
# #     print("Arapahoe and El Paso are not in the list of counties.")

# # if "Arapahoe" in counties and "El Paso" not in counties:
# #    print("Only Arapahoe is in the list of counties.")
# # else:
# #     print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

# # x = 0
# # while x <= 5:
# #     print(x)
# #     x = x + 2

# # counties = ["Arapahoe","Denver","Jefferson"] 
# # for county in counties:
# #     print(county)

# # numbers = [0, 1, 2, 3, 4]
# # for num in numbers:
# #     print(num)

# # for i in range(5):
# #     print(i)

# # alphabet = ["a", "b", "c", "d", "e", "f", "g"]
# # for alpha in range(len(alphabet)):
# #       print(alphabet[alpha])

# # counties = ["Arapahoe","Denver","Jefferson"] 
# # for i in range(len(counties)):
# #     print(counties[i])

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}   
# for county in counties_dict:
#     print(county)

# for voters in counties_dict.values():
#     print(voters)

# # for county in counties_dict:
# #     print(counties_dict[county])

# for county, voters in counties_dict.items():
#     print(county, voters)

# # for county, voters in counties_dict.items():
# #     print(county + " has " + str(voters) + " registered voters.")

# voting_data = [{"county":"Arapahoe", "registered_voters": 422829, "alpha":1},
#                 {"county":"Denver", "registered_voters": 463353, "alpha":2},
#                 {"county":"Jefferson", "registered_voters": 432438, "alpha":3}]

# for county_dict in voting_data:
#     print(county_dict)


# for i in range(len(voting_data)):
#       print(voting_data[i]['alpha'])


# for i in range(len(voting_data)):
#       print(voting_data[i]['alpha'])

# for i in voting_data:
#     for j in i.values():
#         print(j)

# # for county_dict in voting_data:
# #     for value in county_dict.values():
# #         print(value)


# # for county_dict in voting_data:
# #      print(county_dict['registered_voters'])


# for i in voting_data:
#      print(i['registered_voters'])

# # for county_dict in voting_data:
# #     print(county_dict['county'])

# # my_votes = int(input("How many votes did you get in the election? "))
# # total_votes = int(input("What is the total votes in the election? "))
# # print(f"I received {my_votes / total_votes * 100}% of the total votes.")
# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]


# counties_dict = {"Arapahoe": 369237, "Denver": 413229, "Jefferson": 390222}
# # # for county, voters in counties_dict.items():
# # #     print(county + " county has " + str(voters) + " registered voters.")

# # for county, voters in counties_dict.items():
# #     print(f"{county} county has {voters} registered voters.")

# # for i, j in counties_dict.items():
# #     print(f"{i} county has {j} registered voters.")

# print(counties_dict.get("Arapahoe"))

# # counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}   
# # for j in counties_dict:
# #     print(j)



# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes:,} number of votes. "
#     f"The total number of votes in the election was {total_votes:,}. "
#     f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

# print(message_to_candidate)

# counties_dict = {"Arapahoe": 369237, "Denver": 413229, "Jefferson": 390222}
# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters:,} registered voters.")

# voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, 
# {"county":"Denver", "registered_voters": 463353}, 
# {"county":"Jefferson", "registered_voters": 432438}]

# for i in voting_data:
# #    print( i["county"] +" has " + str(i["registered_voters"]) + " registred voters.")
#     print(f' {i["county"]} has {(i["registered_voters"]):,} registred voters.')

# PYTHON DEPENDENCIES, MODULES AND PACKAGES

# Import the datetime class from the datetime module.
import datetime
# # Use the now() attribute on the datetime class to get the present time.
# now = datetime.datetime.now()
# # Print the present time.
# print("The time right now is ", now)

#print(dir(datetime))
print(dir(tuple))
