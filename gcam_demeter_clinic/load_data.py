import pkg_resources


def get_config_file():
    """Get the configuration file from package data.

    :return:                    Path to configuration file

    """

    return pkg_resources.resource_filename('gcam_demeter_clinic', 'data/csdms_clinic_config.ini')
