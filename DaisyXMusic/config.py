# DAISYXMUSIC- Telegram bot project
# Copyright (C) 2021  Roj Serbest
# Copyright (C) 2021  Inuka Asith
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# Modified by Inukaasith

import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = "AQBR47f1Yt9jz5qdU1aDsFW9f3ke3I4eTlKuHSrVodZpL3b_P0PhYxyMjhP7m3gyDmNjiKahMbP7vIEBRlbyNIg4q5TKfriBgoQBwo6EISlqc4U4F5SNh8xnEaxH1mrUQWwnE5bkYdGeXTET2NHnfEgnxaPN6HA1RUY3ISW9bApb78hzHK3R0IJXIJTkaqN5kzNhOy-v-ClN33_dgfS5jYXhQaP6os9VmAWJYKPHaokqjr5NJFs625YqTXev-igo0IAQ5CeMd2HtJsMxFGTBt03FOXjW93f3Ac_uWHyouhBT0bhMDJitSgjbWjp4hbfLcgEiNeEIZEUr8p1dAjV6maE0b3ZeAwA"
BOT_TOKEN = "1762083152:AAHs34jX5iNjfD5_UAX3rvKP2XErKiBRcgE"
BOT_NAME = "Yato"
UPDATES_CHANNEL = "YatoUpdates"
BG_IMAGE = "https://telegra.ph/Inline-yato-07-31"
admins = {}
API_ID = 6062531
API_HASH = "83423435383d38a2edd08211d1814c25"
BOT_USERNAME = "Calamity_Robot"
ASSISTANT_NAME = "Yato_VC"
SUPPORT_GROUP = "Yato_Support"
PROJECT_NAME = "Yato Music"
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/teamdaisyx/daisyxmusic")
DURATION_LIMIT = 10
ARQ_API_KEY = "GGHHWC-BIUTPW-EVCGOJ-QDFQEU-ARQ"
PMPERMIT = "ENABLE"
LOG_GRP = -1001594229801
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = 1870028291, 1934004579
