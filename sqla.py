from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData

engine = create_engine('sqlite:///sqladb.db', echo=True)
metadata = MetaData()

prispevky = Table("prispevky", metadata,
                  Column('id', String, primary_key=True),
                  Column('title', String),
                  Column('targetURL', String),
                  Column('redditURL', String),
                  Column('score', Integer)
                  )

#metadata.create_all(engine)
#conn = engine.connect()
#ins = prispevky.insert().values(id='x01', targetURL='https://test',
                                # redditURL='https://test2', score=5)
#conn.execute(ins)
