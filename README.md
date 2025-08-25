# osisaf_thredds_download

Library for download of SIC netCDF files from OSISAF thredds server.

For manual, web browser based access to the data visit [https://osi-saf.eumetsat.int/products/sea-ice-products](https://osi-saf.eumetsat.int/products/sea-ice-products)


### Preparation
Create anaconda environment:

    # create and activate new environment
    conda create -y --name OSISAF python=3.12
    conda activate OSISAF

    # install requirements
    conda install -y xarray loguru requests netCDF4 pydap


### Installation
You can install this library directly from github (1) or locally after cloning (2).  
For both installation options, first set up the environment as described above.

1. **Installation from github**

       # install this package
       pip install git+https://github.com/jlo031/osisaf_thredds_download

2. **Local installation**

       # clone the repository
       git clone git@github.com:jlo031/osisaf_thredds_download

   Change into the main directory of the cloned repository (it should contain the *setup.py* file) and install the library:

       # installation
       pip install .


### Usage
TO DO
