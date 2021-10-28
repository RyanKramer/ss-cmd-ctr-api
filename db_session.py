from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import yaml

with open("config.yml", "r") as yml_file:
    cfg = yaml.load(yml_file, Loader=yaml.FullLoader)

Base = declarative_base()

engine = create_engine(f'oracle://{cfg["database"]["username"]}:{cfg["database"]["password"]}@{cfg["database"]["host"]}:{cfg["database"]["port"]}/{cfg["database"]["sid"]}')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
dbSession = DBSession()
dbSession.autoflush = True