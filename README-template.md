## Install

This theme requires:

* Python >= 3.4
* NtDocutils >= 1.0.0 (auto installed)

```shell-session
# pip install ntdocutils-theme-{{ Name }}
```

## Usage

Basically, you have to do two things:

1\. Create a `.rst` file:

`example.rst`:

```rest
==========
My Article
==========

:Author: Vultur Gryphus
:Contact: info@vultur.org.ve

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip
ex ea commodo consequat. Duis aute irure dolor in reprehenderit in
voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur
sint occaecat cupidatat non proident, sunt in culpa qui officia
deserunt mollit anim id est laborum.
```

2\. Process your file:

```shell-session
$ ntdocutils -T {{ Name }} example.rst example.html
```

And that's it, you already have a HTML file.

[![screenshot](http://via.placeholder.com/500x475)](https://placeholder.com)

## Uninstall

```shell-session
# pip uninstall -y ntdocutils-theme-{{ Name }}
```

