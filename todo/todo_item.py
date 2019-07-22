from datetime import datetime


def strike(text):
    return ''.join([u'{}\u0336'.format(c) for c in text])


class TodoItem:
    __separator = ' -> '
    __done_date_placeholder = 'not done yet'

    def __init__(self, content, creation_date=None):
        self.content = content
        if isinstance(creation_date, datetime):
            self.creation_date = creation_date
        elif creation_date is None:
            self.creation_date = datetime.now()
        else:
            raise ValueError('creation date must be type datetime or None')
        self.done_date = None

    def done(self, done_date=None):
        if isinstance(done_date, datetime):
            self.done_date = done_date
        elif done_date is None:
            self.done_date = datetime.now()
        else:
            raise ValueError('done date must be type datetime or None')

    def undone(self):
        self.done_date = None

    @property
    def status(self):
        if self.done_date is None:
            return 'todo'
        else:
            return 'done'

    def __str__(self):
        out = self.creation_date.strftime('%Y-%m-%d %H:%M:%S')
        if self.status == 'todo':
            out += ' - '
            out += self.content
        elif self.status == 'done':
            out += ' X '
            out += self.content + " (done on " + self.done_date.strftime('%Y-%m-%d %H:%M:%S)')
        return out

    def serialize(self):
        out = self.creation_date.strftime('%Y-%m-%d %H:%M:%S')
        if self.status == 'done':
            out += TodoItem.__separator + self.done_date.strftime('%Y-%m-%d %H:%M:%S')
        else:
            out += TodoItem.__separator + TodoItem.__done_date_placeholder
        out += TodoItem.__separator + self.content
        return out

    @staticmethod
    def deserialize(item):
        item = item.strip()
        fields = item.split(TodoItem.__separator, 2)
        if len(fields) != 3:
            raise ValueError('Bad format of item')
        try:
            creation_date = datetime.strptime(fields[0], '%Y-%m-%d %H:%M:%S')
        except ValueError:
            raise ValueError('Bad format of creation date')

        content = fields[2]
        deserialized_item = TodoItem(content, creation_date)

        if fields[1] != TodoItem.__done_date_placeholder:
            try:
                done_date = datetime.strptime(fields[1], '%Y-%m-%d %H:%M:%S')
            except ValueError:
                raise ValueError('Bad format of done date')
            else:
                deserialized_item.done(done_date)

        return deserialized_item
