## writeFile.py
# If the file does not exist, opening it for writing will cause it
# to be created in the local folder.  If it does exist, the open
# function will cause the file to be wiped clean.

def write_file():
    print ("Executing readWriteFile.py")

    # Choose the input file name. Open the input file to be read.
    infileName = "input.txt"
    infile = open(infileName, "r")
    
    # Choose the output file name. Open the output file to be written.    
    outfileName = "output.txt"
    outfile = open(outfileName, "w")
    
    # Loop to read lines from the input file and write these to the
    # output file. Note that the "reading" is done by the for loop.
    for line in infile:
        line = line[:-1] #strips the carriage return from the end of the line
        print(line.lstrip(), file = outfile)

    print("The files have been processed.")

    infile.close()
    outfile.close()

def main():
    write_file()
    
main()
