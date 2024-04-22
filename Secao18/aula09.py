from pprint import pprint
from re import findall

TEXTO = '''
ONLINE  192.168.0.1 GHIJK active
OFFLINE  192.168.0.2 GHIJK inactive
OFFLINE  192.168.0.3 GHIJK active
ONLINE  192.168.0.4 GHIJK active
ONLINE  192.168.0.5 GHIJK inactive
OFFLINE  192.168.0.6 GHIJK active
'''
# pprint(findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', TEXTO))

# pprint(findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)', TEXTO))

# pprint(findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)', TEXTO))

# pprint(findall(r'.+', TEXTO))

# pprint(findall(r'(?=.*inactive).+', TEXTO))
# pprint(findall(r'(?=.*[^in]active).+', TEXTO))

# pprint(findall(r'\w+(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', TEXTO))
# pprint(findall(r'\w+(?<!ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', TEXTO))

# pprint(findall(r'\w+(?<=OFFLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', TEXTO))
# pprint(findall(r'\w+(?<!OFFLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', TEXTO))

# pprint(findall(r'\w+(?<!OFFLINE)\s+\d+\.\d+\.\d+\.\d+\s+\w+\s+\w+', TEXTO))
pprint(findall(r'(?<=OFFLINE)\s+\d+\.\d+\.\d+\.\d+\s+\w+\s+\w+', TEXTO))
pprint(findall(r'\w+(?<=OFFLINE)\s+\d+\.\d+\.\d+\.\d+\s+\w+\s+\w+', TEXTO))
