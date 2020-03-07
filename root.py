from pathlib import Path

p = Path('/root/root.txt')
with open(p, 'r') as f:
    with open('root.txt', 'w') as r:
        r.write(f.readlines()[0])
        r.close()
    f.close()
