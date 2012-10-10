#Open text file
my_file = open("scores.txt")

#Create initial dictionary
my_dict = {}

#Read the file into the dictionary
for line in my_file:

    split = line.strip().split(":")

    my_dict[split[0]] = split[1]

my_list = []

#Make a list of restaurant names
for restaurant, score in my_dict.items():
    my_list.append(restaurant)

#Sort the list of restaurant names to create a list of keys in alphabetical order
sort_list = sorted(my_list)

#Loop through the list of keys and print in alphabetical order
for key in sort_list:
    score = int(my_dict[key])
    print "Restaurant %s is rated at %d." % (key, score)

#Close file
my_file.close()
