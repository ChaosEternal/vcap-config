import json, os, re
VCAP_APP_CONFIG = json.loads(os.getenv('VCAP_APPLICATION', """{"uris": ["127.0.0.1:8080"]}"""))
VCAP_SERVICE_CONFIG = json.loads(os.getenv('VCAP_SERVICES', """{}"""))
VCAP_APP_URI = VCAP_APP_CONFIG['uris'][0]

def vcap_extract_cred(srv_config, srvname="srvdb$", tag="relational"):
    for i in srv_config.values():
        for j in i:
            if tag in j.get("tags", []):
                if re.search(srvname, j.get("name", "")):
                    return j["credentials"]
                for t in j.get("tags", []):
                    if re.match(srvname, t):
                        return j["credentials"]
    return None
