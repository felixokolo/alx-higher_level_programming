#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status
"""
if __name__ == "__main__":
    import requests
    import sys

    r = requests.get('https://swapi.co/api/people/?search={}'
                     .format(sys.argv[1])).json()
    print('Number of results: {}'.format(r.get('count')))
    for res in r.get('results'):
        print(res.get('name'))