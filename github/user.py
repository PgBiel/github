"""
/user.py

    Copyright (c) 2019 ShineyDev
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from .utils import (
    abc,
)


class User(abc.DataStore):
    def __eq__(self, other):
        ...

    def __repr__(self):
        return "<User >".format()

    @classmethod
    def from_data(cls, data: dict):
        if (data is None):
            return None

        return cls._from_data(data)