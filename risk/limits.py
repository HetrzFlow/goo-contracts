"""Risk limits for the arb engine."""
class RiskLimits:
    def __init__(self, max_position=10_000, max_single_leg=2_000):
        self.max_position = max_position
        self.max_single_leg = max_single_leg

    def allow(self, leg_size: float, current: float) -> bool:
        return leg_size <= self.max_single_leg and current + leg_size <= self.max_position
