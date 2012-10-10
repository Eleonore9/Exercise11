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
    my_tup = (restaurant, score)
    my_list.append(my_tup)

#Sort the list of restaurant names
sort_list = sorted(my_list)

#Loop through the list of restaurant names and get the corresponding score
for elements in sort_list:

    restaurant = elements[0]
    score = int(elements[1])

    print "Restaurant %s is rated at %d." % (restaurant, score)

#Close file
my_file.close()