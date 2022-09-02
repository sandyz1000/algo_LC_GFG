"""
Factory method move instance creation to it's subclasses.
Advantages:
1. It decoupled the code that create objects from the code that uses them, reducing the complexity of maintainence
2. It makes code more universal, not being tied to the concreate class but to the interface
"""

from urllib.request import urlopen, URLError
from bs4 import BeautifulSoup
from abc import abstractmethod, ABCMeta


class Port(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __str__(self):
        pass


class Protocol(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __str__(self):
        pass


class Connector(object):
    """
    Connector class need to be implemented by it's subclass. It has 2 method protocol_factory and
    port_factory both interfaces need to be defined in their child class
    """
    __metaclass__ = ABCMeta

    def __init__(self, is_secure):
        self.is_secure = is_secure
        self.port = self.factory_port()
        self.protocol = self.factory_protocol()

    @abstractmethod
    def parse(self, content):
        pass

    def read(self, host, path):
        url = self.protocol + "://" + host + ":" + str(self.port) + path
        try:
            return urlopen(url, timeout=2).read()
        except URLError as e:
            print("Error occurred: ", e)
            return None

    @abstractmethod
    def factory_port(self):
        """
        In case of FTPPort the port n will be 22 and in case of Http it will be 80
        :return:
        """
        pass

    @abstractmethod
    def factory_protocol(self):
        """
        This factory will be different for http and ftp and need to redefined in their child class
        :return:
        """
        pass


class HttpConnector(Connector):
    def parse(self, content):
        soup = BeautifulSoup(content)
        links = soup.find_all('a')
        filenames = [link['href'] for link in links]
        return "\n".join(filenames)

    def factory_protocol(self):
        if self.is_secure:
            return HttpsProtocol()
        return HttpProtocol()

    def factory_port(self):
        if self.is_secure:
            return HttpsPort()
        return HttpPort()


class FtpConnector(Connector):
    def parse(self, content):
        lines = content.split('\n')
        filenames = []
        for line in lines:
            # The FTP format typically has 8 columns, split them
            splitted_line = line.split(None, 8)
            if len(splitted_line) == 9:
                filenames.append(splitted_line[-1])

        return '\n'.join(filenames)

    def factory_protocol(self):
        return FtpProtocol()

    def factory_port(self):
        return FtpPort()


class HttpPort(Port):
    """A concrete product which represents http port."""
    def __str__(self):
        return "80"


class HttpsPort(Port):
    """A concrete product which represents https port."""

    def __str__(self):
        return "443"


class FtpPort(Port):
    """A concrete product which represents ftp port."""
    def __str__(self):
        return "22"


class HttpProtocol(Protocol):
    """A concrete product which represents http protocol."""

    def __str__(self):
        return "http"


class HttpsProtocol(Protocol):
    """A concrete product which represents https protocol."""

    def __str__(self):
        return "https"


class FtpProtocol(Protocol):
    """A concrete product which represents ftp protocol."""

    def __str__(self):
        return "ftp"


if __name__ == '__main__':
    domain = 'ftp.freebsd.org'
    path = '/pub/FreeBSD/'
    protocol = input('Connecting to {}. Which Protocol to use? (0-http, 1 - ftp): '.format(domain))
    if protocol == 0:
        is_secure = bool(input('Use secure connection? (1-yes, 0-no): '))
        connector = HttpConnector(is_secure)
    else:
        is_secure = False
        connector = FtpConnector(is_secure)

    content = connector.read(domain, path)
    if content is not None:
        print(connector.parse(content))
