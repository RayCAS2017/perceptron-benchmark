# Copyright 2019 Baidu Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Random utils"""

import random
import numpy as np
rng = random.Random()
nprng = np.random.RandomState()


def set_seeds(seed):
    """Sets the seeds of both random number generators used by Foolbox.

    Parameters
    ----------
    seed : int
        The seed for both random number generators.

    """
    rng.seed(seed)
    nprng.seed(seed)
