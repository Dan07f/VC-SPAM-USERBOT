# FILES BELONGS TO @THEDEADLYBOTS 

import os
from dotenv import load_dotenv

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("API_ID", "11727095"))
API_HASH = os.getenv("API_HASH", "6f36129da1a6050ee10ece4fa99db6f0")
SESSION = os.getenv("SESSION", "BAB71LKSyEFrRRI0ok3Og1EeIIcQqGNL1V8zWqY_ro5uP3QZcGouvguKUcDGLKxaRztBoP6OuWIMF3LwAIBqUNhXVPmxSqcmr2xFcYrJ-vEKqLc3eD8t-AxuSkNq8sljjEI_2yvBm-ImaUikZij9WZDY5fL1nrIJ6ux4yzzWs_x3fgwamjQxcqjctv-uvTWnW4oZK0C-gZQSAL_IHxo42m0UFp7b6NElYqhu_NeHbqTxDWDHxsdeFUqOgNjqbSf48CYDRC4M8iMMhR-0iJmIcoGKrb1ZXmKpg3qhbTAyYPU_EpSRsrydjMqzFMGYiKaqYralzDa6Xfi4ccrrwYkOnN_iAAAAATyYFZ4A")
OWNER = os.getenv("OWNER", "ur_pati")
SUPPORT = os.getenv("SUPPORT", "rocks_fighters")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", "5522433934 5522433934").split()))
