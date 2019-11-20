class Gene:
    def __init__(self, value: bool):
        """
        Gene can have either a value 1 (feature is included) or 0 (feature is excluded).
        """
        self._value = value
