# A regular expression in Python (often referred to as "regex") is a sequence of characters that forms a search pattern. It's used to match and manipulate text based on patterns. 

# Here's an example that showcases how you might use a regular expression to find and extract email addresses from a given text:

import re

text = "Send an email to john@example.com and mary@example.com"
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

emails = re.findall(pattern, text)
print(emails)  # Output: ['john@example.com', 'mary@example.com']

#In this example:
#- `re.findall()` searches for all occurrences of the pattern within the text.
#- The regular expression pattern `r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'` looks for email addresses in the provided text.
#- It uses specific rules to identify email patterns, but the breakdown of the pattern is quite complex and specific to email structures.

#Regular expressions are powerful tools used for pattern matching and text manipulation in Python and many other programming languages. They allow for flexible and sophisticated text pattern matching