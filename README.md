<img src="thumbnail.png" alt="thumbnail" width="300"/>

# Geostationary satellite Cookbook

[![nightly-build](https://github.com/ProjectPythia/cookbook-template/actions/workflows/nightly-build.yaml/badge.svg)](https://github.com/ProjectPythia/cookbook-template/actions/workflows/nightly-build.yaml)
[![Binder](https://binder.projectpythia.org/badge_logo.svg)](https://binder.projectpythia.org/v2/gh/ProjectPythia/cookbook-template/main?labpath=notebooks)
[![DOI](https://zenodo.org/badge/475509405.svg)](https://zenodo.org/badge/latestdoi/475509405)

The "Project Pythia Cookbook" aims to provide a comprehensive guide for utilizing Satpy to analyze geostationary satellite data of the sensor Advanced Baseline Imager ([ABI](https://www.goes-r.gov/spacesegment/abi.html)) on [GOES-R](https://www.goes-r.gov) (west and east), sensor Advanced Himawari Imager ([AHI](https://www.data.jma.go.jp/mscweb/en/himawari89/space_segment/spsg_ahi.html)) on [HIMAWARI](https://www.jma.go.jp/jma/jma-eng/satellite/himawari89.html), and sensor Advance Meteorological Imager (AMI) on [Geo-KOMPSAT-2A](https://nmsc.kma.go.kr/enhome/html/base/cmm/selectPage.do?page=satellite.gk2a.intro) (GK2A). [Satpy](https://satpy.readthedocs.io/en/stable/) is a powerful Python library specifically designed for processing and analyzing satellite data, offering capabilities for data visualization, manipulation, and analysis.

## Motivation

Global weather, climate, and environmental phenomena monitoring is greatly aided by geostationary satellites such as GOES-R, HIMAWARI, and GK2A. The need for thorough tools and resources to efficiently analyze and interpret satellite data is growing as the use of such data for scientific research, weather forecasting, and environmental monitoring grows. A Python library called Satpy was created specifically for handling data from satellite instruments that observe the Earth. Remote-sensing data can be read, modified, and written with it. Geophysical parameters can be converted from various file formats into Xarray DataArray and Dataset classes, which allow for easy integration with other scientific Python libraries. Satpy combines data from various instrument bands or products to make it easier to create RGB images and composite types. In order to enhance the quality and usefulness of images, it has features for atmospheric corrections and visual improvements. Several formats, including PNG, GeoTIFF, and CF standard NetCDF files, are available for saving output data. Users can resample data to geographic projected grids (areas) using Satpy as well.Although there are already guides and tutorials available for using Satpy, there isn't much thorough advice that is tailored specifically to the analysis 
of the three geostationary satellites that can be accessed freely from AWS buckets [AWS_GOES-R](https://registry.opendata.aws/noaa-goes/), [AWS_HIMAWARI](https://registry.opendata.aws/noaa-himawari/), and [AWS_GK2A](https://registry.opendata.aws/noaa-gk2a-pds/). Users can gain access to structured tutorials, detailed instructions, and sample workflows that are specifically designed to meet the needs and distinctive features of these satellites by creating a cookbook specifically for them.


## Authors

[jhbravo](@jhbravo), [Second Author](@second-author), etc. _Acknowledge primary content authors here_

### Contributors

<a href="https://github.com/ProjectPythia/cookbook-template/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ProjectPythia/cookbook-template" />
</a>

## Structure

(State one or more sections that will comprise the notebook. E.g., _This cookbook is broken up into two main sections - "Foundations" and "Example Workflows."_ Then, describe each section below.)

### Section 1 ( Replace with the title of this section, e.g. "Foundations" )

(Add content for this section, e.g., "The foundational content includes ... ")

### Section 2 ( Replace with the title of this section, e.g. "Example workflows" )

(Add content for this section, e.g., "Example workflows include ... ")

## Running the Notebooks

You can either run the notebook using [Binder](https://binder.projectpythia.org/) or on your local machine.

### Running on Binder

The simplest way to interact with a Jupyter Notebook is through
[Binder](https://binder.projectpythia.org/), which enables the execution of a
[Jupyter Book](https://jupyterbook.org) in the cloud. The details of how this works are not
important for now. All you need to know is how to launch a Pythia
Cookbooks chapter via Binder. Simply navigate your mouse to
the top right corner of the book chapter you are viewing and click
on the rocket ship icon, (see figure below), and be sure to select
“launch Binder”. After a moment you should be presented with a
notebook that you can interact with. I.e. you’ll be able to execute
and even change the example programs. You’ll see that the code cells
have no output at first, until you execute them by pressing
{kbd}`Shift`\+{kbd}`Enter`. Complete details on how to interact with
a live Jupyter notebook are described in [Getting Started with
Jupyter](https://foundations.projectpythia.org/foundations/getting-started-jupyter.html).

### Running on Your Own Machine

If you are interested in running this material locally on your computer, you will need to follow this workflow:

(Replace "cookbook-example" with the title of your cookbooks)

1. Clone the `https://github.com/ProjectPythia/cookbook-example` repository:

   ```bash
    git clone https://github.com/ProjectPythia/cookbook-example.git
   ```

1. Move into the `cookbook-example` directory
   ```bash
   cd cookbook-example
   ```
1. Create and activate your conda environment from the `environment.yml` file
   ```bash
   conda env create -f environment.yml
   conda activate cookbook-example
   ```
1. Move into the `notebooks` directory and start up Jupyterlab
   ```bash
   cd notebooks/
   jupyter lab
   ```
