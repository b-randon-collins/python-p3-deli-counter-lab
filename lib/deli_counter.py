katz_deli = []

def line(line):
    if len(line) == 0:
        print("The line is currently empty.")
        return "The line is currently empty."
    else:
        output = "The line is currently:"
        for i, person in enumerate(line):
            output += f" {i+1}. {person}"
        print(output)



def take_a_number(line, name):
    line.append(name)
    if len(line) == 1:
        print(f"Welcome, {name}. You are number 1 in line.")
    else:
        print(f"Welcome, {name}. You are number {len(line)} in line.")



def now_serving(line):
    if len(line) == 0:
        print("There is nobody waiting to be served!")
    else:
        person_to_serve = line.pop(0)
        print(f"Currently serving {person_to_serve}.")

# take_a_number(katz_deli, "Ada") #=> Welcome, Ada. You are number 1 in line.
# take_a_number(katz_deli, "Grace") #=> Welcome, Grace. You are number 2 in line.
# take_a_number(katz_deli, "Kent") #=> Welcome, Kent. You are number 3 in line.

# line(katz_deli) #=> "The line is currently: 1. Ada 2. Grace 3. Kent"

# now_serving(katz_deli) #=> "Currently serving Ada."

# line(katz_deli) #=> "The line is currently: 1. Grace 2. Kent"

# take_a_number(katz_deli, "Matz") #=> Welcome, Matz. You are number 3 in line.

# line(katz_deli) #=> "The line is currently: 1. Grace 2. Kent 3. Matz"

# now_serving(katz_deli) #=> "Currently serving Grace."

# line(katz_deli) #=> "The line is currently: 1. Kent 2. Matz"