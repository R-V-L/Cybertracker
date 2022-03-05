import asyncio
import aiohttp
import platform

async def obtener_urls(urls):
    results = []
    async with aiohttp.ClientSession() as session:
        tasks = [session.get(url, ssl=False) for url in urls]
        responses = await asyncio.gather(*tasks)
        for response in responses:
            results.append(await response.text())
    return results

def get_response(urls):
    # Workaround for Windows
    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    return asyncio.run(obtener_urls(urls))

if __name__ == "__main__":
    urls2 = []
    url_base = "https://pokeapi.co/api/v2/pokemon/"
    for i in range(1, 2):
        urls2.append(url_base + str(i))
    print(get_response(urls2))