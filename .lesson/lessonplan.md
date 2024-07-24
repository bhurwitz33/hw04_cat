# Lesson plan
  
This week, we get a chance to start working with data in files, and writing to STDOUT. Most of the time, and especially now in our data-intensive world, input data stored in files or databases file rather than brought in from user-input on the command-line. As part of the exercises this week, you will learn how to read input from files and write to an output file. You will be using the argparse module just like you have before, but instead of positional or optional arguments, you will learn how to define a file as input. Remember, you can use the new.py script to start the homework assignment, and can quickly update the arguments there to read and write to a file.

## Exercise (howler.py)

In this lesson, we are going to write a program that create a "Howler". In the Harry Potter stories, a "Howler" is a nasty-gram that yells a message at you when you open it. We are going to "yell" a message at our user, by converting their lowercase message to uppercase, and writing it to a file.

In this week's lesson we will walk you through how to:

* Accept input from the command-line or a file
* Change strings to uppercase
* Write output to a file, or to STDOUT
* Learn how to use a file handle, or change an input string into a file handle

## Homework (cat.py)

Can you use these new skills in the homework? This week, you will write the Python version of the Unix `cat` command that will _conCATenate_ files. The program will need to take one or more filenames as input as positional arguments, and include an optional `-n` or `--number` argument for whether or not to print line numbers. 

Reach out if you need any help! We use the same tests you are given to test the code and assign a grade for your assignment.

## Learning Objectives:

Learn how to read and write to a file or STDOUT (via the os Python module). Learn how to use filehandles to write to output files. Learn how to write a low-memory Python programs that doesn't read the entire file into memory all at once.