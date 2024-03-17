proxies = []
with open("./proxies.txt", 'r') as f:
    for l in f:
        proxy = l.strip()
        proxies.append(proxy)
        print(proxy)
    
