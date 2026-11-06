from unittest import TestCase

from mc_launcher_cli.env import get_javas
from mc_launcher_cli.env import get_minecrafts


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

    def test_get_mcs_returns_list(self):
        self.assertIsInstance(get_minecrafts(), list)

    def test_discovered_mcs_have_required_files(self):
        for mc in get_minecrafts():
            self.assertTrue((mc.HOME / f"{mc.ID}.json").is_file())
            self.assertTrue((mc.HOME / f"{mc.ID}.jar").is_file())

    def test_discovered_mcs_have_metadata(self):
        for mc in get_minecrafts():
            self.assertTrue(mc.ID)
            self.assertTrue(mc.HOME)
            self.assertTrue(mc.VERSION)