# coding: utf-8
# flake8: noqa
from os.path import join

from ._version import __version__
from ._version import __version_info__


# Jupyter Extension points
def _jupyter_nbextension_paths():
    return [
        dict(
            section="notebook",
            src=join("static", "cell-tools"),
            dest="cell-tools",
            require="cell-tools/main"
        ),
        dict(
            section="notebook",
            src=join("static", "document-tools"),
            dest="document-tools",
            require="document-tools/main"
        ),
        dict(
            section="notebook",
            src=join("static", "publish"),
            dest="publish",
            require="publish/main"
        ),
        dict(
            section="notebook",
            src=join("static", "spell-check"),
            dest="spell-check",
            require="spell-check/main"
        ),
        dict(
            section="notebook",
            src=join("static", "submit"),
            dest="submit",
            require="submit/main"
        ),
    ]
