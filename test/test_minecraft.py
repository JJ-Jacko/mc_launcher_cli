from typing import List
from unittest import TestCase

from mc_launcher_cli.env import get_minecrafts
from mc_launcher_cli.datas import Minecraft


class TestMinecraft(TestCase):
    minecrafts: List[Minecraft]

    @classmethod
    def setUpClass(cls):
        cls.minecrafts = get_minecrafts()

    def test_get_mcs_returns_list(self):
        self.assertIsInstance(self.minecrafts, list)
        for mc in self.minecrafts:
            self.assertIsInstance(mc, Minecraft)

    def test_discovered_mcs_have_required_files(self):
        for mc in self.minecrafts:
            self.assertTrue((mc.HOME / f"{mc.ID}.json").is_file())
            self.assertTrue((mc.HOME / f"{mc.ID}.jar").is_file())

    def test_discovered_mcs_have_metadata(self):
        for mc in self.minecrafts:
            self.assertTrue(mc.ID)
            self.assertTrue(mc.HOME)
            self.assertTrue(mc.VERSION)