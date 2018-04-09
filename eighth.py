import urllib



def read_text():
    quotes = open("C:\Users\moham\Desktop\movie-quotes\movie_quotes\movie_quotes.txt")
    contents_of_files = quotes.read()
    quotes.close()
    check_profanity(contents_of_files)

def check_profanity(text_to_check) :
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    print output
    connection.close()



#print contents_of_files


read_text()