from sys import argv

# Define an varible with the name of archive
archivo = 'ex15_sample.txt'

# Add the argument to argv
argv.extend([archivo])

# Define variables to use argv
script, filename = argv

# Open the file
txt = open(filename)

# Prints out the filename
print "Here's your file %r:" % filename

# Read the filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt.close()
