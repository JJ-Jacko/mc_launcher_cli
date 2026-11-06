from typing import List
from unittest import TestCase

from mc_launcher_cli.env import get_javas
from mc_launcher_cli.datas import Java


class TestJava(TestCase):
    javas: List[Java]

    @classmethod
    def setUpClass(cls):
        cls.javas = get_javas()
    
    def test_get_jdks_returns_list(self):
        self.assertIsInstance(self.javas, list)
        for java in self.javas:
            self.assertIsInstance(java, Java)

    def test_discovered_jdks_have_required_files(self):
        for java in self.javas:
            self.assertTrue((java.HOME / "bin/java.exe").is_file())
            self.assertTrue((java.HOME / "bin/javac.exe").is_file())

    def test_discovered_jdks_have_metadata(self):
        for java in self.javas:
            self.assertTrue(java.IMPLEMENTOR)
            self.assertTrue(java.VERSION)
            self.assertTrue(java.OS_ARCH)