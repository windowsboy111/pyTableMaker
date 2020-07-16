class InvalidSettings(Exception):
    """The settings passed via kwargs from the constructor of the class is invalid"""

    def __init__(self, message: str, possible=None, reason: str = ""):
        super.__init__(super(str, message))
        self.message = message
        self.possible = possible
        self.reason = reason

    def __str__(self):
        return self.message

    def __repr__(self):
        return {
            'error': InvalidSettings,
            'message': self.message,
            'possible': self.possible,
            'reason': self.reason
        }


class UnmatchedElements(Exception):
    """There are unmatched attributes / properties between objects"""

    def __init__(self, message: str, unmatched=None, reason: str = None):
        super.__init__(super(str, message))
        self.message = message
        self.unmatched == unmatched
        self.reason == reason

        def __str__(self):
            return self.message

        def __repr__(self):
            return {
                'error': UnmatchedElements,
                'message': self.message,
                'unmatched': self.unmatched,
                'reason': self.reason
            }


class Column:
    def __init__(self, table, name):
        """\
        create a new column (initialize)\n
        arg1: name.  Name of the new column.\n
        return: column location\
        """
        table.data[name] = list()
        table.colMaxLen.append(len(name))
        self.name = name
        self.location = len(table.colMaxLen) - 1
        self.table = table

    def rename(self, newname):
        """
        rename the column (and move to end)
        arg1: newname.
        return: old name
        """
        oldname = self.name
        self.table.data[newname] = self.table.data[self.name]
        del self.table.data[self.name]
        self.name = newname
        self.location = len(self.table.colMaxLen) - 1
        return self if self.table.settings['exp'] else oldname

    def delete(self):
        """
        delete the column
        no arguments
        """
        del self.table.data[self.name]
        return self if self.table.settings['exp'] else 1

    def move_to_end(self):
        """
        move a column
        no arguments
        """
        self.table.data[self.name] = self.table.data.pop(self.name)
        self.location = len(self.table.colMaxLen) - 1
        return self if self.table.settings['exp'] else 1


