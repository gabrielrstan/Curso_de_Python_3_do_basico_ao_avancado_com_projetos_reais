from log import LogPrintMixin, LogFileMixin


class Electronic:
    def __init__(self, name):
        self.name = name
        self._turn_on = False

    def turn_on(self):
        if not self._turn_on:
            self._turn_on = True

    def turn_off(self):
        if self._turn_on:
            self.turn_on = False


class Smartphone(Electronic, LogFileMixin):
    def turn_on(self):
        super().turn_on()
        if self._turn_on:
            msg = f'{self.name} is on'
            self.log_success(msg)

    def turn_off(self):
        super().turn_off()
        if not self._turn_on:
            msg = f'{self.name} is off'
            self.log_error(msg)
