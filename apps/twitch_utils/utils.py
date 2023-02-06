from typing import AsyncGenerator

async def loop_agen(agen:AsyncGenerator, limit:int = 20):
	try:
		data = []
		c = 0
		async for i in agen:
			c += 1
			data.append(i.to_dict())

			if c >= limit:
				break
		return data
	except Exception as e:
		print(e)
		return False