#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
"""
Simple WebScraping using URLLIB2 and BeautifulSoup.

@author: Jaume Giralt Barbé
@author: Nil Agut Marín
@author: Jordi Blanco López
"""

import urllib2
from bs4 import BeautifulSoup


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

    def parse_web_page(self, html):
        """
        Parses an html page searching the title of the free book.
        :param html: Source code of the page.
        :return: The title of the free book.
        """
        soup = BeautifulSoup(html, 'html.parser')
        result = soup.find("div", "dotd-title")
        book = result.find("h2")
        return book.text if book else "Error"

    def clean_result(self, result):
        return result.replace("\t", "").replace("\n", "")

    def run(self):
        """
        Retrieves the title of the free book of the day from the web page:
        https://www.packtpub.com/packt/offers/free-learning/ and print it.
        :return: The title of the free book.
        """
        html = self.get_web_page("https://www.packtpub.com/packt/offers/free"
                                 "-learning/")
        result = self.parse_web_page(html)
        title = self.clean_result(result)
        print title

if __name__ == "__main__":
    client = Client()
    client.run()
