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
In the current landscape of data science and research, visualizing data is crucial for analysis, interpretation, and communication. However, existing tools for reconstructing visualizations from datasets are limited in their accessibility and interoperability. The primary tool available is restricted to the Windows operating system, creating significant barriers for users on other platforms such as macOS and Linux. This limitation hinders the application of the FAIR principles (Findable, Accessible, Interoperable, and Reusable) to data visualization:

### Limited Accessibility:
- Researchers and data scientists using non-Windows operating systems are unable to access the existing tool, leading to inefficiencies and potential data silos.
### Poor Interoperability:
- The existing tool may not support integration with other widely-used data analysis tools or workflows, making it difficult to share and collaborate on visualizations across different platforms and software environments.
### Challenges in Reusability:
- Without a standardized approach to creating and sharing visualizations, researchers may struggle to replicate or adapt visualizations for different datasets or research contexts.

## Our solution: spark-imp
We have developed a cross-platform Python visualisation tool called the SPARC Python Imager (sparc-imp) to run within o<sup>2</sup>S<sup>2</sup>PARC that can produce VTK visualisations from data scaffolds. This Python module enhancess the **FAIR**ness of SPARC data by:
- **F**indability
  - Enhanced Metadata: The tool can extract and attach metadata to visualizations, making it easier to locate specific datasets and their visual representations.
  - Searchability: By tagging visualizations with relevant keywords and descriptions, users can quickly find the visual data they need.
- **A**ccessibility
  - User-Friendly Interface: A well-designed tool can provide an intuitive interface for accessing and generating visualizations, lowering the barrier for users with varying levels of technical expertise.
  - Light weight: A universally implementable visualisation tool can be run within o<sup>2</sup>S<sup>2</sup>PARC while accessing visualisations of curated SDS datasets and their metadata (using the Pennsieve API).
  - Open Access: If the tool is open-source or freely available, it ensures that a wider audience can access and use it without restrictions.
- **I**nteroperability
  - Standard Formats: The tool can support and export visualizations in standardized formats (e.g., JSON & VTK at present - can be expanded further), ensuring compatibility with other tools and platforms.
  - APIs and Integration: By providing APIs and integration capabilities, the tool can work seamlessly with other data analysis and visualization workflows, promoting interoperability.
- **R**eusability
  - Documentation and Templates: The tool includes comprehensive documentation and reusable templates for common visualization types, making it easier for users to replicate and adapt visualizations for their own datasets.
  - Version Control: Implementing version control for visualizations ensures that users can track changes and reuse previous versions as needed.
    
## Impact
### Improve existing capabilities of SPARC tools with direct integration
The sparc-imp tool has been developed to integrate existing SPARC tools such as Pennsieve and sparc-me. This allows for a streamlined process within the SPARC ecosystem from downloading datasets to generating visualisations. By supporting standardised data formats this tool is highly interoperable with existing tools, improving the capabilities and experience of the SPARC platform. The capabilities of spark-imp extend further as it can query metadata and embeded within the visualisations to provide powerful analyses (e.g. scaffold volume). This tool is provided alongside comprehensive documentation to ensure a user-friendly experience, empowering researchers to integrate sparc-imp into their workflows for more consistent and reproducible visualisations. 



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
To report an issue or suggest a new feature, please use the [issues page](https://github.com/SPARC-FAIR-Codeathon/sparc-imp/issues). TODO
Please check existing issues before submitting a new one.
## Contributing

To contribute: fork this repository and submit a pull request. Before submitting a pull request, please read our [Contributing Guidelines](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md). If you found this tool helpful, please add a GitHub Star to support further developments!

### Project structure
-   '/sparc_imp/' - Parent directory of sparc-imp python module.
-   TODO

## Cite us
TODO
## FAIR practices
TODO
## License
sparc-imp is open source and distributed under the Apache License 2.0. See [LICENSE](https://github.com/SPARC-FAIR-Codeathon/2024-team-3/blob/main/LICENSE) for more information.
## Team
* [Michael Hoffman](https://github.com/Moffhan) (Writer)
* [Yun Gu](https://github.com/greeyun) (Developer)
* [Mishaim Malik](https://github.com/Mmal151) (Developer)
* [Mishaim Malik](https://github.com/savindi-wijenayaka) (Developer)
* [Matthew French](https://github.com/frenchmatthew) (Lead, SysAdmin)
## Acknowledgements
- We would like to thank the  2024 SPARC Codeathon organizers for their guidance and support during this Codeathon.

