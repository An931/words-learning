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
            theme_obj = Theme(name=theme, )
            # todo write


if __name__ == '__main__':
    add_data()
