"""
    Url shortner which will shorten the url given and save it to pickle object.
    When user invoke the method with the shortened url it will redirect user to the actual web page
"""
import pickle
from flask import Flask


app = Flask(__name__, template_folder='views')


class Url(object):
    @classmethod
    def shorten(cls, full_url):
        """
        Shorten the url
        :param full_url:
        :return:
        """
        instance = cls()
        instance.full_url = full_url
        instance.short_url = instance.__create_short_url()
        Url.__save_url_mapping(instance)
        return instance

    @classmethod
    def get_by_short_url(cls, short_url):
        pass

    def __increment_string(self, string):
        """
        url: http://www.packtpub.com
        a -> b
        z -> aa
        az -> ba
        empty
        string -> a
        :param string: of type char arr
        :return: shortened_url of type string
        """
        if string == '':
            return 'a'
        last_char = string[-1]
        if last_char != 'z':
            return string[:-1] + chr(ord(last_char) + 1)

        return self.__increment_string(string[:-1]) + 'a'

    def __create_short_url(self):
        """Creates short url, saves it and returns it."""
        last_short_url = Url.__load_last_short_url()
        short_url = self.__increment_string(last_short_url)
        Url.__save_last_short_url(short_url)
        return short_url

    @staticmethod
    def __save_last_short_url(short_url):
        """Saves last generated short url."""
        pickle.dump(short_url, open("last_short.p", "wb"))

    @staticmethod
    def __load_last_short_url():
        """Returns last generated short url."""
        try:
            return pickle.load(open("last_short.p", "rb"))
        except IOError:
            return ''

    @staticmethod
    def __save_url_mapping(instance):
        """Saves short_url to Url instance mapping."""
        short_to_url = Url.__load_url_mapping()
        short_to_url[instance.short_url] = instance
        pickle.dump(short_to_url, open("short_to_url.p", "wb"))

    @staticmethod
    def __load_url_mapping():
        """Returns short_url to Url instance mapping."""
        try:
            return pickle.load(open("short_to_url.p", "rb"))
        except IOError:
            return {}


@app.route("/")
def index():
    """
    Render info about url shorten routes
    :return:
    """
    pass

@pp.route("/shorten/")
def shorten():
    """
    Return the shortened url of the full url
    :return:
    """
    pass

