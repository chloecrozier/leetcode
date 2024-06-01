#!/bin/bash

# Check for 4 arguments
if [ $# -ne 4 ]; then
  echo "Usage: ./submit_solution.sh <programming-language> <difficulty> <file_name> <message>"
  exit 1
fi

# Extract arguments
language="$1"
difficulty="$2"
filename="$3"
message="$4"

# Get the list of folders in the current directory
valid_languages=($(ls -d */ | sed 's#/##'))

# Validate programming language
language_valid=false
for lang in "${valid_languages[@]}"; do
  if [ "$lang" == "$language" ]; then
    language_valid=true
    break
  fi
done

if [ "$language_valid" == false ]; then
  echo "Invalid programming language. Must be one of: ${valid_languages[@]}"
  exit 1
fi

# Validate difficulty
if [[ ! "$difficulty" =~ ^(easy|medium|hard)$ ]]; then
  echo "Invalid difficulty. Must be one of: easy, medium, hard."
  exit 1
fi

# Build directory path
dir="$language/$difficulty"

# Check if the directory exists, create if not
if [ ! -d "$dir" ]; then
  mkdir -p "$dir"
fi

# Create the file with a template content if it doesn't exist
file_path="$dir/$filename"
if [ ! -f "$file_path" ]; then
  echo "// Solution for $filename" > "$file_path"
fi

# Update readme (assuming python3 update_readme.py exists)
python3 update_readme.py

# Git operations
git pull
git add .
git commit -m "$message"
git push

echo "Solution submitted!"