class CustomTable:
    def __repr__(self) -> dict:
        return self.data

    def __str__(self) -> str:
        return 'CustomTable'

    def __init__(self, style: list, data=None, colMaxLen: list = [], **kwargs):
        """\
        Initialize a table creation.
        Required arg1: style. type is list. charaters to form table.
        Optional arg1: data.  type is dict.
        Optional arg2: colMaxLen.  type is list.\
        arg 2 must be passed if you have the dict (arg1) passed.\
        """
        self._init(style, data, colMaxLen, **kwargs)

    def __cmp__(self, other) -> int:
        if self.data == other.data:
            return 0
        return len(self.data) - len(other.data)

    def __add__(self, other) -> CustomTable:
        if other.style != self.style:
            raise UnmatchedElements('Unmatch style', (other.style, self.style), 'the style between tables being added are different')
        return CustomTable(
            other.style,
            other.data.copy().update(self.data),
            other.colMaxLen.copy().update(self.colMaxLen),
            **other.settings.copy().update(self.settings)
        )

    def __sub__(self, other) -> CustomTable:
        if other.style != self.style:
            raise UnmatchedElements('Unmatch style', (other.style, self.style), 'the style between tables being added are different')
        colMaxLen = list()
        result = dict()
        other_k = other.keys()
        loop = 0
        for k, v in self.data.items():
            if k not in other_k:
                result[k] = v
                colMaxLen.append(self.colMaxLen[loop])
            loop += 1row
        return CustomTable(self.style, result, colMaxLen, **self.settings)

    def __len__(self) -> int:
        return len(self.data)

    def _init(self, style: list, data=None, colMaxLen: list = [], **kwargs):
        self.style = style
        self.data = data or dict()
        self.row = 0
        self.colMaxLen = colMaxLen
        self.settings = {"align": "left", "linespacing": 0, "exp": False, "linewrap": 100, "cellwrap": 30}
        self.settings.update(kwargs)

    def copy(self) -> CustomTable:
        return CustomTable(self.style,
                           self.data, self.colMaxLen, **self.settings)

    def new_column(self, name) -> Column:
        return Column(self, name)

    def insert(self, *values) -> any:
        """
        insert a row.
        arg1: values. The value for the row.
        return: the longest length of columns (list)
        """
        self.row += 1
        loopCount = 0  # for the index loop of the list
        for column in self.data:  # column is the key
            self.data[column].append(str(values[loopCount]))
            self.colMaxLen[loopCount] = max(
                self.colMaxLen[loopCount],
                len(str(values[loopCount])),
                len(column)
            )
            loopCount += 1
        if self.settings['exp']:
            return self
        return self.colMaxLen

    def remove(self, index) -> any:
        """
        remove a row.
        arg1: index. count from 0. rowNum.
        return: removed items / values
        """
        result = list()
        self.row -= 1
        loopCount = 0
        for column in self.data:
            result.append(self.data[column].pop(index))
            self.colMaxLen[loopCount] = max(self.data[column])
            loopCount += 1
        if self.settings['exp']:
            return self
        return result

    def get(self, rq=0) -> str:
        """Return back the table in string.  No arguments."""
        return self._get(rq)

    def _get_l(self, style12, result, rowNum=-1) -> str:
        if self.settings['linespacing'] != 0:
            for i in range(self.settings['linespacing']):
                colNum = 0
                for column in self.data:
                    if rowNum != -1:
                        column = self.data[column][rowNum]
                    result += f'{style12} {" " * self.colMaxLen[colNum]} '
                    colNum += 1
                result += style12 + '\n'
        colNum = 0
        if self.settings['align'] == 'left':
            for column in self.data:
                if rowNum != -1:
                    column = self.data[column][rowNum]
                result += f'{style12} {column} '
                neededSpaces = self.colMaxLen[colNum] - len(column)  # the column string subtract from needed full length
                result += ' ' * neededSpaces
                colNum += 1
        elif self.settings['align'] == 'center':
            for column in self.data:
                if rowNum != -1:
                    column = self.data[column][rowNum]
                neededSpaces = self.colMaxLen[colNum] - len(column)
                result += f'{style12} {" " * int(neededSpaces / 2)}{column}{" " * int(neededSpaces / 2)} '
                if neededSpaces / 2 % 1:
                    result += ' '
                colNum += 1
        elif self.settings['align'] == 'right':
            for column in self.data:
                if rowNum != -1:
                    column = self.data[column][rowNum]
                neededSpaces = self.colMaxLen[colNum] - len(column)
                result += f'{style12} ' + ' ' * neededSpaces + f'{column} '
                colNum += 1
        else:
            raise InvalidSettings("Invalid align settings passed", ['left', 'right', 'center'], f"'{self.settings['align']}' is not a valid align setting.")
        result += style12 + '\n'
        if self.settings['linespacing'] != 0:
            for i in range(self.settings['linespacing']):
                colNum = 0
                for column in self.data:
                    if rowNum != -1:
                        column = self.data[column][rowNum]
                    result += f'{style12} ' + ' ' * self.colMaxLen[colNum] + ' '
                    colNum += 1
                result += style12 + '\n'
        return result

    def _get(self, rq) -> str:
        rq = rq or self.row
        result = self.style[0]  # top line
        colNum = 0
        for column in self.data:  # pylint: disable=unused-variable
            result += self.style[1] * (self.colMaxLen[colNum] + 2)
            result += self.style[3]
            colNum += 1
        result = result[:-1]
        result += self.style[2] + '\n'
        # 2nd line loop
        result = self._get_l(self.style[12], result)
        # every row and every top bar
        i = 0
        for rowNum in range(self.row):
            result += self.style[4]
            colNum = 0
            # the top bar
            for column in self.data:
                result += self.style[5] * (self.colMaxLen[colNum] + 2)
                result += self.style[7]
                colNum += 1
            result = result[:-1]
            result += self.style[6] + '\n'
            # the value
            result = self._get_l(self.style[12], result, rowNum)
            i += 1
            if i >= rq:
                break
        # finish the bottom of the table
        result += self.style[8]
        colNum = 0
        for column in self.data:
            result += self.style[9] * (self.colMaxLen[colNum] + 2)
            result += self.style[11]
            colNum += 1
        result = result[:-1]
        result += self.style[10] + '\n'
        return result

    def show(self, rq=0) -> CustomTable:
        print(self.get(rq))
        if self.settings['exp']:
            return self


class ModernTable(CustomTable):
    def __str___(self) -> str:
        return 'ModernTable'

    def __init__(self, data=None, colMaxLen: list = [], **kwargs):
        """\
        Initialize a Modern Table creation.\
        """
        self._init(['╔', '═', '╗', '╦', '╠', '═', '╣', '╬', '╚', '═', '╝', '╩', '║'], data, colMaxLen, **kwargs)


class ClassicTable(CustomTable):
    def __str__(self) -> str:
        return 'ClassicTable'

    def __init__(self, data=None, colMaxLen: list = [], **kwargs):
        """\
        Initialize a classic table creation, which is formed with + | and -.\
        """
        self._init(['+', '-', '+', '+', '+', '-', '+', '+', '+', '-', '+', '+', '|'], data, colMaxLen, **kwargs)


class OnelineTable(CustomTable):
    def __str__(self) -> str:
        return 'OnelineTable'

    def __init__(self, data=None, colMaxLen: list = [], **kwargs):
        """\
        Initialize a modern table creation, but have one border instead of double borders.\
        """
        self._init(['┌', '─', '┐', '┬', '├', '─', '┤', '┼', '└', '─', '┘', '┴', '│'], data, colMaxLen, **kwargs)


lib_info = """\
pyTableMaker by windowsboy111
Check out the repo:    https://github.copm/windowsboy111/pyTableMaker/
Here's the website:    https://windowsboy111.github.io/pyTableMaker/
By using this library, you agree the terms in both the website and README.md
Thanks for choosing this library! Remember to share it too!\
"""

if __name__ == "__main__":
    print(lib_info)
