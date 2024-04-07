#!/usr/bin/python3
"""
Create and distribute archive to web server
"""

from fabric.api import run, put, env
from AirBnB_clone_v2 import do_pack, do_deploy


def deploy():
    """Create and distribute archive to web servers."""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
