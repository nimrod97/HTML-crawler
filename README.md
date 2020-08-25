# HTML-crawler
crawling on html files in a recursive way and in each file- saving the information about references to other html files (parser).


The program gets an html file name as an input from the user and adds it to a dictionary as a key. Then saves all of his reference to the other html files that the input file contains in a recursive way (calls 'parser' function). This will be executed in each file that appears in the recursion.                  
All the information will be stored in the dictionary: the keys are the file names and the value of each key is the list with the file names that the key as a reference to. A file will be added as a value to a key only if the file hasn't shown up yet as a reffered file of the key.
After crawling all the html files, the program will save the information in a csv file called results. in this file, each row will start with the name of the file , and to his right, the reffered files that the specific file has hyperlinks to.
After that, the program gets another html file as an input from the user , and prints the sorted list with the files that the input file as a reference to.
