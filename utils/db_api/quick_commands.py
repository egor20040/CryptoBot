from asyncpg import UniqueViolationError

from utils.db_api.db_gino import User


async def add_user(id: int, name: str, chat_id: int, btc: str = None, eth: str = None, qiwi: str = None,
                   sol: str = None, language: str = None, currency: str = None):
    try:
        user = User(id=id, name=name, chat_id=chat_id, btc=btc, eth=eth, qiwi=qiwi, sol=sol, language=language,
                    currency=currency)

        await user.create()

    except UniqueViolationError:
        pass


async def select_user(id: int):
    user = await User.query.where(User.id == id).gino.first()
    return user


async def get_currency(id: int):
    user = await User.query.where(User.id == id).gino.first()
    return user.currency


async def update_purse(id, purse, currency):
    user = await User.get(id)
    if currency == "BTC":
        await user.update(btc=purse).apply()
    if currency == "ETH":
        await user.update(eth=purse).apply()
    if currency == "QIWI":
        await user.update(qiwi=purse).apply()
    if currency == "SOL":
        await user.update(sol=purse).apply()
