import asyncio
from subprocess import Popen, PIPE

tgt = ['google.com', 'yahoo.com']
async def test(ip):
    ping = asyncio.create_subprocess_exec(['ping', '-c', '5', ip], stdout=PIPE,
                                                               stderr=PIPE)
    out, err = ping.communicate()
    await asyncio.sleep(10)
    return i, out

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.call_later(2, loop.stop)
    tasks = [loop.create_task(test(ip)) for ip in tgt]
    try:
        loop.run_until_complete(
                asyncio.wait(tasks)
                )
        for task in tasks:
            prnint(*task.result())
    finally:
        loop.close()
