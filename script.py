import os
import socket
from collections import Counter
import re

# Function to read file and return the content as a list of words
def read_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    # Convert to lowercase and split into words using regex to handle punctuation
    words = re.findall(r'\b\w+\b', text.lower())
    return words

# Read the text files
file_1_path = '/home/data/IF-1.txt'
file_2_path = '/home/data/AlwaysRememberUsThisWay-1.txt'

words_file_1 = read_file(file_1_path)
words_file_2 = read_file(file_2_path)

# Count total number of words in each file
total_words_file_1 = len(words_file_1)
total_words_file_2 = len(words_file_2)

# Calculate the grand total word count
grand_total_words = total_words_file_1 + total_words_file_2

# Count the frequency of words in file 1 and find the top 3 most frequent words
counter_file_1 = Counter(words_file_1)
top_3_file_1 = counter_file_1.most_common(3)

# Handle contractions in file 2 (e.g., I'm -> I, am) and count the frequency of words
contractions = {
    "i'm": ['i', 'am'],
    "can't": ['can', 'not'],
    "don't": ['do', 'not'],
    "won't": ['will', 'not'],
    # Add other contractions as needed
}

def handle_contractions(words):
    expanded_words = []
    for word in words:
        if word in contractions:
            expanded_words.extend(contractions[word])
        else:
            expanded_words.append(word)
    return expanded_words

words_file_2_expanded = handle_contractions(words_file_2)
counter_file_2 = Counter(words_file_2_expanded)
top_3_file_2 = counter_file_2.most_common(3)

# Get the IP address of the machine running the container
ip_address = socket.gethostbyname(socket.gethostname())

# Prepare the result to write to the result.txt file
result = f"""
Total words in IF-1.txt: {total_words_file_1}
Total words in AlwaysRememberUsThisWay-1.txt: {total_words_file_2}
Grand total words across both files: {grand_total_words}

Top 3 most frequent words in IF-1.txt:
"""
for word, count in top_3_file_1:
    result += f"{word}: {count}\n"

result += f"\nTop 3 most frequent words in AlwaysRememberUsThisWay-1.txt (with contractions handled):\n"
for word, count in top_3_file_2:
    result += f"{word}: {count}\n"

result += f"\nIP Address of the container: {ip_address}\n"

# Write the results to a file
output_dir = '/home/data/output'
os.makedirs(output_dir, exist_ok=True)
result_file_path = os.path.join(output_dir, 'result.txt')
with open(result_file_path, 'w') as result_file:
    result_file.write(result)

# Print the result to console
print(result)
