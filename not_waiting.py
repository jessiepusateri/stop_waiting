class Project:
    def __init__(self, key, name=None, github=None, store_url=None, gitter=None, requirements=None):
        self.key = key
        self.name = name
        self.github = github
        self.gitter = gitter
        self.store_url = store_url
        self.requirements = requirements

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

pebble_watchfaces = [
    Project(
        key="cgm in the sky",
        name="CGM in the Sky",
        github=None,
        gitter=None,
        store_url="https://apps.getpebble.com/en_US/application/578a92d21e00a66bb1000199",
        requirements=[
            set(['nightscout', 'pebble_any'])
        ]
    ),
    Project(
        key="simple cgm",
        name="Simple CGM",
        github="https://github.com/hackingtype1/cgm-simple-pebble",
        gitter=None,
        store_url="https://apps.getpebble.com/en_US/application/557c3091d269ce13b300001a",
        requirements=[
            set(['nightscout', 'pebble_any'])
        ]
    ),
    Project(
        key="simple cgm spark",
        name="Simple CGM Spark",
        github="https://github.com/hackingtype1/cgm-simple-spark",
        gitter=None,
        store_url="https://apps.getpebble.com/en_US/application/56534d58d2d67de36d00005f",
        requirements=[
            set(['nightscout', 'pebble_any'])
        ]
    ),
    Project(
        key="urchin cgm",
        name="Urchin CGM",
        github="https://github.com/mddub/urchin-cgm",
        gitter=None,
        store_url=None, #beta - not yet released
        requirements=[
            set(['nightscout', 'pebble_any'])
        ]
    ),
    Project(
        key='nightscout duo',
        name="Nightscout Duo",
        github=None,
        gitter=None,
        store_url=None,
        requirements=[
            set(['nightscout', 'pebble_any'])
        ]
    ),

]

apple_watch_apps = [
    Project(
        key='mybg',
        name="MyBG",
        github='https://github.com/nightscout/nightscout-apple-watch',
        gitter=None,
        store_url='https://itunes.apple.com/us/app/mybg-continuous-glucose-monitor/id993805949?ls=1&mt=8',
        requirements=[
            set(['nightscout', 'apple_watch'])
        ]
    ),
    Project(
        key='nightscouter',
        name="Nightscouter",
        github='https://github.com/someoneAnyone/Nightscouter',
        gitter=None,
        store_url='https://itunes.apple.com/us/app/nightscouter/id1010503247?mt=8',
        requirements=[
            set(['nightscout', 'apple_watch'])
        ]
    ),
    Project(
        key='nightguard',
        name='Nightguard',
        github='https://github.com/nightscout/nightguard',
        gitter='https://gitter.im/nightscout/nightguard',
        store_url=None,
        requirements=[
            set(['nightscout', 'apple_watch'])
        ]
    ),

]

def check_list(need_list, have):
    for need in need_list:
        if need.issubset(have):
            return True
    return False

def check_possible_projects(have):
    possible_projects = []
    for prerequisite_name in prerequisites.keys():
        if check_list(prerequisites[prerequisite_name], have):
            have.add(prerequisite_name)

    for watchface in pebble_watchfaces:
        if check_list(watchface.requirements, have):
            possible_projects.append(watchface)

    for app in apple_watch_apps:
        if check_list(app.requirements, have):
            possible_projects.append(app)
    return possible_projects

phones = [
    'android',
    'ios'
]

pumps = [
    'medtronic 522/722',
    'medtronic 523/723',
    'medtronic 523/722 with update'
]

cgms = [
    'dexcom g5'
    'dexcom g4 share',
    'dexcom g4',
    'medtronic 530g/veo',
    'medtronic minimed connect',
    'medtronic 640g',
    'freestyle libre'
]

extra_hardware = [
    'rileylink',
    'xDrip'
]

if __name__ == "__main__":
    have = set(['dexcom g4 share', 'android', 'pebble time', 'apple_watch'])
    projects = check_possible_projects(have)
    for project in projects:
        print "You can download %s at %s" % (project.name, project.store_url)
        print "You can contribute to %s at %s" % (project.name, project.github)
    have = set(['android'])
    print check_possible_projects(have)