# ---- This <osi_utils.py> ----

"""
Utils for handling download from OSISAF thredds server
"""

from loguru import logger

# -------------------------------------------------------------------------- #
# -------------------------------------------------------------------------- #

def check_date(date):
    try:
        YYYY, MM, DD = date.split('-')
    except:
        logger.error("Input date format must be 'YYYY-MM-DD'. Example: '2023-10-01'")
        return False
    return True


def check_year_month(year, month):
    min_year  = 1990
    max_year  = 2030
    min_month = 1
    max_month = 12
    if not min_year <= int(year) <= max_year:
        return False
    if not min_month <= int(month) <= max_month:
        return False
    return True


def check_hemisphere(hemisphere):
    if hemisphere not in ['nh', 'sh']:
        logger.error("Invalid hemisphere. Must be 'nh' (Northern Hemisphere) or 'sh' (Southern Hemisphere).")
        return False
    return True


def check_download_dir(download_dir):
    if not download_dir.is_dir():
        logger.error(f"Could not find download_dir: {download_dir}")
        return False
    return True

def check_sensor_daily(sensor):
    if sensor not in ['amsr2', 'multi']:
        logger.error("Invalid sensor. Must be 'amsr2' or 'multi'.")
        return None
    return True

def check_sensor_level2(sensor):
    if sensor not in ['amsr2', 'ssmis']:
        logger.error("Invalid sensor. Must be 'amsr2' or 'ssmis'.")
        return None
    return True

# -------------------------------------------------------------------------- #
# -------------------------------------------------------------------------- #

# ---- End of <osi_utils.py> ----