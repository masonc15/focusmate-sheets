import requests
import json
from datetime import datetime
import pytz


def get_sessions_json():
    url = "https://api.focusmate.com/v1/sessions?start=2022-01-01T12:00:00Z&end=2022-07-26T13:00:00Z"

    payload = {}
    headers = {'X-API-KEY': '0620bc9746ef49de98214cc49c0c4fd0'}

    response = requests.request("GET", url, headers=headers, data=payload)

    json_response = json.loads(response.text)
    return json_response


def get_recent_partner_id(sessions):
    most_recent_session = sessions['sessions'][0]
    partner_id = most_recent_session['users'][1]['userId']
    return partner_id


def get_partner_profile(partner_id):
    url = "https://api.focusmate.com/v1/users/" + partner_id
    payload = {}
    headers = {'X-API-KEY': '0620bc9746ef49de98214cc49c0c4fd0'}
    response = requests.request("GET", url, headers=headers, data=payload)
    json_response = json.loads(response.text)
    return json_response


sessions = get_sessions_json()
recent_partner_id = get_recent_partner_id(sessions)
partner_profile = get_partner_profile(recent_partner_id)


def get_session_start_datetime(sessions):
    most_recent_session = sessions['sessions'][0]
    session_datetime = most_recent_session['startTime']
    # convert to datetime object
    date_object = datetime.strptime(session_datetime, '%Y-%m-%dT%H:%M:%S%z')
    # convert date_object timezone to EST
    date_object = date_object.astimezone(pytz.timezone('US/Eastern'))
    # convert date_object to m-d-y format
    date_string = date_object.strftime('%m-%d-%y')
    return date_object


# create variables for relevant partner data
partner_name = partner_profile['user']['name']
partner_tz = partner_profile['user']['timeZone']
partner_session_count = partner_profile['user']['totalSessionCount']

# most recent session variables
start_date = get_session_start_datetime(sessions).strftime('%m-%d-%y')
start_time = get_session_start_datetime(sessions).strftime('%I:%M %p')