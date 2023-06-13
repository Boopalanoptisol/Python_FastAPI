from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



SQLALCHAMEY_DATABASE_URL = 'sqlite:///./blog.db'
engine = create_engine(SQLALCHAMEY_DATABASE_URL,connect_args={"check_same_thread":False})
# engine = create_engine('sqlite:///./blog.db',echo=True )


SessionLocal = sessionmaker(bind = engine,autocommit=False,autoflush=False)

Base = declarative_base()