import re

message = "Call office at 123-123-1234"

phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
matched_object = phoneNumberRegex.search(message)
print(matched_object.group())

area_code = matched_object.group(1)
print(area_code)

number = matched_object.group(2)
print(number)
