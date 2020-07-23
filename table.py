import utils


DEFAULT_SETTINGS = {
    "align":        "left",
    "linespacing":  0,
    "exp":          False,
    "cellwrap":     40
}


class invalidSettings(Exception):
    """The settings passed via kwargs from the constructor of the class is invalid"""

    def __init__(self, message, possible=None, reason=""):
        super.__init__(super(str, message))
        self.message = message
        self.possible = possible
        self.reason = reason

    def __str__(self):
        return self.message

    def __repr__(self):
        return {'error': invalidSettings, 'message': self.message, 'possible': self.possible, 'reason': self.reason}


class customTable:
    def __repr__(self):
        return str(self.data)

    def __str___(self):
        return 'customTable'

    def __init__(self, style: list, data=None, colMaxLen: list = [], **kwargs):
        """\
        Initialize a table creation.\n
        Required arg1: style. type is list. charaters to form table.\n
        Optional arg1: data.  type is dict.\n
        Optional arg2: colMaxLen.  type is list.  Must be passed if you have the dict (arg1) passed.\
        """
        self._init(style, data, colMaxLen, **kwargs)

    def _init(self, style: list, data=None, colMaxLen: list = [], **kwargs):
        self.style = style
        self.data = data or dict()
        self.row = 0
        self.colMaxLen = colMaxLen
        self.settings = DEFAULT_SETTINGS.copy()
        self.settings.update(kwargs)

    def copy(self):
        return customTable(self.style, self.data, self.colMaxLen, **self.settings)

    def new_column(self, name):
        class column:
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
                rowdata = self.table.data[self.name]
                del self.table.data[self.name]
                self.table.data[newname] = rowdata
                self.name = newname
                self.location = len(self.table.colMaxLen) - 1
                if self.table.settings['exp']:
                    return self
                return oldname

            def delete(self):
                """
                delete the column
                no arguments
                """
                del self.table.data[self.name]
                if self.table.settings['exp']:
                    return self

            def move_to_end(self):
                """
                move a column
                no arguments
                """
                self.table.data[self.name] = self.table.data.pop(self.name)
                self.location = len(self.table.colMaxLen) - 1
                if self.table.settings['exp']:
                    return self

            def get_table(self):
                return self.table
        return column(self, name)

    def insert(self, *values):
        """
        insert a row.
        arg1: values. The value for the row.
        return: the longest length of columns (list)
        """
        self.row += 1
        # for the index loop of the list
        loopCount = 0
        # column is the key
        for column in self.data:
            self.data[column].append(str(values[loopCount]))
            self.colMaxLen[loopCount] = max(self.colMaxLen[loopCount],
                                            len(str(values[loopCount])))
            loopCount += 1
        if self.settings['exp']:
            return self
        return self.colMaxLen

    def remove(self, index):
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

    def get(self, rq=0):
        """Return back the table in string.  No arguments."""
        return self._get(rq)

    def _add_linespacing(self, s12):
        result = ''
        for i in range(self.settings['linespacing']):
            for colNum in range(len(self.data)):
                result += f'{s12} ' + ' ' * \
                    (self.colMaxLen[colNum] if self.colMaxLen[colNum] <= (self.settings['cellwrap'] - 2) else (self.settings['cellwrap'] - 2)) + ' '
            result += s12 + '\n'
        return result

    def _get_l(self, s12, rowNum=-1):
        result = self._add_linespacing(s12)

        colNum = 0  # get loop count ready
        next = list()  # storing next line to be placed if cell / line wrapping is needed
        maxLen = self.settings['cellwrap'] - 2
        for k, v in self.data.items():
            name = k if rowNum == -1 else v[rowNum]
            if len(name) > maxLen:
                next.append(name[maxLen:])
                name = name[:maxLen]
            else:
                next.append('')
            neededSpaces = (
                self.colMaxLen[colNum] if self.colMaxLen[colNum] <= maxLen else maxLen) - len(name)
            result += f'{s12} {name} ' + ' ' * neededSpaces
        result = result[:-1] + ' ' + s12 + '\n'
        while any(next):
            loop = 0
            theNext = list()
            for name in next:
                if len(name) > maxLen:
                    theNext.append(name[maxLen:])
                    name = name[:maxLen]
                else:
                    theNext.append('')
                neededSpaces = (
                    self.colMaxLen[colNum] if self.colMaxLen[colNum] <= maxLen else maxLen) - len(name)
                result += f'{s12} {name} ' + ' ' * neededSpaces
                loop += 1
            result = result[:-1] + ' ' + s12 + '\n'
            if theNext == ['' for col in self.data]:
                break
            next = theNext.copy()

        result += self._add_linespacing(s12)
        return result

    def _get_struct(self, styleLeft, styleMid, styleCross, styleRight, colNum):
        result = styleLeft
        for column in self.data:
            result += styleMid * ((self.colMaxLen[colNum] + 2) if (
                self.colMaxLen[colNum] + 2) < self.settings['cellwrap'] else self.settings['cellwrap'])
            result += styleCross
            colNum += 1
        return result[:-1] + styleRight + '\n'

    def _get(self, rq):
        rq = rq or self.row
        colNum = 0
        result = self._get_struct(self.style[0], self.style[1], self.style[3], self.style[2], colNum)  # get line 1
        # 2nd line loop
        result += self._get_l(self.style[12])
        # every row and every top bar
        i = 0
        for rowNum in range(self.row):
            colNum = 0
            # the top bar
            result += self._get_struct(self.style[4], self.style[5], self.style[7], self.style[6], colNum)
            # the value
            result += self._get_l(self.style[12], rowNum)
            i += 1
            if i >= rq:
                break
        # finish the bottom of the table
        colNum = 0
        result += self._get_struct(self.style[8], self.style[9], self.style[11], self.style[10], colNum)
        return result

    def show(self, rq=0):
        print(self.get(rq))
        if self.settings['exp']:
            return self


class modernTable(customTable):
    def __str___(self):
        return 'modernTable'

    def __init__(self, data=None, colMaxLen: list = [], **kwargs):
        """\
        Initialize a Modern Table creation.\
        """
        self._init(['╔', '═', '╗', '╦', '╠', '═', '╣', '╬', '╚',
                    '═', '╝', '╩', '║'], data, colMaxLen, **kwargs)

    def get(self, rq=0):
        return self._get(rq)


class classicTable(customTable):
    def __str__(self):
        return 'classicTable'

    def __init__(self, data=None, colMaxLen: list = [], **kwargs):
        """\
        Initialize a classic table creation, which is formed with + | and -.\
        """
        self._init(['+', '-', '+', '+', '+', '-', '+', '+', '+',
                    '-', '+', '+', '|'], data, colMaxLen, **kwargs)

    def get(self, rq=0):
        """Return back the table in string.  No arguments."""
        return self._get(rq)


class onelineTable(customTable):
    def __str__(self):
        return 'onelineTable'

    def __init__(self, data=None, colMaxLen: list = [], **kwargs):
        """\
        Initialize a modern table creation, but have one border instead of double borders.\
        """
        self._init(['┌', '─', '┐', '┬', '├', '─', '┤', '┼', '└',
                    '─', '┘', '┴', '│'], data, colMaxLen, **kwargs)

    def get(self, rq=0):
        return self._get(rq)


lib_info = """\
pyTableMaker by windowsboy111
Check out the repo:    https://github.copm/windowsboy111/pyTableMaker/
Here's the website:    https://windowsboy111.github.io/pyTableMaker/
By using this library, you agree the terms in both the website and README.md
Thanks for choosing this library! Remember to share it too!\
"""

if __name__ == "__main__":
    print(lib_info)
