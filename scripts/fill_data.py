from apps.categories.models import Category
from apps.levels.models import Level
from apps.themes.models import Theme
from apps.words.models import Word


data = {
    'People and things': {
        'Food': {
            'level': 'A1',
            'words': [
                ('apple', 'яблуко'),
                ('bread', 'хліб'),
                ('pie', 'пиріг'),
            ]
        },
        'Human body': {
            'level': 'A2',
            'words': [
                ('nose', 'ніс'),
                ('eye', 'око'),
                ('ear', 'вухo'),
            ]
        }
    },
    'Time and dates': {
        'Months': {
            'level': 'B1',
            'words': [
                ('January', 'Січень'),
                ('February', 'Лютий'),
                ('March', 'Березень'),
                ('April', 'Квітень'),
                ('May', 'Травень'),
            ]
        }
    }
}


def add_data():
    # todo write or remove
    for category, themes in data:
        category_obj = Category(name=category)
        category_obj.save()
        for theme, attributes in themes:
            theme_obj = Theme(name=theme, )


if __name__ == '__main__':
    add_data()