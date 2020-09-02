# from apps.levels.models import Level
# from apps.categories.models import Category
#
# LEVELS = (
#     ('A0', 'Beginner'),
#     ('A1', 'Elementary'),
#     ('A2', 'Pre-Intermediate'),
#     ('B1', 'Intermediate'),
#     ('B2', 'Upper Intermediate'),
#     ('C1', 'Advanced'),
#     ('C2', 'Proficiency'),
# )
#
#
# def add_levels():
#     for level in LEVELS:
#         level_obj = Level(name=level[1], code=level[0])
#         level_obj.save()
#         print(f'Level created: {level_obj.code} - {level_obj.name}')
#
#
# CATEGORIES = (
#     'People and things',
#     'Appearance and character',
#     'Time and dates',
# )
#
#
# THEMES = ('Human body, Face, Things',)
#
# def add_categories():
#     for c in CATEGORIES:
#         c_obj = Category(c)
#         c_obj.save()
#         print()  # todo
#
# def add_data():
#     cat = Category('People and things')
#
# if __name__ == '__main__':
#     l = Level(name='jhhk', code='a1')
#     # todo if not in set then '-'
#     l.save()
#     print('success')
