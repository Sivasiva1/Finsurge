import re

text = "hello 123 world 456"
pattern = r"\d+"  # Matches digits
matches = re.match(pattern, text)
print("Matches:", matches)

text1 = "123 world 456"
matches = re.match(pattern, text1)
print("Matches:", matches.group())


matches = re.findall(pattern, text)
print("Matches:", matches)

