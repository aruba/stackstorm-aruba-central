
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# __author__ = "@netwookie"
# __credits__ = ["Rick Kauffman"]
# __license__ = "Apache2.0"
# __maintainer__ = "Rick Kauffman."
# __email__ = "rick@riickkauffman.com"

from pymongo import MongoClient
from pycentral.base import ArubaCentralBase
from st2common.runners.base_action import Action
import json

__all__ = [
    'ArubaCentralBaseAction'
]


class ArubaCentralBaseAction(Action):
    def __init__(self, config):
        super(ArubaCentralBaseAction, self).__init__(config=config)
        self.auth = self._get_auth()
        print(self.auth)

    def _get_auth(self):
        client_id = self.config['client_id']
        client_secret = self.config['client_secret']
        username = self.config['username']
        password = self.config['password']
        customer_id = self.config['customer_id']
        base_url = self.config['base_url']
        

        # Create central_info dictionary
        central_info = {}
        central_info['client_id'] = client_id
        central_info['client_secret'] = client_secret
        central_info['username'] = username
        central_info['password'] = password
        central_info['customer_id'] = customer_id
        central_info['base_url'] = base_url

        ssl_verify = True
        token = ArubaCentralBase(central_info=central_info,ssl_verify=ssl_verify)

        return token
