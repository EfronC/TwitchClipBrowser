import os

from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.types import AuthScope
from apps.twitch_utils.utils import *

async def get_users(twitch, username: str = ""):
	limit = 20
	c = 0
	try:
		async for i in twitch.get_users(None, ["alfa",]):
			c += 1
			print(i.to_dict())
			if c >= limit:
				break
		return False
	except Exception as e:
		print(e)
		raise e


async def get_clips(twitch, broadcaster_id=None, game_id=None):
	try:
		clips = await loop_agen(twitch.get_clips(None, "489635", first=5))
		if clips:
			return clips
		else:
			raise Exception("Fetching Failed")
	except Exception as e:
		print(e)
		raise e

async def get_games(twitch, name: str = "Ark"):
	try:
		games = await loop_agen(twitch.search_categories(query=name))
		if games:
			return games
		else:
			raise Exception("Fetching Failed")
	except Exception as e:
		print(e)
		raise e