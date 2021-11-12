log_file = open("um-server-01.txt")


def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip() 
        day = line[0:3] 
        if day == "Mon":
            print(line) 


sales_reports(log_file)

#open the file and assigns it to a varaible called log_file
# created a function that has a parm of the log_file variable
#loops thru every item in that variable
#this is removing any trailing charecters from the logfile
# pulls the informations from the zero index to the third index
# a if statments that wants to confirm if day is equal to tue
#if tusday is true then it will print the current line