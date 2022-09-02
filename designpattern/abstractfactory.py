"""
When we need to create family of object, it isolates the creation of object from the client
and only provide a interface method to interact with it
Advantages:
1. It isolates the concrete class from the class
2. It ensure the compatibility of the product in the product family

Disadvantages:
1. Adding a new product to the existing factories will be difficult because AbstractFactory will
be using fixed set of product interface so adding new product means extending the interface
"""
from __future__ import print_function, unicode_literals

from urllib.request import URLError, urlopen
from bs4 import BeautifulSoup
from abc import ABCMeta, abstractmethod


class AbstractFactory(object):
    __metaclass__ = ABCMeta

    def __init__(self, is_secure=False):
        self.is_secure = is_secure

    @abstractmethod
    def create_port(self):
        pass

    @abstractmethod
    def create_parser(self):
        pass

    @abstractmethod
    def create_protocol(self):
        pass


class HttpFactory(AbstractFactory):
    """
    The HttpFactory create factory of related object HttpPort, HttpProtocol and HttpParser
    """
    def create_parser(self):
        return HttpParser()

    def create_port(self):
        if self.is_secure:
            return HttpsPort()
        return HttpPort()

    def create_protocol(self):
        if self.is_secure:
            return HttpsProtocol()
        return HttpProtocol()


class FtpFactory(AbstractFactory):
    """
    The FtpFactory create factory of related object FtpPort, FtpProtocol and FtpParser
    """

    def create_parser(self):
        return FtpParser()

    def create_port(self):
        return FtpPort()

    def create_protocol(self):
        return FtpProtocol()


class Parser(object):
    __metaclass__ = ABCMeta

    def __call__(self, content, *args, **kwargs):
        """ The parser class will be callable that will parse the content"""
        pass


class Port(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __str__(self):
        pass


class Protocol(object):
    __metaclass__ = ABCMeta

    def __str__(self):
        pass


class HttpParser(Parser):
    def __call__(self, content, *args, **kwargs):
        soup = BeautifulSoup(content)
        links = soup.find_all('a')
        filenames = [link['href'] for link in links]
        return "\n".join(filenames)


class FtpParser(Parser):
    """ Concreate class implementation of parser to parse ftp content"""
    def __call__(self, content, *args, **kwargs):
        lines = content.split("\n")
        filenames = []
        for line in lines:
            # The FTP format typically has 8 columns, split them
            splitted_line = line.split(None, 8)
            if len(splitted_line) == 9:
                filenames.append(splitted_line[-1])
        return '\n'.join(filenames)


class HttpPort(Port):
    def __str__(self):
        return "80"


class HttpsPort(Port):
    def __str__(self):
        return "443"


class FtpPort(Port):
    def __str__(self):
        return "22"


class HttpProtocol(Protocol):
    def __str__(self):
        return "http"


class HttpsProtocol(Protocol):
    def __str__(self):
        return "https"


class FtpProtocol(Protocol):
    def __str__(self):
        return "ftp"


class Connector(object):
    """
    Client class that will accept the concrete factory, and this factory will be used to
    inject protocol, port and method to parse
    """
    def __init__(self, factory):
        self.protocol = factory.create_protocol()
        self.port = factory.create_port()
        self.parse = factory.create_parse()

    def read(self, domain, path):
        url = self.protocol + "://" + domain + ":" + str(self.port) + path
        try:
            return urlopen(url, timeout=2).read()
        except URLError as e:
            print("Error occurred: ", e)
            return None


if __name__ == '__main__':
    domain = 'ftp.freebsd.org'
    path = '/pub/FreeBSD/'
    protocol = input('Connecting to {}. Which Protocol to use? (0-http, 1 - ftp): '.format(domain))
    if protocol == 0:
        is_secure = bool(input('Use secure connection? (1-yes, 0-no): '))
        factory = HttpFactory(is_secure)
    else:
        is_secure = False
        factory = FtpFactory(is_secure)

    connector = Connector(factory)
    content = connector.read(domain, path)
    if content is not None:
        print(connector.parse(content))