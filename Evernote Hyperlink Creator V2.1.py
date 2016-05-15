from Tkinter import *

'''
Changelog:
V2.1 - fixed error preventing links with action#n= instead of menu#n= from processing
'''

class GUI:
    def __init__(self, main):
        #create widgets
        self.inputTextBox = Entry(main)
        self.nameTextBox = Entry(main)
        self.resultTextBox = Entry(main)
        self.convertButton = Button(main, text = "Convert")

        #place widgets in main window
        self.inputTextBox.grid(row = 0, column = 0)
        self.nameTextBox.grid(row = 0, column = 1)
        self.convertButton.grid(row = 1, columnspan = 2, sticky = "ew")
        self.resultTextBox.grid(row = 2, columnspan = 2, sticky = "ew")

        #bind events
        self.convertButton.bind("<Button-1>", self.buttonConvertClick)

    #button receives input from hyperlink and name then creates resulting string
    def buttonConvertClick(self, event):
        #receive inputs
        original = self.inputTextBox.get()
        name = self.nameTextBox.get()

        #find note numner
        location = original.find("menu#n=")
        if location == -1: #if menu#n= is not found
            location = original.find("tion#n=") #some hyperlinks have action#n= instead of menu#n=
        if location == -1:  #case that unexpected hyperlink is passed
            self.resultTextBox.delete(0, END)
            self.resultTextBox.insert(0, "Invalid hyperlink")
        else:  #case that we continue with program
            #cut off &ses and everything after
            endLocation = original.find("&ses")
            if endLocation == -1:
                self.resultTextBox.delete(0, END)
                self.resultTextBox.insert(0, "Invalid hyperlink")
            else:
                #store note number
                location = location + 7
                noteNumber = original[location:endLocation]
            
                #convert spaces in name to %20s
                changed = True
                while (changed):
                    changed = False
                    i = name.find(" ")
                    if i != -1:
                        name = name[:i] + "%20" + name[i + 1:]
                        changed = True

                        #put everything back together
                        result = "https://www.evernote.com/shard/s92/nl/10307768/"
                        result = result + noteNumber
                        result = result + "&title="
                        result = result + name

                        #display result and clean up
                        self.resultTextBox.delete(0, END)
                        self.resultTextBox.insert(0, result)

                        self.inputTextBox.delete(0, END)
                        self.nameTextBox.delete(0, END)
        
        
'''        location = original.find("p&n=")     #finds the location of "p&n=" or -1 if not found

    if location == -1:    #this is the case where "p&n=" was not found
        location = original.find("p&x")    #find where p&x is
        if location == -1:   #if you can't find that either, something is seriously wrong
            print("Error: Unexpected link passed to program.  Exiting")    #display error message
            break            #and exit program
        location = original.find("n=", location)     #find where n= is, note number to follow soon
        location = location + 2     #set location to where note number starts
    else:                 #this else is where the original location was accurate
        location = location + 4     #once again, set location to where note number starts

    #step 3: get note number
    noteNumber = original[location:]

#step 4: get the text the user wants to see
    name = raw_input("Enter the text you want the note to say:") #get the text the user wants to see

    if name == "x":      #check to see if the user wants to exit program
        break            #and then exit the program

    #step 5: replace spaces in name with %20
    changed = True   #this will change to true if we change anything
    while changed:   #loop stops when nothing is changed
        i = name.find(" ")    #find a space
        if i == -1:
            changed = False
        else:
            name = name[:i] + "%20" + name[i + 1:]   #this is totally going to work
    
    #step 6: put everything together
    result = "https://www.evernote.com/shard/s92/nl/10307768/"   #this is the starting string
    result += noteNumber   #append the notenumber
    result += "&title="    #some admin characters
    result  += name         #append the name
'''

        
mainWindow = Tk()
mainWindow.title("Evernote Hyperlink Editor")
interface = GUI(mainWindow)
mainWindow.mainloop()
