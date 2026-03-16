class ExposureLimits:

    MAX_OPEN_POSITIONS = 5

    def check_symbol_positions(self, open_positions):

        if open_positions >= self.MAX_OPEN_POSITIONS:
            return False

        return True
