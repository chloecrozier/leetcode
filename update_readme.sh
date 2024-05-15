#!/bin/bash

# Get the list of directories
directories=$(ls -d */)

# Remove trailing slash from directory names
directories=$(echo "$directories" | sed 's#/##')

# Update the README.md file
echo "**Leet Code Solutions**" > README.md
echo "" >> README.md
echo "Link to Profile: [Chloe's LeetCode Profile](https://leetcode.com/u/ChloeCrozier/)" >> README.md
echo "" >> README.md
echo "# Directories" >> README.md
echo "" >> README.md
echo "The current directories in the directory are:" >> README.md
echo "" >> README.md
echo "$directories" | while read -r dir; do
    echo "- $dir" >> README.md
done

echo "README.md updated with current directories."

