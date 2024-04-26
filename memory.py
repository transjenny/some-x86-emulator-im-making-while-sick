class memory:
    MEMORY_MB = 0
    memory = bytearray(0x00)
    def __init__(self, MEMORY_MB) -> None:
        self.MEMORY_MB = MEMORY_MB
        self.memory = bytearray(MEMORY_MB*1000*1000)

