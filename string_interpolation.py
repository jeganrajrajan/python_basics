# Using % (modulo) operator
# Type1:
print("\nHey! I'm %s, %d years old and I love %s Programing" % ('Ram', 25, 'Python'))

# Type2:
format_str = "\nHey! I'm %s and I'm %d years old."
Ram_info = ('ram', 25)

print(format_str % Ram_info)

# 2.Using .format() method

# Dictionary
person_dict = dict(name="Ajay", age=25, country="INDIA", lan="Python")
print("Hey! My name is {name}, I'm {age} years old, currently living in {country} and love {lan} programming"
      .format(**person_dict))  # '**' - used for mapping

# List
person_list = ["AJAY", 25, "INDIA"]
print("\nPerson info from List: {0} from {2}".format(*person_list))

# Tuple
person_tup = ("RAM", "INDA", 25)
print("\nPerson info from Tuple: {0} {2} {1}".format(*person_tup))

# Set
person_set = {"RAM", 23, "Python"}
print("\nPerson info Set: {} {} {}".format(*person_set))
# Sequence of set elements cannot be defined for printing as it is unordered collection.


# 3.Using f-string formatting
# from datetime import datetime

my_name = "Emma"
# today=datetime.now()

# List
info = ["ASHWIN", 30, "INDIA", "Python"]
print(f"{info[0]} is {info[1]} years old currently living in {info[2]} and loves {info[3]} programming.")

# Dictionary
data = dict(name="ASHWIN", age=30, country="INDIA", lan="Python")
print(f"{data['age']} years old  {data['name']} lives in {data['country']} and loves {data['lan']} programming")

from string import Template

name = 'balaji'
program = 'python'
new = Template('Hello $name This is $program.')
print(new.substitute(name=name, program=program))

"""
it will do formating
it has four methods
"""