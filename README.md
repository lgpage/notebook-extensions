# Notebook-extensions

This repository contains several Javascript extensions for Jupyter:
* Cell tools: Two column and tabbed modes for input/output of notebook cells
* Document tools:
 * Sections: Move whole sections up and down, number sections.
 * Create table of contents (TOC) and create references/citations
* Spell check: spell check for markdown cells

Student interaction:
* Publish: your notebook, by copying it to a certain directory
* Submit: copies notebook to instructor

These extensions where once part of the [Calico project](http://calicoproject.org/).


Install
-------

### `pip`

Install into --system, --sys-prefix, or --user (here, dollar-sign
represents the shell prompt):

```shell
$ pip install calysto
$ jupyter nbextension install --user --py calysto
$ jupyter nbextension enable --user --py calysto
```

To check their status:

```shell
$ jupyter nbextension list
```

When you now open or reload a notebook, it should load the extensions.


Develop
-------

First download this collection and cd into the folder:

```shell
$ wget https://github.com/Calysto/notebook-extensions/archive/master.zip
$ unzip master.zip
$ cd notebook-extensions-master
OR:
$ git clone https://github.com/Calysto/notebook-extensions.git
$ cd notebook-extensions
```

Next, install them into --system, --sys-prefix, or --user:

```shell
$ python setup.py develop
$ jupyter nbextension install --overwrite --symlink --sys-prefix --py calysto
$ jupyter nbextension enable --sys-prefix --py calysto
```

Disable extensions
------------------

By defaut all extensions are enabled. If you wish to disable any of them you
want:

```shell
$ jupyter nbextension disable cell-tools/main
$ jupyter nbextension disable document-tools/main
$ jupyter nbextension disable spell-check/main
$ jupyter nbextension disable publish/main
$ jupyter nbextension disable submit/main
```
