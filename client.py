#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
"""
Simple WebScraping using URLLIB2

@author: Jaume Giralt Barbé
@author: Nil Agut Marín
@author: Jordi Blanco López
"""

import urllib2

class Client(object):
    """
    Web Client that gets the page:
    https://www.packtpub.com/packt/offers/free-learning/ and search the title
    of the book that it's free today. After print the title and notified.
    """

    def __init__(self):
        super(Client, self).__init__()

    def get_web_page(self, url):
        """
        The function retrieves an HTML URL and return the HTML.
        :param url: String that contains the HTML URL.
        :return: The HTML of the page.
        """
        f = urllib2.urlopen(url)
        html = f.read()
        f.close()
        return html

    def run(self):
        """
        Retrieves the title of the free book of the day from the web page:
        https://www.packtpub.com/packt/offers/free-learning/ and print it
        :return: The title of the free book
        """
        html = self.get_web_page("https://www.packtpub.com/packt/offers/free"
                                 "-learning/")
        print(html)
