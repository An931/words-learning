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


def add_levels():
    for level in LEVELS:
        level_obj = Level(name=level[1], code=level[0])
        level_obj.save()
        print(f'Level created: {level_obj.code} - {level_obj.name}')


if __name__ == '__main__':
    add_levels()
