# ### METADATA

# Connectors:
# Description: Takes a list of volunteers from a Google Sheets doc and adds them to VAN.

# ### CONFIGURATION

# Set the configuration variables below or set environmental variables of the same name and leave
# these with empty strings.  We recommend using environmental variables if possible.

config_vars = {
    # # Connector 1: Google Sheets
    # "GOOGLE_DRIVE_CREDENTIALS": "",
    # Connector 2: VAN
    # "VAN_API_KEY": """,
    "VAN_DB": 'MyVoters'
}


# ### CODE

import os  # noqa: E402
from parsons import Table, utilities, logger, VAN, GoogleSheets  # noqa: E402

# if variables specified above, sets them as environmental variables
for name, value in config_vars.items():
    if value.strip() != "":
        os.environ[name] = value

# instantiate connectors
# sheets = GoogleSheets()  # or if sheets not working, just use tbl = Table.from_csv('new_volunteers.csv')
van = VAN(db=os.environ["VAN_DB"])

# get people with their data from CSV
people_list = Table.from_csv('useful_resources/sample_code/people.csv')


person = van.find_person(first_name="Rachel", last_name="Allred", phone="(555) 802-8192")
print(person)


# TODO:
# - get some fake people from demo site and add to google sheets or to csv to test
# - then can try out upsert






