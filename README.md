# SPARC Python Imager (sparc-imp)

A python tool to enhance the accessibility of SPARC dataset visualisations and their analyses in accordance with FAIR principles. 

![Python 3](https://img.shields.io/badge/Python->=3.9-blue)
[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GitHub issues-closed][issues-closed-shield]][issues-url]
[![License][license-shield]][license-url]
[![Contributor Covenant][code-of-conduct-shield]](CODE_OF_CONDUCT.md)
[![PyPI version fury.io][pypi-shield]][pypi-url]
[![Conventional Commits][conventional-commits-shield]][conventional-commits-url]

[contributors-shield]: https://img.shields.io/github/contributors/SPARC-FAIR-Codeathon/sparc-imp.svg?style=flat-square
[contributors-url]: https://github.com/SPARC-FAIR-Codeathon/sparc-imp/graphs/contributors
[stars-shield]: https://img.shields.io/github/stars/SPARC-FAIR-Codeathon/sparc-imp.svg?style=flat-square
[stars-url]: https://github.com/SPARC-FAIR-Codeathon/sparc-imp//stargazers
[issues-shield]: https://img.shields.io/github/issues/SPARC-FAIR-Codeathon/sparc-imp/.svg?style=flat-square
[issues-url]: https://github.com/SPARC-FAIR-Codeathon/sparc-imp/issues
[issues-closed-shield]: https://img.shields.io/github/issues-closed/SPARC-FAIR-Codeathon/sparc-imp.svg
[issues-closed-url]: https://GitHub.com/SPARC-FAIR-Codeathon/sparc-me/issues?q=is%3Aissue+is%3Aclosed
[license-shield]: https://img.shields.io/github/license/SPARC-FAIR-Codeathon/sparc-imp.svg?style=flat-square
[license-url]: https://github.com/SPARC-FAIR-Codeathon/sparc-imp/blob/master/LICENSE
[code-of-conduct-shield]: https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg
[pypi-shield]: https://badge.fury.io/py/{sparc_imp}.svg
[pypi-url]: https://pypi.python.org/pypi/{sparc_imp}}/
[conventional-commits-shield]: https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white
[conventional-commits-url]: https://conventionalcommits.org



## Table of contents
* [About](#about)
* [Getting started](#getting-started)
* [Contributing](#contributing)
* [Reporting issues](#reporting-issues)
* [Contributors](#contributors)
* [Acknowledgements](#acknowledgements)


## About
This is the repository of team sparc-me (Team #3) of the 2024 SPARC Codeathon. Information about the 2024 SPARC Codeathon can be found [here](https://sparc.science/news-and-events/events/2024-sparc-fair-codeathon). 

No work was done on this project prior to the Codeathon. 

## Introduction
The NIH Common fund program *Stimulating Peripheral Activity to Relieve Conditions* [SPARC](https://commonfund.nih.gov/sparc) seeks to understand how electrical signals control internal organ function. In doing so it explores how therapeutic devices might modulate nerve activity to treat conditions like hypertension, heart failure, and gastrointestinal disorders. To this end, data have been compiled from 3900+ subjects across 7 species from  49 different anatomical structures.  

The SPARC Portal offers a user-friendly interface to access and share resources from the SPARC community. It features well-curated, high-impact data, SPARC projects, and computational simulations, all available under the “[Find Data](https://sparc.science/data?type=dataset)” section.
## The problem
TODO
There is no single visualisation tool O<sup>2</sup>S<sup>2</sup>PARC that can produce VTK visualisations from data scaffolds. 

This limits the ability of 
   - 
   
## Our solution: spark-imp
We have developed a python module called the SPARC Python Imager (sparc-imp) that enhancess the FAIRness of SPARC data by:
- **F**indability
  - Visualising data and metadata within SDS datasets
- **A**ccessibility
  - Accessing visualisations of curated SDS datasets and their metadata (using the Pennsieve API)
  - Accessing metadata of visualisations 
- **I**nteroperability
  - Visualisations are achieved within a portable framework that ensures reproducibility.
- **R**eusability
  - Comprehensive documentation and guided tutorials that can easily be adapted to new datasets or environments.
 

Tutorials have been provided to demonstrate how sparc-imp enhances FAIRness. 
    
## Impact
TODO

## Setting up sparc-imp
### Pre-requisites 
- [Git](https://git-scm.com/)
- Python versions:
   - 3.9
###  Installing via PyPI

Here is the [link](https://pypi.org/project/{PACKAGE_NAME}/) to our project on PyPI
```
pip install sparc_imp
```
### From source code
#### Downloading source code
Clone the sparc-imp repository from github, e.g.:
```
git clone git@github.com:SPARC-FAIR-Codeathon/TODO
```

### Installing dependencies
TODO

## Using sparc-imp
Included are guided tutorials covering some applications of sparc-imp:

TODO
## Reporting issues 
To report an issue or suggest a new feature, please use the [issues page](https://github.com/SPARC-FAIR-Codeathon/{REPO_NAME}/issues). TODO
Please check existing issues before submitting a new one.
## Contributing

To contribute: fork this repository and submit a pull request. Before submitting a pull request, please read our [Contributing Guidelines](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md). If you found this tool helpful, please add a GitHub Star to support further developments!

### Project structure
-   /sparc_imp/ - Parent directory
-   TODO

## Cite us
TODO



## Contributors
TODO
## Acknowledgements
TODO
