#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import os, sys
from termcolor import colored, cprint
from argparse import ArgumentParser
import pickle
from subprocess import Popen, PIPE, STDOUT
import threading

lock = threading.Lock()


class PackageInstaller(object):

    def __init__(self, dir, options):
        self.dir = dir
        self.options = options

    def _generate_command(self, package):
        wait_cmd = " && read"
        cmd = "cd %s/%s" % (self.dir, package)

        # Before doing anything, review Git changes
        if self.options.git:
            cmd += " && git diff --color . " + wait_cmd

        # Make the package
        cmd += " && makepkg -if"

        # Add changes to the Git index
        if self.options.git:
            cmd += " && git add PKGBUILD"

        if self.options.aur or self.options.export_user != "":
            cmd += " && mkaurball -f"

        if self.options.export_user != "":
            cmd += " && burp -u %s -c devel `ls -c1 | grep src.tar.gz | head -n 1`" \
                % self.options.export_user

        return cmd

    def install(self, package):
        if not os.path.isfile("%s/%s/PKGBUILD" % (self.dir, package)):
            return

        lock.acquire()
        print(colored("\n\nInstalling %s " % package, 'red', attrs=['bold']))

        cmd = self._generate_command(package)
        # TODO: adapt to shell=False for security
        p = Popen(cmd, stdin=sys.stdin,
                  stdout=PIPE,
                  stderr=sys.stderr.fileno(),
                  shell=True, bufsize = 1)
        while p.poll() is None:
            out = p.stdout.read(1)
            sys.stdout.write(out)
            sys.stdout.flush()
        lock.release()


def main():
    parser = ArgumentParser(description="Install generated PKGBUILDs.")

    parser.add_argument('distro', default='hydro',
                        help='ROS distribution.')

    parser.add_argument('-a', '--aur', dest='aur', action='store_true',
                        default=False,
                        help='Make AUR tarball.')

    parser.add_argument('-e', '--export', dest='export_user', default='',
                        help="Export package to the AUR. "
                        "A username is expected.")

    parser.add_argument('-g', '--git', dest='git', action='store_true',
                        default=False,
                        help='Add changes of the PKGBUILD to the Git index.')

    args = parser.parse_args()
    distro = args.distro

    makepkg_dump_filename = "/tmp/import_catkin_packages/makepkg_%s.dump" \
                            % distro

    if not os.path.isfile(makepkg_dump_filename):
        print("Could not find dump file: %s" % makepkg_dump_filename)
        sys.exit()

    makepkg_dump = open(makepkg_dump_filename, "r")
    to_install = pickle.load(makepkg_dump)
    makepkg_dump.close()

    installer = PackageInstaller(to_install["directory"], options=args)

    try:
        for package in to_install["packages"]:
            installer.install(package=package)
            to_install["packages"].remove(package)
    except KeyboardInterrupt:
      pass

    makepkg_dump = open(makepkg_dump_filename, "wb")
    pickle.dump(to_install, makepkg_dump)
    makepkg_dump.close()

if __name__ == '__main__':
    main()
