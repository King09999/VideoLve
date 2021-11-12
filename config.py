#!/usr/bin/env python3
# Copyright (C) @ZauteKm
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()

admins = {}
OLD_PMS = {}
AUDIO_CALL = {}
VIDEO_CALL = {}
API_ID = int(getenv("API_ID", "8191170"))
API_HASH = getenv("API_HASH", "3a6d8f5158858786291d2b40b6e5957b")
BOT_TOKEN = getenv("BOT_TOKEN", "2122823905:AAH_KW0N3qNw_hmUa5BkfKM-vVQ3YXfzsHc")
SESSION_STRING = getenv("SESSION_STRING", "AQBdnJyoJaaWuRKMjiJxzvdJmp5DvoEtQT8g_ipfap1fjc0RPEvsAdQXChApz94tiDhh0RbGK4Fta3MsWpyqTxeN-ZN54IKoT7ueaEK2EGAv2-rTAt_LgOveKQWnTxlAOVSvs3o5NMzKYfPDymN_8wUX3OYVC6J-G9LyKVf80Pk2OEipRu7xk8sJq3MQomNkm9eWkUxLDxmV-EHoLunZpOlGQCAh3kW69TfNcsdtW8NIQ-wRBMOq3NqRvYapB6UURkPNJctfIjc_vxgok0drQND5W6OFAVNtE_UwtZcQ1Y8uEd8rv-WJBTisSp_N0FtwObx6aCIDpi1_i9ETm6Ymp4yFcyaahgA")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "koliXsupportchat)
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "koliXsupport)
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "ANISH07Bot")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
REPLY_MESSAGE = getenv("REPLY_MESSAGE", "")
if not REPLY_MESSAGE:
    REPLY_MESSAGE = None
else:
    REPLY_MESSAGE = REPLY_MESSAGE
