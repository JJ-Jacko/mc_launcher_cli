from unittest import TestCase

from mc_launcher_cli.env import get_javas


class TestManageRuntime(TestCase):
    def test_get_jdks_returns_list(self):
        self.assertIsInstance(get_javas(), list)

    def test_discovered_jdks_have_required_files(self):
        for java in get_javas():
            self.assertTrue((java.HOME / "bin/java.exe").is_file())
            self.assertTrue((java.HOME / "bin/javac.exe").is_file())

    def test_discovered_jdks_have_metadata(self):
        for java in get_javas():
            self.assertTrue(java.IMPLEMENTOR)
            self.assertTrue(java.VERSION)
            self.assertTrue(java.OS_ARCH)