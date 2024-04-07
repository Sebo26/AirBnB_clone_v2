from fabric.api import local
from datetime import datetime
import os

def do_pack():
    if not os.path.exists("versions"):
        local("mkdir versions")
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(timestamp)
    local("tar -czvf versions/{} web_static".format(archive_name))
    return "versions/{}".format(archive_name)
else:
    return None
