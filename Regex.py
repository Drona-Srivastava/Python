import re
pattern='wiki'
text='''A wiki (/ˈwɪki/ ⓘ WIK-ee) is an on
line hypertext publication collaboratively edited and managed by its own audience, using a web browser. A typical wiki contains multiple pages for the subjects or scope of the project, and could be either open to the public or limited to use within an organization for maintaining its internal knowledge base.
Wikis are enabled by wiki software, other
wise known as wiki engines. A wiki engine,
being a form of a content management system,
differs from other web-based systems such as
blog software, in that the content is created
without any defined owner or leader, and wikis
have little inherent structure, allowing structure
to emerge according to the needs of the users.[1] Wiki
engines usually allow content to be written using a
simplified markup language and sometimes edited with the
help of a rich-text editor.[2] There are dozens of different
wiki engines in use, both standalone and part of other software,
such as bug tracking systems. Some wiki engines are free and open-source,
whereas others are proprietary. Some permit control over different functions (
levels of access); for
example, editing rights may permit changing,
adding, or removing material.A'''
match1=re.match(pattern,text) #searches just at the start
match2=re.search(pattern,text) #searches al throughout the string adn gives first occurence
match3=re.fullmatch(pattern,text) #returns only if pattern is exactly same as text otherwise none
match4=list(re.finditer(pattern,text)) #searches all through the string and gives all the occurences
for i in match4 :
    print(i.span()) #to get location of the searched string 
print(match1)
print(match2)
print(match3)
print(match4) 
