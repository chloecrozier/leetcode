import os

current_directory = os.getcwd()

all_entries = os.listdir(current_directory)
directories = [entry for entry in all_entries if os.path.isdir(os.path.join(current_directory, entry)) and not entry.startswith('.')]

directory_file_counts = {directory: {'easy': 0, 'medium': 0, 'hard': 0} for directory in directories}
language_counts = {'easy': {}, 'medium': {}, 'hard': {}}

for directory in directories:
    for subdir in directory_file_counts[directory].keys():
        subdir_path = os.path.join(current_directory, directory, subdir)
        if os.path.exists(subdir_path) and os.path.isdir(subdir_path):
            files = [f for f in os.listdir(subdir_path) if os.path.isfile(os.path.join(subdir_path, f))]
            directory_file_counts[directory][subdir] = len(files)
            if subdir not in language_counts:
                language_counts[subdir] = {}
            language_counts[subdir][directory] = len(files)

readme_content = """
**Leet Code Solutions**

- Link to Profile: [Chloe's LeetCode Profile](https://leetcode.com/u/ChloeCrozier/)

**Solutions:** {}

""".format(sum(sum(counts.values()) for counts in directory_file_counts.values()))

for category in ['easy', 'medium', 'hard']:
    readme_content += "- " 
    category_total = sum(counts[category] for counts in directory_file_counts.values())
    readme_content += f"{category.capitalize()}: {category_total}\n"
    readme_content += "\n" 
    for directory, count in language_counts[category].items():
        if count > 0:
            readme_content += "  -" 
            readme_content += f"  {directory}: {count}\n"
            readme_content += "\n" 
    readme_content += "\n"

with open('README.md', 'w') as readme_file:
    readme_file.write(readme_content.strip())
