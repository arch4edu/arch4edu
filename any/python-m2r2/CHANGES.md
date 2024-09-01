### Version 0.3.3 (2022-08-11)
* Drop support for all python versions prior to 3.7
* Upgrade to docutils 0.19

### Version 0.3.2 (2021-12-10)
* Pin mistune version

### Version 0.3.1 (2021-07-13)
* Fix argparse for python3.10

### Version 0.3.0 (2021-07-12)
* Add support for mermaid code
* Change bump for bump2version

### Version 0.3.0 (2021-07-12)
* Add support for mermaid code
* Change bump for bump2version

### Version 0.2.8 (2021-06-23)
* Fix bug that made multiple inline mathematical expressions fail to render

### Version 0.2.7 (2020-11-20)
* Add official python3.9 support
* Fix classifiers

### Version 0.2.6 (2020-11-19)
* Fix error for Sphinx3.3.0

### Version 0.2.5 (2020-07-13)
* Update repo name in every reference

### Version 0.2.4 (2020-07-12)
* Central versioning
* Add bump

### Version 0.2.3 (2020-07-09)
* Fix https://github.com/miyakogi/m2r/issues/51
* Change `tox` for `nox`
* Add `pre-commit` hooks and fix styling

### Version 0.2.1 (2018-10-12)

* Add `--disable-inline-math` and `m2r_disable_inline_math` sphinx option

## Version 0.2.0 (2018-08-13)

* Add `start-line` and `end-line` option to `mdinclude` directive
* Add `anonymous_references` option ([#26](https://github.com/miyakogi/m2r/pull/26))

### Version 0.1.15 (2018-06-30)

* Support Sphinx's doc/ref directives for relative links ([#16](https://github.com/miyakogi/m2r/pull/16))

### Version 0.1.14 (2018-03-22)

* Implement markdown link with title

### Version 0.1.13 (2018-02-14)

* Catch up sphinx updates

### Version 0.1.12 (2017-09-11)

* Support multi byte characters for heading

### Version 0.1.11 (2017-08-30)

* Add metadata for sphinx
* Add `convert(src)` function, which is shortcut of `m2r.M2R()(src)`

### Version 0.1.10 (2017-08-15)

* Include CHANGES and test files in source distribution

### Version 0.1.9 (2017-08-12)

* Print help when input_file is not specified on command-line

### Version 0.1.8 (2017-08-11)

* Update metadata on setup.py

### Version 0.1.7 (2017-07-20)

* Fix undefined name error (PR #5).

### Version 0.1.6 (2017-05-31)

* Drop python 3.3 support
* Improve image_link regex (PR #3)

### Version 0.1.5 (2016-06-21)

* Support multiple backticks in inline code, like: ```backticks (``) in code```

### Version 0.1.4 (2016-06-08)

* Support indented directives/reST-comments
* Support role-name after backticks (`` `text`:role: style``)

### Version 0.1.3 (2016-06-02)

* Remove extra escaped-spaces ('\ ')
    * before and after normal spaces
    * at the beginning of lines
    * before dots

### Version 0.1.2 (2016-06-01)

* Add reST's `::` marker support
* Add options to disable emphasis by underscore (`_` or `__`)

### Version 0.1.1 (2016-05-30)

* Fix Bug: when code or link is placed at the end of line, spaces to the next word is disappeared

## Version 0.1 (2016-05-30)

First public release.
