from datetime import datetime, timedelta
from battery import Battery

class NubbinBattery(Battery):
    def __init__(self, last_service_date):
        super().__init__(last_service_date)
        self.current_date = datetime.today().date()

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        return service_threshold_date < self.current_date