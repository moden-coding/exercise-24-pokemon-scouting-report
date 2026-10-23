import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

try:
    import pandas as pd
except ModuleNotFoundError:
    raise ModuleNotFoundError(
        "pandas is not installed for the Python running these tests:\n"
        f"    {sys.executable}\n"
        "Select the conda/Anaconda interpreter (Cmd/Ctrl+Shift+P → Python: Select Interpreter), "
        "trash the terminal and open a new one. If you have the extension "
        "'Python Test Explorer for Visual Studio Code', uninstall it and run tests "
        "from the 'Python Tests' tree."
    ) from None

from src.scouting import average_defense, hardest_hitter, hardest_hitter_speed

REAL = pd.read_csv(REPO_ROOT / "data" / "pokemon.csv")

MINI = pd.DataFrame({
    "Name":    ["Sprout", "Ember", "Ripple", "Pebble", "Gust", "Bolt", "Mossy"],
    "Attack":  [49, 52, 48, 90, 45, 55, 70],
    "Defense": [49, 43, 65, 100, 40, 30, 60],
    "Speed":   [45, 65, 43, 20, 56, 90, 40],
})


class TestAverageDefense(unittest.TestCase):
    def test_real_pokedex(self):
        result = average_defense(REAL)
        self.assertIsNotNone(result, msg="should return the average Defense, not None")
        self.assertAlmostEqual(result, 73.8, places=1,
                               msg="should be the average Defense of the real Pokédex")

    def test_small_table(self):
        result = average_defense(MINI)
        self.assertIsNotNone(result, msg="should return the average Defense, not None")
        self.assertAlmostEqual(result, 55.3, places=1,
                               msg="should be the average Defense of the small table")


class TestHardestHitter(unittest.TestCase):
    def test_real_pokedex(self):
        self.assertEqual(hardest_hitter(REAL), "MewtwoMega Mewtwo X",
                         msg="should be the Name of the Pokémon with the highest Attack")

    def test_small_table(self):
        self.assertEqual(hardest_hitter(MINI), "Pebble",
                         msg="should be the Name of the Pokémon with the highest Attack")


class TestHardestHitterSpeed(unittest.TestCase):
    def test_real_pokedex(self):
        self.assertEqual(hardest_hitter_speed(REAL), 130,
                         msg="should be the Speed of the Pokémon with the highest Attack")

    def test_small_table(self):
        self.assertEqual(hardest_hitter_speed(MINI), 20,
                         msg="should be the Speed of the Pokémon with the highest Attack")


if __name__ == "__main__":
    unittest.main()
