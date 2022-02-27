# Notepad

[![GitHub release](https://img.shields.io/github/v/release/Baelfire18/Notepad.svg)](../../releases/latest)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

This is a Notepad made with Python3 and [tkinter library](https://docs.python.org/es/3/library/tkinter.html).

## Release

[Download the first version][release]

## Download with git

### Get the reposiotory

```cmd
git clone https://github.com/Baelfire18/Notepad.git
cd Notepad
```

### Create a virtual enviroment (optional, recommended)

[Virtual enviroment guide][venv-guide]

In Windows:

```cmd
py -m venv env
env\Scripts\activate
```

In macOS and Linux:

```shell
python3 -m venv env
source env/bin/activate  # in bash/zsh
. env/bin/activate.fish  # in fish
```

### Dowload dependecies

```shell
pip install -r requirements.txt
```

### Use

```shell
python Notepad.py
```

### Build

```shell
pyinstaller.exe --onefile --windowed --icon='assets\favicon.ico' Notepad.py
```

## LICENSE

[MIT LICENSE](./LICENSE)

## Credits

I was inspired by this code from [code with Harry](https://www.codewithharry.com/videos/python-gui-tkinter-hindi-29).

[venv-guide]: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment
[release]: https://github.com/Baelfire18/Notepad/releases/latest/download/Notepad.zip
