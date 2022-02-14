#!/bin/bash

# copy command output to file and print the output to the console
command |& tee copy_of_output.txt

# Make file executable
chmod u+rwx file.whatever
# u = current user only gets to execute the file
# + = adds changes to that file
# r = read
# w = write
# x = execute

>   # write to file, create if does not exist, replace if exists
>>  # append to the file


ls -hal
# h = human readable, display filesizes in kilobytes (K), megabytes (M), or gigabytes (G)
# a = all, show hidden files
# l = diplay items in list format

# splitting large file into smaller ones (by size)
split -d -b 2G myfile prefix_name
