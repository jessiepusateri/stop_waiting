prerequisites = {
    'pebble_any': [
        set(['pebble original']),
        set(['pebble steel']),
        set(['pebble time']),
        set(['pebble time steel'])
    ],
    'nightscout': [
        set(['dexcom g5', 'ios']),
        set(['dexcom g4 share', 'ios']),
        set(['dexcom g4 share', 'android']),
        set(['dexcom g4', 'android']),
        set(['medtronic 530g', 'android']),
        set(['medtronic minimed connect', 'ios']),
        set(['medtronic 640g', 'android']),
        set(['freestyle libre', 'android'])
    ]
}

pebble_apps = {
    # Github: https://github.com/mddub/urchin-cgm
    # Pebble Store: beta - not released yet
    'urchin':[
        set(['nightscout', 'pebble_any'])
    ],

    # Github: ?
    # Pebble Store: https://apps.getpebble.com/en_US/application/578a92d21e00a66bb1000199
    'cgm in the sky': [
        set(['nightscout', 'pebble_any'])
    ],

    # Github: https://github.com/hackingtype1/cgm-simple-spark
    # Pebble Store:
    'simple cgm spark': [
        set(['nightscout', 'pebble_any'])
    ],

    # Github: https://github.com/hackingtype1/cgm-simple-pebble
    # Pebble Store: https://apps.getpebble.com/en_US/application/557c3091d269ce13b300001a
    'simple cgm': [
        set(['nightscout', 'pebble_any'])
    ],

    # Github:
    # Pebble Store:
    'nightscout duo': [
        set(['nightscout', 'pebble_any'])
    ]
}

apple_watch_apps = {
    # Github: https://github.com/nightscout/nightscout-apple-watch
    # Apple Store: https://itunes.apple.com/us/app/mybg-continuous-glucose-monitor/id993805949?ls=1&mt=8
    'mybg': [
        set(['nightscout', 'apple watch'])
    ],

    # Github: https://github.com/someoneAnyone/Nightscouter
    # Apple Store: https://itunes.apple.com/us/app/nightscouter/id1010503247?mt=8
    'nightscouter': [
        set(['nightscout', 'apple watch'])
    ],

    # Github: https://github.com/nightscout/nightguard
    # Apple Store: ?
    # Gitter: https://gitter.im/nightscout/nightguard
    'nightguard': [
        set(['nightscout', 'apple watch'])
    ]
}

def check_list(need_list, have):
    for need in need_list:
        if need.issubset(have):
            return True
    return False

have = set(['dexcom g4 share', 'android', 'pebble time'])
possible_projects = []

for prerequisite_name in prerequisites.keys():
    print prerequisite_name
    if check_list(prerequisites[prerequisite_name], have):
        have.add(prerequisite_name)

for app in pebble_apps.keys():
    if check_list(pebble_apps[app], have):
        possible_projects.append(app)

print possible_projects