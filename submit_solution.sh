#!/bin/bash

# Check for 4 arguments
if [ $# -ne 4 ]; then
  echo "Usage: ./submit_solution [programming-language] [difficulty] [file_name] [message]"
  exit 1
fi

# Extract arguments
language="$1"
difficulty="$2"
filename="$3"
message="$4"

# Validate programming language
if [[ ! "$language" =~ ^(cpp|python|javascript|java|mysql)$ ]]; then
  echo "Invalid programming language. Must be python or java."
  exit 1
fi

# Validate difficulty
if [[ ! "$difficulty" =~ ^(easy|medium|hard)$ ]]; then
  echo "Invalid difficulty. Must be easy, med, or hard."
  exit 1
fi

# Build directory path
dir="$language/$difficulty"

# Open file in nano editor
nano "$dir/$filename"

# Update readme (assuming python3 update_readme.py exists)
python3 update_readme.py

# Git operations
git pull
git add .
git commit -m "$message"
git push

echo "Solution submitted!"

