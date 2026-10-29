import os

from crawlora_opendota import OpenDotaClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with OpenDotaClient(api_key=api_key) as client:
    heroes = client.heroes()
    print('heroes', heroes)
    pro_matches = client.pro_matches()
    print('pro_matches', pro_matches)
