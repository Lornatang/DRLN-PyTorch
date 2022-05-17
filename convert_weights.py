# Copyright 2022 Dakewe Biotech Corporation. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
import torch

from model import DRLN

model = DRLN(8)
old_state_dict = torch.load("DRLN_BIX8.pt")

new_state_dict = model.state_dict()

old_lists = []
new_lists = []

for k, v in old_state_dict.items():
    old_lists.append(k)

for k, v in new_state_dict.items():
    new_lists.append(k)

new_lists = new_lists[1:]
old_lists = old_lists[4:]

for index in range(len(old_lists)):
    new_state_dict[new_lists[index]] = old_state_dict[old_lists[index]]

torch.save({"state_dict": new_state_dict}, "DRLN_BIX8.pth.tar")
