# Assignment #2

# function ===============================
def draw_stars2(my_list):
    # traversing through my_list
    for item in my_list:
        # output is a container
        output = ''

        # check to see if value is either int or string
        if type(item) is int:
            for i in range(item):
                output += '*'

        elif type(item) is str:
            # parses the first letter of word and place into 'first_letter'
            first_letter = item[0].lower()
            # figure out the length count of word
            for i in range(len(item)):
                # then store first_letter into output
                output += first_letter

        print output
# ========================================

# List of numbers and string
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

# Pass in list 'x' into funtion 'draw_stars'
draw_stars2(x)




