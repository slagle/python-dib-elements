# Copyright 2013, Red Hat Inc.
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


import argparse
import logging

from dib_elements import manager


def load_args():
    parser = argparse.ArgumentParser(
        description="Execute diskimage-builder elements on the current system.")
    parser.add_argument(
        '-e', '--element', nargs='*',
        help="element(s) to execute")
    parser.add_argument(
        '-p', '--element-path', nargs='*',
        help=("element path(s) to search for elements (ELEMENTS_PATH "
              "environment variable will take precedence if defined)"))
    return parser.parse_args()


def main():
    args = load_args()
    logging.basicConfig(level=logging.DEBUG, 
                        format="%(levelname)s:%(asctime)s:%(name)s:%(message)s")
    em = manager.ElementManager(args.element, args.element_path)
    em.run_hook('install')


if __name__ == '__main__':
    main()