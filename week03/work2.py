#!/usr/bin/python3
from datetime import datetime, date

from sqlalchemy import Column, Integer, String, DateTime, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User_table(Base):
    __tablename__ = 'userpy'
    id = Column(Integer(), primary_key=True)
    name = Column(String(50))
    age = Column(Integer())
    birthday = Column(Date())
    sex = Column(String(2))
    degree = Column(String(20))
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)

    def __repr__(self):
        return f"User_table(id= {self.id}, name={self.name},updated_on={self.updated_on})"


# 实例一个引擎
dburl = "mysql+pymysql://testuser:testpass@192.168.56.50:3306/testdb?charset=utf8mb4"
engine = create_engine(dburl, echo=True, encoding="utf-8")

# create table
Base.metadata.create_all(engine)

# create session
SessionClass = sessionmaker(bind=engine)
session = SessionClass()

# insert 3 records
user1 = User_table(name='Jok', age=25, birthday=date(
    1995, 8, 1), sex='M', degree='Master')
user2 = User_table(name='Tomi', age=35, birthday=date(
    1986, 10, 10), sex='M', degree='Master')
user3 = User_table(name='Mike', age=40, birthday=date(
    1981, 4, 1), sex='F', degree='Master')
session.add(user1)
session.add(user2)
session.add(user3)
session.flush()
session.commit()

# Query
#result = session.query(User_table).all()
result = session.query(User_table)
for result in session.query(User_table):
    print(result)
