from models.zone import Zone


class ZoneManager:

    def __init__(self):

        self.promotion = Zone("Promotion")
        self.new_machine = Zone("NewMachine")
        self.normal = Zone("Normal")

    def get_zone(self, cell_id: str):

        # Promotion Zone
        if cell_id.startswith("R12") or \
           cell_id.startswith("S12") or \
           cell_id.startswith("T12") or \
           cell_id.startswith("U12") or \
           cell_id.startswith("V12") or \
           cell_id.startswith("W12") or \
           cell_id.startswith("X12") or \
           cell_id.startswith("Y12") or \
           cell_id.startswith("Z12") or \
           cell_id.startswith("AA12") or \
           cell_id.startswith("AB12") or \
           cell_id.startswith("AC12"):

            return self.promotion

        # New Machine Zone
        if cell_id in (
            "M15","M16","M17","M18",
            "M19","M20","M21","M22"
        ):

            return self.new_machine

        return self.normal