from mb_base1.db import BaseDB
from mb_commons.mongo import MongoCollection
from pymongo.database import Database

from app.models import Data


class DB(BaseDB):
    def __init__(self, database: Database):
        super().__init__(database)
        self.data: MongoCollection[Data] = Data.init_collection(database)
