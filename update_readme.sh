#!/bin/bash

current_directory=$(pwd)

directories=$(find . -maxdepth 1 -type d -not -path '*/\.*' | sed 's|./||')

declare -A directory_file_counts
declare -A language_counts

for directory in $directories; do
    directory_file_counts[$directory]=0
done

for directory in $directories; do
    for subdir in 'easy' 'medium' 'hard'; do
        subdir_path="$current_directory/$directory/$subdir"
        if [ -d "$subdir_path" ]; then
            files=$(find "$subdir_path" -maxdepth 1 -type f | wc -l)
            directory_file_counts[$directory]=$((${directory_file_counts[$directory]} + $files))
            language_counts[$subdir]=$((${language_counts[$subdir]} + $files))
        fi
    done
done

total_solutions=0
for count in "${directory_file_counts[@]}"; do
    total_solutions=$((total_solutions + count))
done

readme_content="
**Leet Code Solutions**

- Link to Profile: [LeetCode](https://leetcode.com/u/ChloeCrozier/)

**Solutions:** $total_solutions

"

for category in 'easy' 'medium' 'hard'; do
    category_total=0
    for count in "${language_counts[$category]}"; do
        category_total=$((category_total + count))
    done

    # Capitalize the first letter of the category
    category_capitalized="$(tr '[:lower:]' '[:upper:]' <<< ${category:0:1})${category:1}"

    readme_content+="
- $category_capitalized: $category_total

"
    for directory in $directories; do
        count=${language_counts[$category]}
        if [ $count -gt 0 ]; then
            readme_content+="  -  $directory: $count

"
        fi
    done
done

echo "$readme_content" > README.md
