
from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        #print("Found a start tag  :", tag)
        print("Start : {}".format(tag))       
        print("-> {} > ".format(attrs))

    def handle_endtag(self, tag):
        #print("Found an end tag   :", tag)
        print("End   : {}".format(tag))       

    def handle_startendtag(self, tag, attrs):
        #print("Found an empty tag :", tag)
        print("Start : {}".format(tag))
        print("-> {} > ".format(attrs))

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
#parser.feed("<html><head><title>HTML Parser - I</title></head>"
#            +"<body><h1>HackerRank</h1><br /></body></html>")

parser.feed("<html><head><title>HTML Parser - I</title></head>"
            +"<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>")


'''
Task:
You are given an HTML code snippet of N lines. 
Your task is to print start tags, end tags and empty tags separately.

2
<html><head><title>HTML Parser - I</title></head>
<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>

Format your results in the following way:
Start : html
Start : head
Start : title
End   : title
End   : head
Start : body
-> data-modal-target > None
-> class > 1
Start : h1
End   : h1
Empty : br
End   : body
End   : html

'''
