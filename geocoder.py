from geopy.geocoders import Nominatim  # pylint: disable=import-error
from geopy.extra.rate_limiter import RateLimiter  # pylint: disable=import-error

# friends_list = [{'Name': 'stylebender', 'Location': 'Auckland New Zealand'}, {'Name': 'arielhelwani', 'Location': 'Born in Montréal, QC, Canada'}, {'Name': 'thesoundofaja', 'Location': 'Manhattan, NY'}, {'Name': 'LindsJacobellis', 'Location': 'Everywhere'}, {'Name': 'buffa82', 'Location': 'St Louis, MO'}, {'Name': 'donwinslow', 'Location': 'Repped by The Story Factory'}, {'Name': '321gaux', 'Location': 'Las Vegas, NV'}, {'Name': 'VetsandPlayers', 'Location': 'Los Angeles, CA'}, {'Name': 'JayGlazer', 'Location': 'ÜT: 34.072426,-118.400527'}, {'Name': 'PatMcAfeeShow', 'Location': 'Indianapolis'}]



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



