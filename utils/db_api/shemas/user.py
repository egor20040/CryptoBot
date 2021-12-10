from sqlalchemy import BigInteger, Column, String, sql

from utils.db_api.db_gino import TimeBaseModel


class User(TimeBaseModel):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(100))
    chat_id = Column(BigInteger)
    btc = Column(String)
    eth = Column(String)
    qiwi = Column(String)
    sol = Column(String)

    query: sql.Select
