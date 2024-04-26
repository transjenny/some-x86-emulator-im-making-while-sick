import memory
class CPU:

    cpu_memory_address = 0x00

    CPU_registers = {
        'EAX': 0x00,
        'ECX': 0x00,
        'EDX': 0x00,
        'EBX': 0x00,
        'ESP': 0x00,
        'EBP': 0x00,
        'ESI': 0x00,
        'EDI': 0x00,
        'BX': 0x00,
        'SI': 0x00,
        'DI': 0x00,
        'BP':0x00,

    }

    def run_opcode(self,memory: bytearray, opcode, opsize: int, displacement, decoding):
        current_fullopsize = opsize
        decoder = decoding.Decoder() 
        if(opcode == "jmp"):
            address = memory.memory[self.cpu_memory_address+opsize:self.cpu_memory_address+opsize+1][0]
            current_fullopsize +=1
            self.cpu_memory_address = address
            print(f"moved to memory address {hex(address)}")
        elif(opcode == "add"):
            registor = decoder.Decode_registers(memory.memory[self.cpu_memory_address+opsize+1:self.cpu_memory_address + opsize + 2])
            current_fullopsize +=1
            address = decoder.Decode_SIB(memory.memory[self.cpu_memory_address+opsize+2:self.cpu_memory_address + opsize + 3], displacement)
            current_fullopsize +=1
            print(f"adding {memory.memory[address]} and {registor}")
            self.CPU_registers[registor] += memory.memory[address]
            self.cpu_memory_address += current_fullopsize
        elif(opcode == "and"):
            pass

    def __init__(self) -> None:
        pass