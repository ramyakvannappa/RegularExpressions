# importing the module that has all regular expressions in it
import re

message = "Call office at 123-123-1234"

# creating regular expression object
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# using search method to find a sting for the above phone number pattern
matched_object = phoneNumberRegex.search(message)
print(matched_object.group())


message2 = "Call office at 123-123-1234 or 111-222-3333"
# creating regular expression object

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# using search method to find a sting for the above phone number pattern
matched_object = phoneNumberRegex.findall(message2)
print(matched_object) # list of all the phone numbers


