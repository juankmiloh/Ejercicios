from sys import argv

entrada = raw_input("What is your name:")
argv.extend(['first', 'second', 'third', entrada])
script, first, second, third, name = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your name is:", name
