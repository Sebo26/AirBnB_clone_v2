#!/usr/bin/python3
"""
distributes an archive to web servers
"""

from fabric.api import run, put, env
import os

env.hosts = ['xx-web-01', 'xx-web-02']

def do_deploy(archive_path):
    """deploy archive"""
    if not os.path.exists(archive_path):
        print("Archive {} does not exist.".format(archive_path))
        return False
    put(archive_path, '/tmp/')

    archive_filename = os.path.basename(archive_path)
    release_folder = '/data/web_static/releases/{}'.format(archive_filename[:-4])
    run('mkdir -p {}'.format(release_folder))
    run('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_folder))

    run('rm /tmp/{}'.format(archive_filename))
    run('rm -rf /data/web_static/current')
    run('ln -s {} /data/web_static/current'.format(release_folder))
    serve_static_files_locally()
    return True
