"""
draw web map via folium package
"""
import random
import folium  # pylint: disable=import-error
from folium import plugins  # pylint: disable=import-error


def create_map(friends):
    """
    draw map of friends
    :param friends:
    :return:
    """
    my_map = folium.Map(location=[*friends[0]['Coords']], zoom_start=10)
    mini_map = plugins.MiniMap(toggle_display=True)
    my_map.add_child(mini_map)
    plugins.ScrollZoomToggler().add_to(my_map)
    plugins.Fullscreen(position='topright').add_to(my_map)
    folium.raster_layers.TileLayer('CartoDB Dark_Matter').add_to(my_map)
    fg_friends = folium.FeatureGroup(name='Show friends')
    colors = ['red', 'blue', 'green', 'purple', 'orange',
              'darkred', 'lightred', 'beige', 'darkblue',
              'darkgreen', 'cadetblue', 'darkpurple',
              'pink', 'lightblue', 'lightgreen',
              'gray', 'black', 'lightgray']
    for i in friends:
        folium.Marker(location=[*i['Coords']], popup=i['Name'],
                      icon=folium.Icon(icon="fa-brands fa-twitter",
                                       prefix='fa',
                                       color=random.choice(colors))).add_to(fg_friends)

    fg_friends.add_to(my_map)
    folium.LayerControl().add_to(my_map)
    return my_map


if __name__ == "__main__":
    friends_l = [{'Name': 'MelaniePodolyak', 'Location': 'Ukraine',
                'Coords': (49.4871968, 31.2718321)},
               {'Name': 'osmachka', 'Location': 'Ukraine, Lviv', 'Coords': (49.841952, 24.0315921)},
               {'Name': 'mooyouri', 'Location': 'м. Львів', 'Coords': (49.8447678, 24.0567693)},
               {'Name': 'FamilyUCU', 'Location': 'Україна', 'Coords': (49.4871968, 31.2718321)},
               {'Name': 'ilm_ua', 'Location': 'Ukraine, Lviv', 'Coords': (49.841952, 24.0315921)},
               {'Name': 'Dema_Linnyk', 'Location': 'Lviv', 'Coords': (49.841952, 24.0315921)},
               {'Name': 'City_Light20', 'Location': 'Ternopil', 'Coords': (49.6630002, 25.6167516)},
               {'Name': 'TEDxUCU', 'Location': 'Львів, Україна', 'Coords': (49.841952, 24.0315921)},
               {'Name': 'The_OldLion', 'Location': 'Львів, вул. Старознесенська, 24-26',
                'Coords': (49.8508107, 24.0524873012697)}]
    print(create_map(friends_l))
