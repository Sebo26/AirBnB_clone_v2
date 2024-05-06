#!/usr/bin/python3
"""
Create and distribute archive to web server
"""

from fabric.api import run, put, env
from 1-pack_web_static import do_pack
from 2-do_deploy_web_static import do_deploy


def deploy():
    """Create and distribute archive to web servers."""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
