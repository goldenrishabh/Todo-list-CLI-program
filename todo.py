import argparse
from datetime import date

open('todo.txt', 'a')
open('done.txt', 'a')

# function definitions
def add(args):
    list_file = open('todo.txt', "a")
    list_file.write(f"{args.add} \n")
    print(f"Added todo : {args.add}")


def ls():
    list_file = open('todo.txt', "r")
    list_file.seek(0)
    print(list_file.read())


def delno(args):
    list_file = open('todo.txt', 'r')
    tasks = list_file.readlines()
    list_file.close()
    del tasks[args.number - 1]
    list_file = open('todo.txt', 'w+')
    for task in tasks:
        list_file.write(f"{task}")


def done(args):
    done_file = open('done.txt', 'a')
    list_file = open('todo.txt', "r")
    list_file.seek(0)
    lines = list_file.readlines()
    print(f"Done:{lines[args.task - 1]}")
    done_file.write(f"{lines[args.task - 1]}")
    list_file.close()
    done_file.close()
    del lines[args.task - 1]
    list_file = open('todo.txt', 'w+')
    for line in lines:
        list_file.write(f"{line}")


def report():
    list_file = open('todo.txt', 'r')
    done_file = open('done.txt', 'r')
    print(f'{date.today().strftime("%d/%m/%Y")} Pending : {len(list_file.readlines())} Completed: {len(done_file.readlines())}')
    list_file.close()
    done_file.close()


# Parser arguments
parser = argparse.ArgumentParser(description='## welcome to to-do list v1.1 ##', add_help=False,usage="A simple to-do list")
parser.add_argument('-help', action='help', default=argparse.SUPPRESS, help='#Usage')
parser.add_argument('-add', dest="add", help='#Enter the task you want to add', type=str)
parser.add_argument('-ls', action='store_true', help='#Display to-do list')
parser.add_argument('-del', dest='number', help='#The task to be deleted', type=int)
parser.add_argument('-done', dest='task', help='#The task completed', type=int)
parser.add_argument('-report', action='store_true', help='#Return todo list report')
parser.parse_args()
args = parser.parse_args()

if args.ls:
    ls()
if args.add:
    add(args)
if args.number:
    delno(args)
if args.task:
    done(args)
if args.report:
    report()