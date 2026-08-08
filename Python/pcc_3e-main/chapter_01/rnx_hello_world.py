from pathlib import Path

p = Path('src') / 'utils' / 'helpers.py'
print(p)          # src/utils/helpers.py (на Linux) или src\utils\helpers.py (на Windows)
print(p.name)     # helpers.py
print(p.stem)     # helpers
print(p.suffix)   # .py
print(p.parent)   # src/utils
