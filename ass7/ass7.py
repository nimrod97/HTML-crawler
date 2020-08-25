"""
Nimrod Gabbay
"""
def crawler(filename):
    """
    Function Name: crawler                                                              
    Input: filename                                                                     
    Output: -----                                                                     
    Function Operation: The function gets an html file name and adds it                    
                        to the dictionary as a key. Then saves all of his reference     
                        to the other html files that the input file contains            
                        in a recursive way (calls 'parser' function).                   
                        All the information will be stored in the dictionary.
    """
    if filename not in d:
        #adding the file name to the dictionary as a key
        d[filename] = [] 
    with open (filename,'r') as file:
        for line in file.readlines():
            # calling 'parser' to check the line in the file name
            parser(filename, line) 
            

def parser(filename, line):
    """
    Function Name: parser
    Input: filename , line
    Output: -----
    Function Operation: The function gets an html file name and a line from
                        the file and checks if the line has a reference to
                        other html file. if the referred file hasn't shown up yet
                        as a value to to key (the inserted file), the function
                        will add it to the dictionary as a value (to the list of values of each key).
                        After that, the function will call to 'crawler' function
                        in order to check if the reffered file itself has a reference
                        to other files 
    """

    if 'href=' in line:
        #getting the reffered file
        new_file = line.split('href=')[1].split('"')[1] 
        if new_file not in d[filename]:
            # add the file to the list of the values that the key has
            d[filename].append(new_file) 
             # calling 'crawler' to check the new file
            crawler(new_file)

str=input("enter source file:\n")
d=dict()
crawler(str)

# Saving the information in csv file
with open('results.csv', 'w') as f:
    for key in d.keys():
        f.write(key)
        f.write(',')
        for value in d[key]:
            f.write(value)
            f.write(',')
        f.write('\n')
        
str=input("enter file name:\n")
 # print the files that the input file as a reference to (sorted)
print(sorted(d[str]))
