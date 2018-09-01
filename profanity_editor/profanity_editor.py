# =============================================================================
# 1. read text from a document
# 2. check for curse words
# Code returns error urllib.urlopen deprecated with Python 3. Fixed by using quote function
# =============================================================================
import urllib.request

def read_text():
    #name of the file = quotes, open it
    #an object of the file, something like __init__
    quotes = open("/Users/Austin/Desktop/Software Engineering/Python/CS036/profanity_editor/movie_quotes.txt")
    #read the content of movie quotes
    contents_of_file = quotes.read()
    #print content
    print(contents_of_file)
    #close file
    quotes.close()
    profanity_check(contents_of_file)
        
def profanity_check(text_to_check):
    #add quote to read url properly
    quoted_text_to_check = urllib.request.quote(text_to_check)
    with urllib.request.urlopen ("http://www.wdylike.appspot.com/?q="+quoted_text_to_check) as connection:
        output = connection.read()
    #print(output)
    connection.close()
    if b"true" in output:
        print ("profanity alert!")
    elif b"false" in output:
        print ("this document has no curse words!")
    else:
        print ("could not scan the document properly")
        
read_text()
