# Week 6

# Welcome back!

This week, we are going to get a handle on file handles! To get started we are going to learn how to read and write files by writing a program called Howler. A howler is a letter from the Harry Potter Series that screams a message at the person receiving it. We are going to mimic this by changing the words in the letter from lowercase to all uppercase to make it look like we are screaming the message.

There are a few very important points to watch out for in this this lesson when reading in files:

* First, we need to make sure that the file we are opening exists. We can do this using the os module in Python to check if something is a file. This same module can be used to get the directory name or basename of the file
* Next, it is important to realize that once you open a file into a file handle and read it, the file handle is exhausted (or used up). If you need to access the content of that file agin, you would need to open it into a new file handle
* Another gotcha are new line characters in the file. When Python reads a file in, all of the new lines come along. If you want to remove these, you will need to use 'rstrip'

There are also a few points to be very careful of when writing to files!

* First, the default for opening a file is 'r' for reading so you will need to tell Python that you want to write to a file instead with the string 'w'
* Next, when you open a file in Python for writing, it will automatically overwrite any file that exists in that directory with the same name. If you want to append to that file instead you will need to open the file with the 'a' string.
* Newlines can also be tricky when writing a file! In particular, if you use the "write" method it won't automatically attach a newline, whereas the print method does!

As you get into writing programs with input and output files, it is also important to learn how to use argparse (the Python module that we use for interpreting input from the user) to check if these files exist and open them as file handles. We can do this in main, but it is much cleaner to handle all of the user input in the get_args function in your script. 

Last, but not least, we will teach you about how to write a low memory version of your programs. Opening up a file will put all of the file contents into your computer's memory. And, if you work in the field of genomics, like I do, these files can be huge! We will show you how to go line by line through the file, rather then opening the file all at once. This is something I use everyday to make sure my code is robust, and I don't get a Howler from my users when I overwhelm the memory on their laptops!

You will put everything you've learned to the test in the graded homework assignment and practice quiz. In this week's homework you will write a program to "cat" or concatenate files, where the content of the files will be placed into a single output file. You will also need to include a flag that tells the program that you want to include line numbers before each line from the concatented files.

 When you are ready, and all of the tests pass, submit your homework to repl.it. Remember that your code should be called cat.py in the 04_cat directory. Be sure to reach out over slack if you need any help at all, or attend office hours. I'll catch up with you there.