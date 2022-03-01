import pygal_maps_world.maps


wm = pygal_maps_world.maps.World()
wm.title = 'Populations of North America'
wm.add('North America', {'ca': 3412600, 'us': 30934900, 'mx': 113423000})
wm.render_to_file('no_populations.svg')
