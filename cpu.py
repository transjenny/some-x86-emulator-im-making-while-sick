import memory
class CPU:

    cpu_memory_address = 0x00
    Bootsector = 0
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

    def Get_RM_Registors(self,mod,rm):
        output = ""
        if(mod != 3):
            if(rm == 0):
                output = 'BX,' + 'SI'
                
            elif(rm ==1):
                output = 'BX,' + 'DI'
                
            elif(rm == 2):
                output = 'BP,' +'SI'
                
            elif(rm == 3):
                output = 'BP,'+'DI'
                
            elif(rm == 4):
                output = 'SI'
                
            elif(rm == 5):
                output = 'DI'
                
            elif(rm == 6):
                output = 'BP'
            elif(rm == 7):
                output = 'BX'
        else:
                if(rm == 0):
                    output = 'EAX'
                elif(rm == 1):
                    output = 'ECX'
                elif(rm == 2):
                    output = 'EDX'
                elif(rm == 3):
                    output = 'EBX'
                elif(rm == 4):
                    output = 'ESP'
                elif (rm == 5):
                    output = 'EBP'
                elif(rm == 6):
                    output = 'ESI'
                elif(rm == 7):
                    output = 'EDI'
        return (output)

    def Run_ModRm(self,byte, decoder):
            
            rm, mod = decoder.Decode_ModRm_rm(byte,self.Bootsector,self)
            reg = decoder.Decode_registers(byte)
            return (rm, mod, reg)

    def run_opcode(self,memory: bytearray, opcode, opsize: int, displacement, decoding: classmethod):
        current_fullopsize = opsize
        decoder = decoding.Decoder() 
        if(opcode == "jmp"):
            address = memory.memory[self.cpu_memory_address+opsize:self.cpu_memory_address+opsize+1][0] # unknown if working right
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
            current_fullopsize +=1
            mod_byte = memory.memory[self.cpu_memory_address + current_fullopsize]
            rm, mod, reg = self.Run_ModRm(mod_byte,decoder)
            rm_REG = self.Get_RM_Registors(mod,rm)
            if(reg != ""):
                self.CPU_registers[reg] = self.CPU_registers[rm_REG.split(',')[0]] & self.CPU_registers[reg] # run the and bitwise and store back in the first registor
            current_fullopsize +=1
            self.cpu_memory_address += current_fullopsize


    def __init__(self, Bootsector) -> None:
        self.Bootsector = Bootsector
if __name__ == "__main__":
    print("cant run from cpu starting main")
    import main