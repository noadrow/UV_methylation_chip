#!/bin/bash

# Define the input files
file1=$1
file2=$2

# Loop through each line in file1
while IFS= read -r line; do
  # Use grep to find matching lines in file2
  grep -F "$line" "$file2"
done < "$file1"