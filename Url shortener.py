#install required package 

pip install pyshorteners

#create tiny url

def urlShortner(url):

    type_tiny = pyshorteners.Shortener()

    short_url = type_tiny.tinyurl.short(url)

    return short_url

