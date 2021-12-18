
import re

# creating regex patterns for phone numbers
phoneRegex = re.compile(r''' 
    (((\d\d\d)|(\(\d\d\d\)))? # area code 111 or (111)  , ? => optional          
    (\s|-)             # separator whitespace or a - 
    \d\d\d           # first three digits
    -                # seperator
    \d\d\d\d         # last four digits
    (((ext(\.)?\s)|x) # extension , optional, space, digits after that  ext 1234, ext.1234,x1234
    (\d{2,5}))?)
     ''', re.VERBOSE)

# creating regex for email address
emailRegex = re.compile('''
   [a-zA-Z0-9_.+]+
   @
   [a-zA-Z0-9_.+]+
   ''', re.VERBOSE)

text = "abc@xyx.com, 1235454,123-333-3333, adasfdfds.xyz, (123)-456-7890 ext 12334"
# extracting email/phone
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

phonenumberlist = []
for eachphonenumber in extractedPhone:
    phonenumberlist.append(eachphonenumber[0])

print(extractedPhone) # [('123-333-3333', '123', '123', '', '-', '', '', '', '', ''), ('(123)-456-7890', '(123)', '', '(123)', '-', '', '', '', '', '')]
print(extractedEmail) # ['abc@xyx.com']
print(phonenumberlist) # ['123-333-3333', '(123)-456-7890']

results = '\n'.join(phonenumberlist) + '\n'+ '\n'.join(extractedEmail)
print(results)

