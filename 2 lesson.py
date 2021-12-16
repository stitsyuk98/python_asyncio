"""
асинхренненький скрипт
"""

import time
import asyncio

async def waiter() -> None: # async - делает функцию корутиной
    task1 = asyncio.create_task(cook('Past', 8))
    task2 = asyncio.create_task(cook('Ceaser', 3))
    task3 = asyncio.create_task(cook('Lamb Chops', 16))
    # теперь есть 3 корутины, можно их запустить

    await task1
    await task2
    await task3
    # теперь это работает асинхронно

async def cook(order: str, time_to_prepare: int) -> None:
    print(f'Getting {order} order')
    await asyncio.sleep(time_to_prepare)
    print(order, 'ready')

# if __name__ == '__main__':
#     waiter()

asyncio.run(waiter())

