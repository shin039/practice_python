# 参考URL: https://zenn.dev/plhr7/articles/201572f26721ac
# ------------------------------------------------------------------------------
# Import
# ------------------------------------------------------------------------------
import urllib.request
from typing import Sequence
import threading
import queue

import asyncio

# ------------------------------------------------------------------------------
# Function
# ------------------------------------------------------------------------------

# single
def health_check(url: str):
  try:
    response = urllib.request.urlopen(url)
    return response.status
  except urllib.error.HTTPError as e:
    return e.code

# Sequential
def health_checks(urls: Sequence[str]):
  return [health_check(url) for url in urls]

# - - - - - - - - - - - - - - - - - - - - 
# Thread
# - - - - - - - - - - - - - - - - - - - - 

# Thread (No Return...)
def health_check_threads(urls: Sequence[str]):
  threads = []
  for url in urls:
    # スレッド作成
    t = threading.Thread(target=health_check, args=(url,))
    # スレッドスタート
    t.start()
    # スレッドをリストに追加
    threads.append(t)
  # スレッドが全て終わるのを待って、終了を検知する
  for t in threads:
    t.join()

# Queue
def health_check_queue(url: str, i: int, q: queue.Queue):
  try:
    response = urllib.request.urlopen(url)
    q.put((i, response.code))
  except urllib.error.HTTPError as e:
    q.put((i, e.code))

# Thread with Queue
def health_check_threads_with_queue(urls: Sequence[str]):
  q = queue.Queue()
  threads = []

  for i, url in enumerate(urls):
    t = threading.Thread(target=health_check_queue, args=(url, i, q))
    t.start()
    threads.append(t)
  for t in threads:
    t.join()
  return [x[1] for x in sorted(list(q.queue), key=lambda x: x[0])]

# - - - - - - - - - - - - - - - - - - - - 
# asyncio
# - - - - - - - - - - - - - - - - - - - - 
async def health_check_async(url: str):
  # NOTE: こちらの実行では、同期処理になってしまう。
  # return health_check(url)
  loop = asyncio.get_event_loop()
  return await loop.run_in_executor(None, health_check, url)

async def health_check_asyncs(urls: Sequence[str]):
  return await asyncio.gather(*[health_check_async(url) for url in urls])

# ------------------------------------------------------------------------------
# Main
# ------------------------------------------------------------------------------

target = [
  'https://google.com',
  'https://google.com/detarame_sonzaishinai_1',
  'https://google.com/detarame_sonzaishinai_2',
  'https://google.com/detarame_sonzaishinai_3',
  'https://google.com/detarame_sonzaishinai_4',
  'https://google.com/detarame_sonzaishinai_5',
  'https://google.com/detarame_sonzaishinai_6',
  'https://google.com/detarame_sonzaishinai_7',
  'https://google.com/detarame_sonzaishinai_8',
  'https://google.com/detarame_sonzaishinai_9',
  'https://google.com/detarame_sonzaishinai_10',
]

# - Sequencial
# print(health_checks(target))

# - Thread
# print(health_check_threads(target))
# print(health_check_threads_with_queue(target))

# - asyncio
print(asyncio.run(health_check_asyncs(target)))

# loop = asyncio.get_event_loop()
# print(loop.run_until_complete(health_check_asyncs(target)))

