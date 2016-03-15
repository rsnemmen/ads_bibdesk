ADS Paste
==============

This is a command line tool for retrieving the bibtex and abstract of an astronomical journal article published on [ADS](http://adsabs.harvard.edu) or [arXiv](http://arxiv.org/archive/astro-ph) and copying it to your clipboard. You can then add the citation to your favorite  bibtex database manager (e.g., [jabref](http://www.jabref.org), [bibdesk](http://bibdesk.sourceforge.net), [papers](http://www.papersapp.com), [mendeley](https://www.mendeley.com/newsfeed/)).

This tool is based on [ADS to Bibdesk](https://github.com/jonathansick/ads_bibdesk). The reason why I adapted it is because the original code worked only with the [bibdesk](http://bibdesk.sourceforge.net) program. However, bibdesk as of early 2016 is quite buggy and has not been supported in quite a while.


# Command Line Quickstart

ADS Paste can also be run directly from the command line.
The command line script can be installed via::

    python setup.py install

You may need to run the last command with `sudo`.

Once `adspaste` is installed, you can call it with the same types of article tokens you can launch the Service with, e.g.,::

    adspaste 1998ApJ...500..525S

A full summary of `adspaste` commands is available via::

    adspaste --help

# Summary of article tokens

* The URL of an ADS or arXiv article page,
* The ADS bibcode of an article (e.g. `1998ApJ...500..525S`),
* The arXiv identifier of an article (e.g. `0911.4956`), or
* An article DOI.




# TODO

* Graphical interface with simple text input for pasting the article token and pressing enter/clicking, copying the bibtex entry to the clipboard
* Remove other options previously available in adsbibdesk which are not needed anymore


# License

Copyright 2016 [Rodrigo Nemmen](http://rodrigonemmen.com), Jonathan Sick, Rui Pereira and Dan-Foreman Mackey.

ADS Paste is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

ADS Paste is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with ADS Paste.  If not, see <http://www.gnu.org/licenses/>.
