import unittest
from app.converter import Converter


class ConverterTest(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    def test_convert_01(self):
        self.assertEqual(Converter("a=b\ncd=1\nx=yz",
                                   "abdnab\nhello world\nx123x\nrandomstring\nasciiart").convert(),
                         "bbdnbb\nyz123yz\nbsciibrt\nrbndomstring\nhello world")  
        
    def test_convert_02(self):
        self.assertEqual(Converter("e=f\ng=h\nij=k",
                                   "example\nstringg\nij123\nmoretext\nfgeij").convert(),
                         "fhfk\nfxamplf\nstrinhh\nk123\nmorftfxt")
        
    def test_convert_03(self):
        self.assertEqual(Converter("s=t\nuv=w\nx=y",
                                   "sunset\nuvwx\nsuvx\nmoreinfo\nstuvx").convert(),
                         "twy\nttwy\nwwy\ntuntet\nmoreinfo")