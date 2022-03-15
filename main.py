#!/usr/bin/python3

#
# Copyright (C) 2022-present lifehackerhansol
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from os import path
from typing import Optional
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/banner/{game_id}")
async def get_banner(game_id: str):
    response = {}
    if not path.isdir(f"assets/{game_id}"):
        if path.isdir(f"assets/{game_id[:3]}"):
            game_id = game_id[:3]
        else:
            raise HTTPException(status_code=404, detail="Game not found")

    if path.isfile(f"assets/{game_id}/{game_id}.png"):
        response['image'] = f"https://github.com/lifehackerhansol/YANBF-assets/raw/main/assets/{game_id}/{game_id}.png"
    if path.isfile(f"assets/{game_id}/{game_id}.wav"):
        response['sound'] = f"https://github.com/lifehackerhansol/YANBF-assets/raw/main/assets/{game_id}/{game_id}.wav"
    if response == {}:
        raise HTTPException(status_code=404, detail="Game not found")
    return response
