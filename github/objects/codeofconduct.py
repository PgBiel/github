"""
/github/objects/codeofconduct.py

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

from github.objects import abc


class CodeOfConduct(abc.Node):
    """
    Represents a Code of Conduct.

    https://developer.github.com/v4/object/codeofconduct
    """

    __slots__ = ("data",)

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<{0} key='{1}'>".format(self.__class__.__name__, self.key)

    @classmethod
    def from_data(cls, data):
        if "codeOfConduct" in data:
            return cls(data["codeOfConduct"])
        else:
            codes = list()

            for (code) in data["codesOfConduct"]:
                codes.append(cls(code))

            return codes

    @property
    def body(self):
        """
        The body of this Code of Conduct.
        """

        return self.data.get("body")

    @property
    def key(self):
        """
        The key for this Code of Conduct.
        """

        return self.data.get("key")

    @property
    def name(self):
        """
        The formal name of this Code of Conduct.
        """

        return self.data.get("name")

    @property
    def url(self):
        """
        The http url for this Code of Conduct.
        """

        return self.data.get("url")
