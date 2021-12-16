"""
Асинхронка но пока без асинхронки
просто запустили корутины
"""

import time
import asyncio

async def waiter() -> None: # async - делает функцию корутиной
    await cook('Past', 8)
    await cook('Ceaser', 3)
    await cook('Lamb Chops', 16)

async def cook(order: str, time_to_prepare: int) -> None:
    print(f'Getting {order} order')
    await asyncio.sleep(time_to_prepare)
    print(order, 'ready')

# if __name__ == '__main__':
#     waiter()

asyncio.run(waiter())

