ADS Paste
==============

This is a command line tool for retrieving the bibtex info of an astronomical journal article published on [ADS](http://adsabs.harvard.edu) or [arXiv](http://arxiv.org/archive/astro-ph) and copying it to your clipboard. You can then add the citation to your favorite  bibtex database manager (e.g., [jabref](http://www.jabref.org), [bibdesk](http://bibdesk.sourceforge.net), [papers](http://www.papersapp.com), [mendeley](https://www.mendeley.com/newsfeed/)).

This tool is based on [ADS to Bibdesk](https://github.com/jonathansick/ads_bibdesk). The reason why I adapted it is because the original code worked only with the [bibdesk](http://bibdesk.sourceforge.net) program. However, bibdesk as of early 2016 is quite buggy and has not been supported in a while.


# Command Line Quickstart

adspaste can be called in the following ways:

#### 1. Using the ADS code

    adspaste 1998ApJ...500..525S
    
#### 2. Using the DOI

    adspaste 10.1093/mnras/stv260

#### 3. Using the arXiv code

    adspaste 1411.4682

The complete BibTeX info will then be available in the clipboard, for example:

```
@ARTICLE{2015MNRAS.449..316N,doi={10.1093/mnras/stv260},title="{On the efficiency of jet production in radio galaxies}",arxivurl="http://arxiv.org/abs/1406.7420",journal={\mnras},author={{Nemmen}, R.~S. and {Tchekhovskoy}, A.},adsnote={Provided by the SAO/NASA Astrophysics Data System},abstract="The mechanisms that produce and power relativistic jets are fundamental open questions in black hole (BH) astrophysics. In order to constrain these mechanisms, we analyse the energy efficiency of jet production eta based on archival Chandra observations of 27 nearby, low-luminosity active galactic nuclei. We obtain eta as the ratio of the jet power, inferred from the energetics of jet powered X-ray emitting cavities, to the BH mass accretion rate dot{M}_BH. The standard assumption in estimating dot{M}_BH is that all the gas from the Bondi radius rB makes it down to the BH. It is now clear, however, that only a small fraction of the gas reaches the hole. To account for this effect, we use the standard disc mass-loss scaling, dot{M}(r) ∝ (r/r_B)^s dot{M}_Bondi. This leads to much lower values of dot{M}_BH and higher values of eta than in previous studies. If hot accretion flows are characterized by 0.5 <= s <= 0.6 - on the lower end of recent theoretical and observational studies - then dynamically important magnetic fields near rapidly spinning BHs are necessary to account for the high eta ≈ 100-300 per cent in the sample. Moreover, values of s > 0.6 are essentially ruled out, or there would be insufficient energy to power the jets. We discuss the implications of our results for the distribution of massive BH spins and the possible impact of a significant extra cold gas supply on our estimates.",month=may,volume=449,eprint={1406.7420},primaryClass="astro-ph.HE",year=2015,keywords={accretion, accretion discs, black hole physics, galaxies: active, galaxies: jets, X-rays: galaxies},archivePrefix="arXiv",pages={316-327},adsurl={http://adsabs.harvard.edu/abs/2015MNRAS.449..316N}}
```

You can then paste it in your favorite bibtex database manager (e.g., [jabref](http://www.jabref.org), [bibdesk](http://bibdesk.sourceforge.net), [papers](http://www.papersapp.com), [mendeley](https://www.mendeley.com/newsfeed/)).

A full summary of adspaste commands is available via

    adspaste --help

# Summary of article tokens

* The URL of an ADS or arXiv article page,
* The ADS bibcode of an article (e.g. `1998ApJ...500..525S`),
* The arXiv identifier of an article (e.g. `0911.4956`), or
* An article DOI.


# Installation

The command line script can be installed via

    python setup.py install

and the binary adsbibdesk will be installed into your path. You may need to run the last command with `sudo`.

If you want to be able to right click on a reference and run the script on the selection from OS X, run

    python setup.py service

to build the service.

# TODO

* Update the automator service for OS X, such that you can right click to add references with Mac
* Graphical interface with simple text input for pasting the article token and pressing enter/clicking, copying the bibtex entry to the clipboard
* Remove other options and unnecessary code previously available in adsbibdesk which are not needed anymore


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
