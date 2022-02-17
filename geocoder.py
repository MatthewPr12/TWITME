from geopy.geocoders import Nominatim  # pylint: disable=import-error
from geopy.extra.rate_limiter import RateLimiter  # pylint: disable=import-error


def get_coords(friends_lst):
    geocoder = RateLimiter(Nominatim(user_agent="TWITME").geocode, min_delay_seconds=1)
    # d = {'Name': 'stylebender', 'Location': 'Auckland New Zealand'}
    # print(geocoder(d['Location']).latitude)

    friends = []
    for i in friends_lst:
        try:
            lat = geocoder(i['Location']).latitude
            lon = geocoder(i['Location']).longitude
            i['Coords'] = (lat, lon)
            friends.append(i)
        except AttributeError:
            continue
    return friends



