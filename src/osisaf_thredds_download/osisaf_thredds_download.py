# ---- This <osisaf_thredds_download.py> ----

"""
Download passive microwave SIC products from OSISAF thredds server
"""

import pathlib
from loguru import logger

import xarray as xr

import requests
from bs4 import BeautifulSoup

import osisaf_thredds_download.utils as osi_utils

# -------------------------------------------------------------------------- #
# -------------------------------------------------------------------------- #

def download_osisaf_daily_SIC(date, hemisphere, sensor, download_dir, overwrite=False):
    """
    Download average daily SIC for input date and hemisphere, and sensor
    
    Parameters
    ----------
    date : input date ('YYYY-MM-DD')
    hemisphere : choose northern or southern hemisphere ('NH', 'SH')
    sensor : choose amsr2 or multi ('amsr2', 'multi' )
    download_dir : download directory
    overwrite : overwrite existing files (default=False)
    """

    hemisphere   = hemisphere.lower()
    sensor       = sensor.lower()
    download_dir = pathlib.Path(download_dir)

    # check all inputs
    if not all([
        osi_utils.check_date(date),
        osi_utils.check_hemisphere(hemisphere),
        osi_utils.check_sensor_daily(sensor),
        osi_utils.check_download_dir(download_dir)
    ]):
        return None

    # ------------------------------ #

    # build url to ncdf file and path to downloaded file

    # OSISAF thredds url for sea ice products
    osisaf_opendap_ice_thredds = "https://thredds.met.no/thredds/dodsC/osisaf/met.no/ice"
    
    # get year, month, day
    yyyy, mm, dd = date.split('-')

    # a bit ugly: amsr2 data is in a subfolder called 'amsr2_conc, ssmis/amsr2 data is in 'conc'
    if sensor=='amsr2':
        subfolder = 'amsr2_conc'
    elif sensor=='multi':
        subfolder = 'conc'

    # build file name for current product (daily products  have mid-day (1200) time stamp)
    ncdf_file_name = f"ice_conc_{hemisphere}_polstere-100_{sensor}_{yyyy}{mm}{dd}1200.nc"

    # build full thredds url
    full_url = f"{osisaf_opendap_ice_thredds}/{subfolder}/{yyyy}/{mm}/{ncdf_file_name}"
    
    # build full download path
    download_path = download_dir / ncdf_file_name

    # ------------------------------ #
    
    if not download_path.is_file() or overwrite:

        logger.info(f"Downloading OSISAF SIC data for {date} ({hemisphere.upper()})")
        logger.info(f"Source URL: {full_url}")
        logger.info(f"Saving to: {download_path}")

        try:
            with xr.open_dataset(full_url) as ds:
                ds.to_netcdf(download_path)
        except Exception as e:

            logger.error(f"Failed to download or save dataset: {e}")
            return None
        
    else:
        logger.info(f"'{download_path}' already exists")
        
    return

# -------------------------------------------------------------------------- #
# -------------------------------------------------------------------------- #

def download_osisaf_full_month_daily_SIC(year, month, hemisphere, sensor, download_dir, overwrite=False):

    month = str(month).zfill(2)
    hemisphere   = hemisphere.lower()
    sensor       = sensor.lower()
    download_dir = pathlib.Path(download_dir)

    # check all inputs
    if not all([
        osi_utils.check_year_month(year, month),
        osi_utils.check_hemisphere(hemisphere),
        osi_utils.check_sensor_daily(sensor),
        osi_utils.check_download_dir(download_dir)
    ]):
        return None

    # ------------------------------ #

    # build url to catalogue for the month

    # a bit ugly: amsr2 data is in a subfolder called 'amsr2_conc, ssmis/amsr2 data is in 'conc'
    if sensor=='amsr2':
        subfolder = 'amsr2_conc'
    elif sensor=='multi':
        subfolder = 'conc'

    url = f"https://thredds.met.no/thredds/catalog/osisaf/met.no/ice/{subfolder}/{year}/{month}/catalog.html"

    logger.debug(f"Catalogue url: {url}")

    # ------------------------------ #

    # fetch the HTML content
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # extract file links
    file_links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.endswith('.nc') and f"_{hemisphere}_" in href :  # Adjust file extension as needed
            file_links.append(href)
            
    # ------------------------------ #

    # loop over file links and download
    
    for file in file_links:
        logger.debug(f"Processing file link: {file}")

        # ------------------------------ #

        # build url to ncdf file and path to downloaded file

        # OSISAF thredds url for sea ice products
        osisaf_opendap_ice_thredds = "https://thredds.met.no/thredds/dodsC/osisaf/met.no/ice"

        # get file name for current product (daily products  have mid-day (1200) time stamp)
        ncdf_file_name = file.split('/')[-1]
        
        # build full thredds url
        full_url = f"{osisaf_opendap_ice_thredds}/{subfolder}/{year}/{month}/{ncdf_file_name}"

        # build full download path
        download_path = download_dir / ncdf_file_name

        # ------------------------------ #
    
        if not download_path.is_file() or overwrite:

            logger.info(f"Downloading OSISAF SIC data for {year}/{month} ({hemisphere.upper()})")
            logger.info(f"Source URL: {full_url}")
            logger.info(f"Saving to: {download_path}")

            try:
                with xr.open_dataset(full_url) as ds:
                    ds.to_netcdf(download_path)
            except Exception as e:

                logger.error(f"Failed to download or save dataset: {e}")
                return None
        
        else:
            logger.info(f"'{download_path}' already exists")

    return

# -------------------------------------------------------------------------- #
# -------------------------------------------------------------------------- #

def download_osisaf_level2_daily_SIC(date, hemisphere, sensor, download_dir, overwrite=False):

    hemisphere   = hemisphere.lower()
    sensor       = sensor.lower()
    download_dir = pathlib.Path(download_dir)

    # check all inputs
    if not all([
        osi_utils.check_date(date),
        osi_utils.check_hemisphere(hemisphere),
        osi_utils.check_sensor_daily(sensor),
        osi_utils.check_download_dir(download_dir)
    ]):
        return None

# -------------------------------------------------------------------------- #
# -------------------------------------------------------------------------- #

# ---- End of <osisaf_thredds_download.py> ----