# ### METADATA

# Connectors:
# Description:

# ### CONFIGURATION

# Set the configuration variables below or set environmental variables of the same name and leave
# these with empty strings.  We recommend using environmental variables if possible.

config_vars = {
}

# Setup
from parsons import Zoom

zoom = Zoom()
users_tbl = zoom.get_users()

user_id = None
for user in users_tbl:
    if user["first_name"] == "Shauna":
        user_id = user["id"]

meetings_tbl = zoom.get_meetings(user_id)
meeting = meetings_tbl[0]

participants = zoom.get_past_meeting_participants(meeting["id"])
print(participants)


# for meeting in meetings_tbl:
#     meeting_id = meeting["id"]
#     print("Getting for: ", meeting_id)
#     print(zoom.get_past_meeting(meeting_id))

