#!/usr/bin/python3
"""
Create and distribute archive to web server
"""

from fabric.api import run, put, env
import 2-do_deploy_web_static



def deploy():
    """Create and distribute archive to web servers."""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
