import pygal_maps_world.maps


wm = pygal_maps_world.maps.World()
wm.title = 'North, Central, and South America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gd', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'cl', 'co', 'ec', 'gf',
    'gy', 'pe', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')