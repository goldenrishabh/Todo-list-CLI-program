(Copy the batch file in c drive to acces the program through command prompt)

This is a command-line-interface "todo" program.
The functionalities of the program include:
help   #to list out commands available
add    #to addd a new task
done   #to report a completed task
del    #to delete a task
report # to generate report of completed vs pending tasks
ls     #to list out remaining tasks


You need to add '-' before giving every command 
for eg:
todo -add "assignment 1"
todo add "assignment 1"  will give 'unrecognized argument error'

exaple commands:

todo -add "assignment 1"
todo -ls
...
