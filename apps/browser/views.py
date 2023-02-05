import os

from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.types import AuthScope
from apps.twitchc.twitch_util import TwitchUserAuthenticator

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
	c = 0
	clips = []
	try:
		async for i in twitch.get_clips(None, "489635", first=5):
			c += 1
			clips.append(i.to_dict())
			if c >= 20:
				break
		return clips
	except Exception as e:
		print(e)
		raise e

async def get_games(twitch, name: str = "Ark"):
	try:
		async for i in twitch.get_games(None, names=[name,]):
			print(i)
			print(i.to_dict())

		clips = []
		return clips
	except Exception as e:
		print(e)
		raise e