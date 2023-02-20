#
# Copyright 2023 lifehackerhansol
#
# SPDX-License-Identifier: Apache-2.0
#

#
# Generate json of all files present in the `assets` directory
#

import json
import os

if __name__ == "__main__":
    f = open('assets.json', 'w')
    folders = os.listdir('assets')

    assets = {
    }
    for i in folders:
        assets[i] = {}
        for j in os.listdir(f"assets/{i}"):
            if '.wav' in j:
                assets[i]["sound"] = True
    print(assets)
    output = {}
    output["assets"] = assets
    print(output)
    json.dump(output, f, indent=2)
