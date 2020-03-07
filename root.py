with open('/root/root.txt', 'r') as f:
    with open('root.txt', 'w') as r:
        r.write(f.readlines()[0])
        r.close()
    f.close()
