from sqlalchemy import create_engine, MetaData


# engine = create_engine("sqlite///name.db")
engine = create_engine("mysql+pymysql://root@localhost:3306/test")
meta = MetaData()
conn = engine.connect()