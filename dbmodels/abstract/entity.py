from sqlalchemy import Column, Integer


class Entity:
    id = Column("Id", Integer, primary_key=True)
