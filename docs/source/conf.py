# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ansible-sdk'
copyright = '2022, Ansible'
author = 'Ansible'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_ansible_theme',
    'sphinxcontrib.apidoc'
]

templates_path = ['_templates']
exclude_patterns = []

#apidoc configuration
#find more at https://pypi.org/project/sphinxcontrib-apidoc/
apidoc_module_dir = '../../ansible_sdk/'
#apidoc_excluded_paths = ['tests']
apidoc_separate_modules = True

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "ansible"
highlight_language = "YAML+Jinja"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_ansible_theme'
html_static_path = ['_static']
html_title = "Ansible SDK Documentation"