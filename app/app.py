from mb_base1.app import BaseApp

from app.config import AppConfig, DConfigSettings, DValueSettings
from app.db import DB
from app.services.base import AppServiceParams
from app.services.data_service import DataService


class App(BaseApp):
    def __init__(self):
        super().__init__(AppConfig(), DConfigSettings(), DValueSettings())
        self.db: DB = DB(self.database)
        self.data_service = DataService(self.base_params)

        self.scheduler.add_job(self.data_service.generate_data, 600)

    @property
    def base_params(self):
        return AppServiceParams(super().base_params, self.db)
