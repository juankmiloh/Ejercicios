from sys import argv
from os.path import exists

fileOne = 'test.txt'
fileTwo = 'new_file.txt'
argv.extend([fileOne, fileTwo])
script, from_file, to_file = argv
in_file = open(from_file, 'w')
text = raw_input("Write your text here:\n\t>>>")
in_file.write(text)

print "Copying from %s to %s" % (from_file, to_file)

#  We could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "alright, all one"

out_file.close()
in_file.close()
