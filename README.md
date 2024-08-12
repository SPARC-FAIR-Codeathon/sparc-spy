# SPARC Python Imager (SPARC-SPy)
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

[contributors-shield]: https://img.shields.io/github/contributors/SPARC-FAIR-Codeathon/SPARC-SPy.svg?style=flat-square
[contributors-url]: https://github.com/SPARC-FAIR-Codeathon/SPARC-SPy/graphs/contributors
[stars-shield]: https://img.shields.io/github/stars/SPARC-FAIR-Codeathon/SPARC-SPy.svg?style=flat-square
[stars-url]: https://github.com/SPARC-FAIR-Codeathon/SPARC-SPy//stargazers
[issues-shield]: https://img.shields.io/github/issues/SPARC-FAIR-Codeathon/SPARC-SPy/.svg?style=flat-square
[issues-url]: https://github.com/SPARC-FAIR-Codeathon/SPARC-SPy/issues
[issues-closed-shield]: https://img.shields.io/github/issues-closed/SPARC-FAIR-Codeathon/SPARC-SPy.svg
[issues-closed-url]: https://GitHub.com/SPARC-FAIR-Codeathon/sparc-me/issues?q=is%3Aissue+is%3Aclosed
[license-shield]: https://img.shields.io/github/license/SPARC-FAIR-Codeathon/SPARC-SPy.svg?style=flat-square
[license-url]: https://github.com/SPARC-FAIR-Codeathon/SPARC-SPy/blob/master/LICENSE
[code-of-conduct-shield]: https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg
[pypi-shield]: https://badge.fury.io/py/{sparc_spy}.svg
[pypi-url]: https://pypi.python.org/pypi/{sparc_spy}}/
[conventional-commits-shield]: https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white
[conventional-commits-url]: https://conventionalcommits.org



