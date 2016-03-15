#!/usr/bin/env python
# encoding: utf-8
"""
Installation for command-line ADS Paste

Run::

    python setup.py install

and the binary adspaste will be installed into your path.

To build the "Copy BibTeX info" service, run::

    python setup.py service
"""

import os
import re
import logging
from xml.etree import ElementTree
from setuptools import setup, Command

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def read(fname):
    return open(rel_path(fname)).read()


def rel_path(path):
    return os.path.join(os.path.dirname(__file__), path)


def get_version():
    with open(rel_path("adspaste.py")) as f:
        for line in f:
            if line.startswith("VERSION"):
                version = re.findall(r'\"(.+?)\"', line)[0]
                return version
    return "0.0.0.dev"


class BuildService(Command):
    """Setuptools Command to build the Service and App.
    
    This replaces the build.py script.
    """
    description = "build Copy BibTeX info.service(.app)"
    user_options = []

    def initialize_options(self):
        """Init options"""
        pass

    def finalize_options(self):
        """Finalize options"""
        pass

    def run(self):
        """Runner"""
        service_path = rel_path(os.path.join("build",
            "Copy BibTeX info.workflow", "Contents", "document.wflow"))
        app_path = rel_path(os.path.join("build", "Copy BibTeX info.app",
            "Contents", "document.wflow"))
        py_path = rel_path("adspaste.py")

        for workflow in (service_path, app_path):
            xml = ElementTree.fromstring(open(workflow).read())
            for arr in xml.find('dict').find('array').getchildren():

                # fetch Python code inside the xml
                py = [c for c in arr.find('dict').getchildren()
                    if c.tag == 'dict' and
                    any([i.text and '/usr/bin/env' in i.text
                        for i in c.getchildren()])]

                # rewrite with current file
                if py:
                    logger.info("Inserting {0} into {1}".format(py_path,
                        workflow))
                    py[0].find('string').text = open(py_path).read()

            logger.info("Saving {0}".format(workflow))
            open(workflow, 'w').write(ElementTree.tostring(xml))
        logger.info("Completed Copy BibTeX info build step")


setup(
    name='adspaste',
    version=get_version(),
    author='Jonathan Sick, Rodrigo Nemmen',
    author_email='rsnemmen@gmail.com',
    url="http://www.jonathansick.ca/adsbibdesk/",
    description="Add papers from arxiv.org or NASA/SAO ADS to your clipboard",
    long_description=read('README.md'),
    keywords="bibtex astronomy",
    classifiers=["Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: MacOS :: MacOS X",
        "Topic :: Scientific/Engineering :: Astronomy"],
    py_modules=['adspaste'],
    entry_points={'console_scripts': ['adspaste = adspaste:main']},
    cmdclass={'service': BuildService}
)
