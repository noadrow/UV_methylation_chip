#!/bin/bash

input_file=$1
output_file=$2

# Use sed to transform each line in the input file
grep -v "#N/A" "$1" | sed 's/^\(.*\)\s\(.*\)/>\1\n\2/' | tail +3> "$2"

echo "Transformation complete. Output saved to $output_file"
