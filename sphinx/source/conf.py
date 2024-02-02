# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.insert(0, os.path.abspath('../../src'))

project = 'Sphinx Documentation'
copyright = '2024, lauri'
author = 'lauri'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo'

]


templates_path = ['_templates']
exclude_patterns = []

html_logo = "assets/moilapp.png"
html_theme_options = {'logo_only': True, 'display_version': False,}

html_show_sourcelink = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

latex_elements = {'extraclassoptions': 'openany, oneside',
                  'papersize': 'a4paper',}
latex_font_size = '12pt, oneside'
latex_logo = 'assets/moilapp.png'