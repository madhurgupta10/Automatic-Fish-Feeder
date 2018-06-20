from fishfeeder import FishFeeder

import firebase

url = "{your firebase url}"

while True:
    result = firebase.get(url)

    if (result['action'] == True):
        FishFeeder().FeedNow(0, 90)
        firebase.put(url, {'action': False})