import webbrowser
import sys
 
a_website = "https://www.youtube.com/results?search_query="

if len(sys.argv) > 0:
    sys.argv.pop(0)
    searchTerm = '+'.join(sys.argv)
    a_website = a_website + searchTerm
# Open url in a new window of the default browser, if possible

 
# Open url in a new page (“tab”) of the default browser, if possible
webbrowser.open_new_tab(a_website)