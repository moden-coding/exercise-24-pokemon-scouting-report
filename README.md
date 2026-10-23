# Scouting Report

Answer three questions about the Pokédex, one function each.

## The questions

All three functions are in `src/scouting.py`.

1. **How tough is the average Pokémon?** `average_defense(df)` returns the average Defense.
2. **Who hits the hardest?** `hardest_hitter(df)` returns the Name of the Pokémon with the highest Attack.
3. **How fast is the hardest hitter?** `hardest_hitter_speed(df)` returns the Speed of the Pokémon with the highest Attack.

Every function must work on any Pokédex table with these columns, not just this one; the tests also use a small practice table.

## How to run

- See your findings: `python src/scouting.py`
- Run the tests: `python -m unittest discover` (or use the "Python Tests" tree in the Testing panel)

## If tests won't run

- **"No module named pandas"**: select the conda/Anaconda interpreter (Cmd/Ctrl+Shift+P → Python: Select Interpreter), then trash the terminal and open a new one.
- If "Python Test Explorer for Visual Studio Code" is installed, uninstall it; it ignores your interpreter choice.
- Open the assignment folder itself (File → Open Folder), not a folder above it.
- Windows: if conda won't activate in the terminal, run `conda init powershell` once in Anaconda Prompt and restart VS Code.
