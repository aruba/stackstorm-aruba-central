

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#------------------------------------------------------------------------------#
#
#                   _                            _             _                    _
#                  | |                          | |           | |                  | |
#   __ _ _ __ _   _| |__   __ _    ___ ___ _ __ | |_ _ __ __ _| |  _ __   __ _  ___| | __
#  / _` | '__| | | | '_ \ / _` |  / __/ _ \ '_ \| __| '__/ _` | | | '_ \ / _` |/ __| |/ /
# | (_| | |  | |_| | |_) | (_| | | (_|  __/ | | | |_| | | (_| | | | |_) | (_| | (__|   <
#  \__,_|_|   \__,_|_.__/ \__,_|  \___\___|_| |_|\__|_|  \__,_|_| | .__/ \__,_|\___|_|\_\
#                                                                 | |
#                                                                 |_|
#
# __author__ = "@netwookie"
# __credits__ = ["Rick Kauffman"]
# __license__ = "Apache2.0"
# __maintainer__ = "Rick Kauffman"
#
#------------------------------------------------------------------------------#

from lib.actions import ArubaCentralBaseAction
from pycentral.configuration import Groups
import json


__all__ = [
    'DeleteGroups'
]

class DeleteGroups(ArubaCentralBaseAction):
    def run(self,group_name=None):
        groups = Groups()
        response = groups.delete_group(conn=self.auth,group_name=group_name)

        return(response['code'])
