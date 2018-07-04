# Installation instructions

We recommend using Python 3.5 or 3.6. We recommend using the latest version of
Mayavi namely, 4.6.0. Mayavi will also work with Python 2.7 if you are
constrained to use that version. However, the following instructions are
written for 3.5 or 3.6.

Once you are done reading this and installing Mayavi, go back to the
[main instructions](./README.md).

## Requirements

[Mayavi](https://github.com/enthought/mayavi) requires numpy and
[VTK](https://www.vtk.org) to be installed. It also requires a suitable GUI
toolkit. We recommend that you install PyQt5 as that is what works best with
Mayavi under Python 3.x.

We provide specific instructions for different packaging environments below.

## Using pip

If you are not using any particular packaging environment you can easily
install Mayavi using pip. This does require that you are able to compile
extensions on your installation. This is usually the case on MacOS and Linux.

On Windows you will need to install the required compilers. Information is
available here: https://wiki.python.org/moin/WindowsCompilers and you likely
need to have Microsoft Visual C++ 14.0 standalone installed.

Given this you can install Mayavi with the following:
```
  $ pip install numpy vtk pyqt5

  $ pip install mayavi
```

We also require jupyter and scipy for the workshop so please also install the following:

```
  $ pip install scipy jupyter
```

If this works successfully, please move on to the "testing your installation" below.

## Using conda

To install Mayavi with conda try the following:

```
$ conda install -c conda-forge numpy scipy apptools envisage jupyter
$ pip install mayavi
```

On some architectures, you may be able to install the latest version of mayavi
with conda itself. You could try that and if it installs the latest version of
Mayavi and everything works, you should be all set. Otherwise, use the above
instructions.

If this works successfully, please move on to the "testing your installation"
below.


## Using edm

If you are using edm you can do the following:

```
$ edm install numpy scipy apptools envisage jupyter
$ pip install mayavi pyqt5
```

If this works successfully, please move on to the "testing your installation"
below.


## Testing your installation

Try the following:

```
$ jupyter console

In []: %gui qt
In []: from mayavi import mlab
In []: mlab.test_plot3d()
```

This should produce a window that is interactive and usable without any
tracebacks or exceptions.

## Possible issues

If you get strange warnings like this:
```
QWidgetWindow(0x7fce6d8eac30, name="_ToolBarClassWindow") ( QScreen(0x7fce6be35730, name="Color LCD") ): Attempt to set a screen on a child window.
```
when creating Mayavi plots, install pyqt5 via pip like so:

```
$ pip install pyqt5
```

Note that pyqt5 version 5.11.2 on PyPI is broken, and you should install the
previous version or perhaps a later version.  This can be done like so:

```
$ pip install pyqt5==5.10.1
```
