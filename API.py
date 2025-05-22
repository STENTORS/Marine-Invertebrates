import pyportal
from pyportal.constants import resources

def get_marine_invertebrates():
    api_key = None
    api = pyportal.API(api_key)

    res_id = resources.specimens
    all_records = []

    search = api.records(res_id, query="Malacostraca")
    for record in search.all():
        if "associatedMedia" in record:

            filtered_media = [
                media for media in record["associatedMedia"]
                if "title" not in media or "page" not in media["title"].lower()
            ]

            if filtered_media:
                record["associatedMedia"] = filtered_media
                all_records.append(record)

            if len(all_records) >= 200:
                break

    return all_records

