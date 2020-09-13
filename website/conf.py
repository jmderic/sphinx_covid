# -*- coding: utf-8 -*-

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
import os
import sys
#sys.path.insert(0, os.path.abspath('.'))
sys.path.append(os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Covid Analytics'
copyright = '2020, J. Mark Deric'
author = 'J. Mark Deric'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'jinja'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['Thumbs.db', '.DS_Store']

# JMD General configuration additions
# https://stackoverflow.com/questions/43760158/disable-syntax-highlight-in-sphinx-alabaster-theme
highlight_language = 'none'

# -- Update Automation Support -----------------------------------------------

import json

def get_jinja_contexts():
    with open('../jinja_contexts_autoX.json') as f:
        jinja_contexts = json.load(f)
    return jinja_contexts

def get_html_context():
    with open('../html_context_autoX.json') as f:
        html_context = json.load(f)
    return html_context

# test jinja directive
jinja_contexts = get_jinja_contexts()

# eliminate template "isn't included in any toctree" warning
exclude_patterns = ['locs/template.rst']

# -- Options for HTML output -------------------------------------------------

html_context = get_html_context()

html_extra_path = [
    'images/plot_Cases.png',
]

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# JMD HTML output additions
html_theme_options = {
#    'page_width': '1250px', # using default 940px
    'sidebar_includehidden': False,
    'fixed_sidebar' : True,
}

html_sidebars = {
    '**': [
        'about.html',
        'asof.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
        'donate.html',
    ]
}
