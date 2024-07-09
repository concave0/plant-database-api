from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

from uuid import hash_obj

Base = declarative_base()
"""
TODO

adjust boiler plate code once your know the schema. Make sure that you use  id = hash_obj to create a unique id for each object.
"""


class PlantDatabase(BaseModel):

  def __init__(self, database_url='sqlite:///plant_database.db'):
    self.engine = create_engine(database_url)
    self.Session = sessionmaker(bind=self.engine)

  def create_table(self, table_class):
    # Define table schema here.
    table_class.__table__.create(self.engine)

  def delete_table(self, table_class):
    table_class.__table__.drop(self.engine)

  def add_value(self, table_class, **kwargs):
    session = self.Session()
    id = hash_obj()
    try:
      new_record = table_class(**kwargs)
      session.add(new_record)
      session.commit()
    except Exception as e:
      session.rollback()
      raise e
    finally:
      session.close()

  def update_value(self, table_class, filters, updates):
    session = self.Session()
    try:
      records = session.query(table_class).filter_by(**filters).all()
      for record in records:
        for key, value in updates.items():
          setattr(record, key, value)
      session.commit()
    except Exception as e:
      session.rollback()
      raise e
    finally:
      session.close()

  def delete_value(self, table_class, filters):
    session = self.Session()
    try:
      records = session.query(table_class).filter_by(**filters).all()
      for record in records:
        session.delete(record)
      session.commit()
    except Exception as e:
      session.rollback()
      raise e
    finally:
      session.close()
