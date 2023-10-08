#!/bin/bash

# Get the name of the file
file_name=$1

# Get the column number
column_number=$2

# Get the number to add
number=$3

# Get the name of the new file
new_file_name=$4

# Open the file in read mode
file=open "$file_name" r

# Open the new file in write mode
new_file=open "$new_file_name" w

# Loop through each line in the file
while read -r line; do

    # Split the line into an array of words
    words=($line)

    # Add the number to each number in the column
    for i in $(seq ${column_number} ${#words}); do
        words[$i]=$((words[$i] + number))
    done

    # Join the words back into a line
    line=$(join "${words[@]}")

    # Print the line to the new file
    echo "$line" >> "$new_file"

done < "$file"

# Close the files
close "$file"
close "$new_file"
