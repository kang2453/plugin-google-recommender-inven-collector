#
#   Copyright 2020 The SpaceONE Authors.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


from setuptools import setup, find_packages

with open("VERSION", "r") as f:
    VERSION = f.read().strip()
    f.close()

setup(
    name="plugin-google-recommender-inven-collector",
    version=VERSION,
    description="Google cloud Recommender service inventory collector",
    long_description="",
    url="https://www.spaceone.dev/",
    author="MEGAZONE SpaceONE Team",
    author_email="admin@spaceone.dev",
    license="Apache License 2.0",
    packages=find_packages(),
    install_requires=[
        "spaceone-api",
        "google-api-python-client",
        "requests",
        "beautifulsoup4",
    ],
    package_data={"cloudforet": ["plugin/metadata/*/*.yaml"]},
    zip_safe=False,
)
