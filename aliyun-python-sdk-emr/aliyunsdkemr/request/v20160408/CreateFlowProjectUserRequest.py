# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class CreateFlowProjectUserRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'CreateFlowProjectUser')

	def get_ProjectId(self):
		return self.get_query_params().get('ProjectId')

	def set_ProjectId(self,ProjectId):
		self.add_query_param('ProjectId',ProjectId)

	def get_Users(self):
		return self.get_query_params().get('Users')

	def set_Users(self,Users):
		for i in range(len(Users)):	
			if Users[i].get('UserId') is not None:
				self.add_query_param('User.' + str(i + 1) + '.UserId' , Users[i].get('UserId'))
			if Users[i].get('UserName') is not None:
				self.add_query_param('User.' + str(i + 1) + '.UserName' , Users[i].get('UserName'))
