### Hexlet tests and linter status:

[![Actions Status](https://github.com/Andradit/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Andradit/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/70452ee57eaddb8925a1/maintainability)](https://codeclimate.com/github/Andradit/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/70452ee57eaddb8925a1/test_coverage)](https://codeclimate.com/github/Andradit/python-project-50/test_coverage)

# A program to display the differences between two data structures

This program compares the two configuration files and shows the difference. Such a mechanism is used, for example, 
when outputting tests or when automatically tracking changes in configuration files.

### Utility features:

Support for various data structures:
- **yaml**
- **json**

Generate reports in the following formats::
- **plain text**
- **stylish** (default output)
- **json**

### Example of use:

    gendiff --format plain filepath1.json filepath2.yml
    
    Setting "common.setting4" was added with value: False
    Setting "group1.baz" was updated. From 'bas' to 'bars'
    Section "group2" was removed


## Installation

> ```diff
> + Please report issues if you try to install and run into problems!
> ```

Make sure you are running at least Python 3.11

Clone the repository and install manually:

```bash
$ git clone git@github.com:Andradit/python-project-50.git
$ cd python-project-50/
$ make install
$ make build
$ make package-install
```
## Starting program execution

To display help, enter the command:

```bash    
$ gendiff -h
```

[![asciicast](https://asciinema.org/a/VAVOkeTXeMxoebFYqqIB732IT.svg)](https://asciinema.org/a/VAVOkeTXeMxoebFYqqIB732IT)

## Starting comparing two files of the same type
To run it, enter the following command, selecting the json or yaml format

```bash    
$ gendiff file1.json file2.json
```
or
```bash    
$ gendiff file1.yaml file2.yaml
```
# ASCINEMA

## Starting comparison of two files of different types
To run it, enter the following command, selecting the json and yaml formats
```bash    
$ gendiff file1.json file3.yaml
```
or
```bash    
$ gendiff file2.yaml file4.json
```
# ASCINEMA

## Possible Improvements

- Color support.
- Adding types of files to be compared
- Creating new output formats
- *Your* creative idea.

If you encounter any problem or have any suggestions, please [open an issue](https://github.com/Andradit/python-project-50/issues/new) or [send a PR](https://github.com/Andradit/python-project-50/compare).

