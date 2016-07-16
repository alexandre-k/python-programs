import unittest
from urlparser import urlParser

class basicProtoParsing(unittest.TestCase):
    def assertProtocol(self, url, expected_protocol):
        parser = urlParser(url)
        self.assertEqual(parser.protocol, expected_protocol)

    def test_html_proto(self):
        self.assertProtocol('http://www.essex.ac.uk', 'http')

    def test_ftp_proto(self):
        self.assertProtocol('ftp://www.essex.ac.uk', 'ftp')

    def test_other_proto(self):
        self.assertProtocol('smb://other.com', 'smb')

class basicSiteParsing(unittest.TestCase):
    def assertSite(self, url, expected_site):
        parser = urlParser(url)
        self.assertEqual(parser.site, expected_site)

    def assertPath(self, url, expected_path):
        parser = urlParser(url)
        self.assertEqual(parser.path, expected_path)

    def test_with_simple_path(self):
        self.assertSite('http://google.com/search', 'google.com')

    def test_empty_path(self):
        self.assertPath('http://google.com', '')

    def test_empty_path_with_slash(self):
        self.assertPath('http://google.com/', '')