## Table of contents
* [About](#about)
* [Introduction](#introduction)
* [The problem](#the-problem)
* [Our solution - (SPARC-SPy)](#our-solution---(SPARC-SPy))
* [Impact](#impact)
* [Contributing](#contributing)
* [Setting up SPARC-SPy](#setting-up-SPARC-SPy)
* [Reporting issues](#reporting-issues)
* [Contributing](#contributing)
* [Cite us](#cite-us)
* [FAIR practices](#fair-practices)
* [License](#license)
* [Team](#team)
* [Acknowledgements](#acknowledgements)


## About
This is the repository of team SPARC-SPy (Team #3) of the 2024 SPARC Codeathon. Information about the 2024 SPARC Codeathon can be found [here](https://sparc.science/news-and-events/events/2024-sparc-fair-codeathon). 

No work was done on this project prior to the Codeathon. 
## Introduction
The NIH Common fund program *Stimulating Peripheral Activity to Relieve Conditions* ([SPARC](https://commonfund.nih.gov/sparc)) seeks to understand how electrical signals control internal organ function. In doing so it explores how therapeutic devices might modulate nerve activity to treat conditions like hypertension, heart failure, and gastrointestinal disorders. To this end, data have been compiled from 60+ research groups, involving 3900+ subjects across 8 species from  49 different anatomical structures.  

The SPARC Portal offers a user-friendly interface to access and share resources from the SPARC community. It features well-curated, high-impact data, SPARC projects, and computational simulations, all available under the “[Find Data](https://sparc.science/data?type=dataset)” section.
## The problem
In the current landscape of data science and research, visualizing data is crucial for analysis, interpretation, and communication. However, existing tools for reconstructing visualizations from datasets are limited in their accessibility and interoperability. The primary tool available is restricted to the Windows operating system, creating significant barriers for users on other platforms such as macOS and Linux. This limitation hinders the application of the FAIR principles (Findable, Accessible, Interoperable, and Reusable) to data visualization:

### Limited Accessibility:
- Researchers and data scientists using non-Windows operating systems are unable to access the existing tool, leading to inefficiencies and potential data silos.
### Poor Interoperability:
- The existing tool may not support integration with other widely-used data analysis tools or workflows, making it difficult to share and collaborate on visualizations across different platforms and software environments.
### Challenges in Reusability:
- Without a standardized approach to creating and sharing visualizations, researchers may struggle to replicate or adapt visualizations for different datasets or research contexts.

## Our solution - (SPARC-SPy)
We have developed a cross-platform Python visualisation tool called the SPARC Python Imager (SPARC-SPy) to run within o<sup>2</sup>S<sup>2</sup>PARC that can produce VTK visualisations from data scaffolds. This Python module enhancess the **FAIR**ness of SPARC data by:
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
The SPARC-SPy tool has been developed to integrate existing SPARC tools such as Pennsieve and sparc-me. This allows for a streamlined process within the SPARC ecosystem from downloading datasets to generating visualisations. By supporting standardised data formats this tool is highly interoperable with existing tools, improving the capabilities and experience of the SPARC platform. The capabilities of spark-spy extend further as it can query metadata and embeded within the visualisations to provide powerful analyses (e.g. scaffold volume). This tool is provided alongside comprehensive documentation to ensure a user-friendly experience, empowering researchers to integrate SPARC-SPy into their workflows for more consistent and reproducible visualisations. 

### Increase visibility of the value within SPARC's public data 
Visualizations can make complex data more engaging and easier to communicate to a broader audience, including those without a technical background. Using SPARC-SPy for reconstructing visualizations, researchers can more effectively analyze and interpret SPARC’s public data, making it more accessible and understandable, which in turn increases its visibility and impact. The tool can help users discover new insights and patterns within SPARC’s datasets, potentially leading to new research questions and applications and the end goal of effective treatments.

## Setting up SPARC-SPy
### Pre-requisites 
- [Git](https://git-scm.com/)
- Python versions:
   - 3.9
###  Installing via PyPI

Here is the [link](https://pypi.org/project/{PACKAGE_NAME}/) to our project on PyPI TODO
```
pip install sparc_spy
```
### From source code
#### Downloading source code
Clone the SPARC-SPy repository from github, e.g.:
```
git clone git@github.com:SPARC-FAIR-Codeathon/SPARC-SPy TODO
```

### Installing dependencies
TODO

## Using SPARC-SPy
Included are guided tutorials covering some applications of SPARC-SPy:

TODO
<table>
<thead>
  <tr>
    <th> Tutorial</th>
    <th> Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href="tutorials/tutorial_1_getting_started.ipynb">
    Tutorial 1: 
    </a></td>
    <td> **Getting started** - In this tutorial we use SPARC-SPy to import a json scaffold file from a public dataset and visualise it within a jupyter notebook running on o<sup>2</sup>S<sup>2</sup>PARC.</td>
  </tr>
  <tr>
    <td><a href="tutorials/tutorial_2_finding_scaffolds.ipynb">
    Tutorial 2: 
    </a></td>
    <td> **Finding scaffolds** - In this tutorial we show how SPARC-SPy can be used to identify scaffolds within a given sparc dataset.</td>
  </tr>
  <tr>
    <td><a href="tutorials/tutorial_3_generating_analytics.ipynb">
    Tutorial 3: 
    </a></td>
    <td> **Generating analytics** - In this tutorial we show how SPARC-SPy can be use scaffolds and metadata to generate powerful analytics (such as volume, ?average temperature/direction?).</td>
  </tr>
  <tr>
    <td><a href="tutorials/tutorial_4_new_tags.ipynb">
    Tutorial 4: 
    </a></td>
    <td> **New tags** - In this tutorial we show how we can tag visualisations with key descriptors to enable users to quickly identify the data they need.</td>
  </tr> 
  <tr>
    <td><a href="tutorials/tutorial_5_into_the_flow.ipynb">
    Tutorial 5: 
    </a></td>
    <td> **Into the flow** - In this tutorial we show how SPARC-SPy can be used with existing tools such as sparc-flow to simplify visualisation workflows.
  </tr>
  <tr>
    <td><a href="tutorials/tutorial_6_mapping_new_data.ipynb">
    Tutorial 6: 
    </a></td>
    <td> **Mapping new data** - In this tutorial we show how new experimental data can be imported to a scaffold.
  </tr>
</tbody>
</table>
<p align="center">
</p>
<br/>

## Reporting issues 
To report an issue or suggest a new feature, please use the [issues page](https://github.com/SPARC-FAIR-Codeathon/SPARC-SPy/issues). TODO
Please check existing issues before submitting a new one.
## Contributing

To contribute: fork this repository and submit a pull request. Before submitting a pull request, please read our [Contributing Guidelines](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md). If you found this tool helpful, please add a GitHub Star to support further developments!

### Project structure
* '/sparc_spy/' - Parent directory of SPARC-SPy python module.
* '/sparc_spy/core/' - 
* `/resources/`
* '/tutorials/'
  
## Cite us
If you use sparc-flow to make new discoveries or use the source code, please cite us as follows:
```
Michael Hoffman, Yun Gu, Mishaim Malik, Savindi Wijenayaka, Matthew French (2024). SPARC-SPy: v1.0.0 - A python tool to enhance the accessibility of SPARC dataset visualisations and their analyses in accordance with FAIR principles.
Zenodo. https://doi.org/XXXX/zenodo.XXXX. TODO
```
## FAIR practices
TODO
## License
SPARC-SPy is open source and distributed under the Apache License 2.0. See [LICENSE](https://github.com/SPARC-FAIR-Codeathon/2024-team-3/blob/main/LICENSE) for more information.
## Team
* [Michael Hoffman](https://github.com/Moffhan) (Writer)
* [Yun Gu](https://github.com/greeyun) (Developer)
* [Mishaim Malik](https://github.com/Mmal151) (Developer)
* [Savindi Wijenayaka](https://github.com/savindi-wijenayaka) (SysAdmin, Developer)
* [Matthew French](https://github.com/frenchmatthew) (Lead, Developer)
## Acknowledgements
- We would like to thank the  2024 SPARC Codeathon organizers for their guidance and support during this Codeathon.

