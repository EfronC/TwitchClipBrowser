from twitchAPI.oauth import UserAuthenticator
from typing import Optional, Callable
import webbrowser

class TwitchUserAuthenticator(UserAuthenticator):

	async def authorize(self, browser_name: Optional[str] = None, browser_new: int = 2):
		try:
			browser = webbrowser.get(browser_name)
			browser.open(self._UserAuthenticator__build_auth_url(), new=browser_new)
			#sleep(0.01)
			return True
		except Exception as e:
			print(e)
			raise e
