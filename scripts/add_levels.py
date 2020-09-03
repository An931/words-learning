from apps.levels.models import Level

LEVELS = (
    ('A0', 'Beginner'),
    ('A1', 'Elementary'),
    ('A2', 'Pre-Intermediate'),
    ('B1', 'Intermediate'),
    ('B2', 'Upper Intermediate'),
    ('C1', 'Advanced'),
    ('C2', 'Proficiency')
)


def run():
    add_levels()


def add_levels():
    """Add necessary levels to db"""
    for level in LEVELS:
        level_obj = Level(name=level[1], code=level[0])
        level_obj.save()




