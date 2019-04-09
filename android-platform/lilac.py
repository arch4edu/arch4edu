#!/usr/bin/env python3
from lilaclib import *
import os

update_on = [{'aur': None}]
build_prefix = 'multilib'
repo_depends = ['android-sdk', 'android-sdk-platform-tools']

def pre_build():
    aur_pre_build()
    os.environ['http_proxy'] = '127.0.0.1:8123'
    os.environ['https_proxy'] = '127.0.0.1:8123'

def post_build():
    aur_post_build()
    del os.environ['http_proxy']
    del os.environ['https_proxy']

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
