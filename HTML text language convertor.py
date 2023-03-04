from googletrans import Translator
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

# Open the HTML file
file_name = input("Enter the file name or path of the file: ")
# providing the file name will require the program to present at the file location 
with open(file_name, "r", encoding="utf8") as f:
    html = f.read()

# Parse the HTML file with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
# print(soup) # ckecking how it looks

# Find all English text in the HTML file
english_text = []
# print(soup.find_all(text=True))
for tag in soup.find_all(text=True):
    # print(tag)
    if tag.parent.name not in ['style', 'script', 'head', 'title']:
    # if tag in ['span', 'title', 'button', 'h2', 'h3', 'a', 'p', 'h5', 'time', 'strong', 'h4']:
        if tag.strip() != '':
            english_text.append(tag)

# print(english_text) # checking all the extracted texts of the webpage

# Translate the English text to Hindi using deep_translator as the googletrans is not working properly
translator = Translator(service_urls=["translate.google.com"])
for text in english_text:
    # print(text)
    # hindi_text = translator.translate(text, src="en", dest="hi").text
    # hindi_text = GoogleTranslator(source='en', target='hi').translate(text)
    # text.replace_with(hindi_text)
    text.strip() # stripping the white spaces
    print(text) # text befor conversion
    if text.isdigit(): continue # checking for the text if it contain only digits in string form as giving this
    # type if input ot the api will gives Error
    hindi_text = GoogleTranslator(source='en', target='hi').translate(text)
    print(hindi_text) # text after conversion
    text.replace_with(hindi_text)

# Write the translated HTML back to the file
with open(file_name, "w", encoding="utf8") as f:
    f.write(str(soup))
