import pyportal
from pyportal.constants import resources


def get_marine_invertebrates():
    api_key = None
    api = pyportal.API(api_key)

    res_id = resources.specimens

    search = api.records(res_id, query="Architeuthis")
    for record in search.all():
        if "associatedMedia" in record:
            return(record)

get_marine_invertebrates()