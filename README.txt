This is a command-line-interface "todo" program.
The functionalities of the program include:
help   #to list out commands available
add    #to addd a new task
done   #to report a completed task
del    #to delete a task
report # to generate report of completed vs pending tasks
ls     #to list out remaining tasks


#FOR WINDOWS :
(Copy the batch file (todo.bat) along with the python file in c drive to access the program through command prompt)

#FOR LINUX :
(copy the given file (todo) with no extension (or .sh) in a paricular directory along with .py file)
On terminal at the saved path type:

./todo -help ...

to access commands

#Important

You need to add '-' before giving every command 
for eg:
todo -add "assignment 1"
todo add "assignment 1"  will give 'unrecognized argument error'

exaple commands:

todo -add "assignment 1"   #assignment 1 will be added in file todo.txt
todo -ls                   #all the pending assignments are listed
todo -del 3                #task 3 in list is deleted
todo -done 2               #task 2 is marked done and shifted to done.txt 
todo -report               #will give a report for completed and pending tasks

(For linux its ./todo and not todo)
