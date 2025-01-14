"""
/github/objects/ratelimit.py

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

import datetime

from github import utils


class RateLimit():
    """
    Represents the viewer's rate limit.

    https://developer.github.com/v4/object/ratelimit/
    """

    __slots__ = ("data",)

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<{0} cost={1} limit={2} remaining={3} reset_at={4}>".format(
            self.__class__.__name__, self.cost, self.limit, self.remaining, self.reset_at.timestamp())

    @classmethod
    def from_data(cls, data):
        return cls(data["rateLimit"])

    @property
    def cost(self) -> int:
        """
        The point cost for the current query counting against the rate limit.
        """

        return self.data.get("cost")

    @property
    def limit(self) -> int:
        """
        The maximum number of points the viewer is permitted to consume in a 60 minute window.
        """

        return self.data.get("limit")

    @property
    def remaining(self) -> int:
        """
        The number of points remaining in the current rate limit window.
        """

        return self.data.get("remaining")

    @property
    def reset_at(self) -> datetime.datetime:
        """
        The time at which the current rate limit window resets in UTC.
        """

        return utils.iso_to_datetime(self.data.get("resetAt"))
