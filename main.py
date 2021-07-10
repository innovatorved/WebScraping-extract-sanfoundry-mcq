from sanfoundryClass import copyit


# Enter the First Page Url of any topic you want
url = "https://www.sanfoundry.com/operating-system-questions-answers-basics/"
data = copyit(url)

print(data.copyright())

# print(len(data.extract_list()))
# print(len(data.extract_dict()))
# print(data.extract_str()[:100])

data.extract_pdf()