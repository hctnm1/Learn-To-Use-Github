"""
Coded by Rohan j
on 20/07/2020
github user id:- rohan-cce
"""

import contextlib
#The contextlib module contains utilities for working with context managers and the with statement
#,common use case of context managers is locking and unlocking resources and closing opened files"""

from urllib.parse import urlencode
#urlencode is often needed when we are calling a remote api with additional query strings or path parameters

from urllib.request import urlopen
#urlopen is capable of fetching URLs using a variety of different protocols.

def shorten_url(url): 

    request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url':url}))
    #URL encoding is often needed when we are calling a remote api with additional query strings or path parameters
    #Any query string or path parameter placed in the URL must be properly URL encoded
    
    with contextlib.closing(urlopen(request_url)) as response:
        #contextlib.closing closes resources like files, sockets, etc
        #and is a nice way to guarantee resources are always closed properly"""

        return response.read().decode('utf-8 ')
        #will decode the returned bytes object to string once it determines or guesses the appropriate encoding

ip=input("Enter url to shorten : ")
#asking for input from user

print(shorten_url(ip))
#printing the shortened url
