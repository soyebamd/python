states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

#accessing item
print(states_of_america[1]) # will print Pennsylvania

#update item
states_of_america[1] = "Soyeb Ahmed"
print(states_of_america[1])

#add item
states_of_america.append("New York")

states_of_america.extend(["sadfsdf", "sadfsadf", "sadfsdfsda"])
print(len(states_of_america))

states_of_america.remove("New York")
print(states_of_america[::-1])
print(len(states_of_america))




#via loop
# for i in states_of_america:
#     print(i)