from apps.categories.models import Category
from apps.levels.models import Level
from apps.themes.models import Theme
from apps.words.models import Word

data = {
    'People and things': {
        'Food': {
            'level': 'A1',
            'words': [
                ('apple', 'яблоко'),
                ('bread', 'хлеб'),
                ('pie', 'пирог'),
            ]
        },
        'Human body': {
            'level': 'A2',
            'words': [
                ('nose', 'нос'),
                ('eye', 'глаз'),
                ('ear', 'ухо'),
            ]
        }
    },
    'Time and dates': {
        'Months': {
            'level': 'B1',
            'words': [
                ('January', 'Январь'),
                ('February', 'Февраль'),
                ('March', 'Март'),
                ('April', 'Апрель'),
                ('May', 'Май'),
            ]
        }
    }
}


def add_data():
    """Fill db with some data objects"""
    for category, themes in data:
        category_obj = Category(name=category)
        category_obj.save()
        for theme, attributes in themes:
            level_obj = Level.objects.filter(code=attributes['level']).first()
            theme_obj = Theme(name=theme, level=level_obj, category=category_obj)
            theme_obj.save()
            for word in attributes['words']:
                word_obj = Word(name=word[0], translation=word[1], theme=theme_obj)
                word_obj.save()

            # todo check


if __name__ == '__main__':
    add_data()
