# Changelog of pyTableMaker
    windowsboy111

## [Unreleased]
### Added
- readme added run on repl.it badge.
- changelog check changes section
### Removed
- `dict()` has been replaced.

## [1.2.0] - 2020-05-03
### Added
- changelog which is what you are looking at rn.
- new type of table: `customTable` that allows user / programmer to define what characters the table can be made of.
- now kwargs can be passed to the constructor of the table class for different settings. If an invalid setting is passed, `invalidSettings` expection will be raised.
- new setting: `align` that specify how text in cells should align such as left, right and center.
- new setting: `linespacing` that specify how many lines cells should add. default is 0. (not recommened as it is ugly unless you need some breathing space)
- new setting: `exp` aka express mode. When set to `True`, methods can stack up each other.
- new method in class `column`: `getTable()` which returns the pointer of the parent class.
- new method: `show()` which is an alias of `print(t.get())`
- new global variable in library: `lib-info` that stores info about the library.
- added file: table_test.py to test the library.
### Changed
- the instance variable `obj` in class `column` has been renamed to `table` to make it more clear that it stores the `self` pointer of its parent class.
- updated `example.py` as expected to show new features.
- `customTable` is now the parent of all table classes.
- Running `table.py` directly (i.e. `python3 table.py`) will print `lib-info` instead of doing nothing.
- Reorganized the code, making `get()` less clutter / simplified the code so that it no longer violates the ultimate DRY rule:
> - `__init__()` ==> `_init()` and `__init__()`              (Not recommened to call them directly)
> - `get()`      ==> `_get()`, `_get_l()` and `get()`        (Not recommened to call `_get()` and `_get_l()` directly)
### Fixed
- no more warnings when using the library, `dummy_func()` has been added to prevent unused variable warnings.
### Deprecated
- soon in a future update, `OrderedDict()` will be replaced with normal standard `dict()`. (Backwards compatible warning!)


## [1.1.0] - 2020-04-13
### Added
- new type of table: `onelineTable`, similar to `modernTable`, but have only one border instead of double borders.

## [1.0.0] - 2020-04-10
### Added
- new type of table: `classicTable` that is formed with +, -, and |.
- Columns can now be renamed with `column.rename(newName)`.
- Columns can now be moved to the end with `column.moveToEnd()`.
- Columns can now be deleted with `column.delete(newName)`.
### Changed
- the original table type now has been renamed to `modernTable`.
- Columns needs to be added with `table.new_column(columnName)` instead of method `add_column()`.
- `new_column()` now returns an column object instead of nothing.
### Fixed
- `OrderedDict` has been used to store data instead of `dict`. This is being considered as a bug because before python 3.7, the standard `dict` type does NOT maintain insertion order by default.

## [0.1.0] - 2020-04-09
### Added
- example for the library.
- a basic table class.

[Unreleased]: https://github.com/windowsboy111/pyTableMaker/compare/v1.2.0...HEAD
[1.2.0]: https://github.com/windowsboy111/pyTableMaker/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/windowsboy111/pyTableMaker/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/windowsboy111/pyTableMaker/compare/v0.1.0...v1.0.0
[0.1.0]: https://github.com/windowsboy111/pyTableMaker/releases/tag/v0.1.0
