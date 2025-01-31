"""Setup for edx-sga XBlock."""

from __future__ import absolute_import

import os

from setuptools import find_packages, setup

import edx_sga


def package_data(pkg, root_list):
    """Generic function to find package_data for `pkg` under `root`."""
    data = []
    for root in root_list:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}

setup(
    name='edx-sga',
    version=edx_sga.__version__,
    description='edx-sga Staff Graded Assignment XBlock',
    license='Affero GNU General Public License v3 (GPLv3)',
    # url="https://github.com/mitodl/edx-sga",
    # author="MITx",
    url="https://github.com/guangyawli/edx-sga",
    author="MITx",
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'XBlock',
        'xblock-utils',
        'web_fragments',
        'requests',
    ],
    entry_points={
        'xblock.v1': [
            'edx_sga = edx_sga.sga:StaffGradedAssignmentXBlock',
        ]
    },
    package_data=package_data("edx_sga", ["static", "templates"]),
)
