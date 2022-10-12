# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

import logging
import pathlib
import sys
import re


sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
sys.path.append(str(pathlib.Path("./extensions")))

extensions = [
    "builder",
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinxcontrib_trio",
    "details",
    "exception_hierarchy",
    "attributetable",
    "resourcelinks",
]

autodoc_member_order = "bysource"
autodoc_typehints = "none"

extlinks = {
    "issue": ("https://github.com/SomeHybrid/pyxkcd/issues/%s", "Issue #%s"),
    "repository": ("https://github.com/SomeHybrid/pyxkcd", "repository"),
}

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

project = "pyxkcd"
copyright = "2022, SomeHybrid"
author = "SomeHybrid"

version = ""
with open("../xkcd/__init__.py") as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE
    ).group(1)

release = version

branch = "master" if version.endswith("a") else "v" + version

language = "en"

gettext_compact = False

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

pygments_style = "friendly"


def _i18n_warning_filter(record: logging.LogRecord) -> bool:
    return not record.msg.startswith(
        (
            "inconsistent references in translated message",
            "inconsistent term references in translated message",
        )
    )


_i18n_logger = logging.getLogger("sphinx")
_i18n_logger.addFilter(_i18n_warning_filter)

# -- Options for HTML output ----------------------------------------------

html_experimental_html5_writer = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "basic"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

resource_links = {
    "issues": "https://github.com/SomeHybrid/pyxkcd/issues",
    "discussions": "https://github.com/SomeHybrid/pyxkcd/discussions",
    "examples": f"https://github.com/SomeHybrid/pyxkcd/tree/{branch}/examples",
}

html_search_scorer = "_static/scorer.js"

html_js_files = ["custom.js", "settings.js", "copy.js", "sidebar.js"]

# Output file base name for HTML help builder.
htmlhelp_basename = "pyxkcddoc"

man_pages = [("index", "pyxkcd", "pyxkcd Documentation", ["SomeHybrid"], 1)]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        "index",
        "pyxkcd",
        "pyxkcd Documentation",
        "SomeHybrid",
        "pyxkcd",
        "One line description of project.",
        "Miscellaneous",
    ),
]
