import pandas as pd

DATA_URL = "https://raw.githubusercontent.com/modengann/Data-sets/refs/heads/master/pokemon.csv"


def average_defense(df: pd.DataFrame) -> float:
    """How tough is the average Pokémon? Return the average Defense."""
    pass


def hardest_hitter(df: pd.DataFrame) -> str:
    """Who hits the hardest? Return the Name of the Pokémon with the highest Attack."""
    pass


def hardest_hitter_speed(df: pd.DataFrame) -> int:
    """How fast is the hardest hitter? Return the Speed of the Pokémon with the highest Attack."""
    pass


def main():
    df = pd.read_csv(DATA_URL)
    print("The average Pokémon has this much Defense:", average_defense(df))
    print("The hardest hitter is:", hardest_hitter(df))
    print("The hardest hitter's Speed is:", hardest_hitter_speed(df))
    print("For comparison, the average Speed is:", df["Speed"].mean())


if __name__ == "__main__":
    main()
