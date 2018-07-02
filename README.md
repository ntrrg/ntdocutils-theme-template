## Usage

Download the template.

```shell-session
$ wget -c 'https://github.com/ntrrg/ntdocutils-theme-template/archive/master.tar.gz'
```

```shell-session
$ tar -xvf ntdocutils-theme-template-master.tar.gz
```

```shell-session
$ rm ntdocutils-theme-template-master.tar.gz
```

Set you prefences.

```shell-session
$ mv ntdocutils-theme-template-master REPOSITORY_NAME
```

```shell-session
$ cd REPOSITORY_NAME
```

```shell-session
$ EDITOR config.sh
```

```shell-session
$ ./setup.sh
```

```shell-session
# pip install -e .
```

Edit and test your theme, check the [MDL theme](https://github.com/ntrrg/ntdocutils-theme-mdl/)
code and use it as example.

When it is ready to be released, create the Python module and then publish it
in the PyPI.

```shell-session
# pip install setuptools twine
```

```shell-session
$ python setup.py sdist bdist_well
```

```shell-session
$ twine upload dist/*
```

## Acknowledgment

Working on this project I use/used:

* [Debian](https://www.debian.org/)

* [XFCE](https://xfce.org/)

* [Chrome](https://www.google.com/chrome/browser/desktop/index.html)

* [Zsh](http://www.zsh.org/)

* [Git](https://git-scm.com/)

* [EditorConfig](http://editorconfig.org/)

* [Github](https://github.com)

* [st](https://st.suckless.org/)

* [Vim](https://www.vim.org/)

* [Gogs](https://gogs.io/)

