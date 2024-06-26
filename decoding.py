class Decoder:
    def Decode_ModRm_mod(self,byte, instruction_stream, mod):
        displacement_size = 0
        if mod == 0b01:
            # 8-bit displacement follows the ModR/M byte
            displacement_size = 8
        elif mod == 0b10:
            # 32-bit displacement follows the ModR/M byte
            displacement_size = 32

        # Now, if you want to parse the actual displacement value:
        if displacement_size > 0:
            # Parse the displacement value from the instruction stream
            # (Assuming little-endian byte order for x86 architecture)
            displacement_bytes = instruction_stream[:displacement_size // 8]
            displacement = int.from_bytes(displacement_bytes, byteorder='little', signed=True)
            # Handle the signed extension of the displacement value if necessary
            if displacement_size == 8 and displacement & 0x80:
                # Sign extend for 8-bit displacement
                displacement |= 0xFFFFFF00
        elif mod == 0b00 or mod == 0b11:
            # No displacement
            displacement = 0

        return displacement
    import cpu
    def Decode_ModRm_rm(self,byte, instruction_stream, cpu:cpu.CPU):
        
        rm = byte & 0b00000111
        mod = (byte & 0b11000000) >> 6

        mod_int = mod
        rm_int = rm
        mod_displacment = self.Decode_ModRm_mod(byte, instruction_stream, mod_int)
        
        return (rm_int,mod_displacment)

    def Decode_SIB(self,byte, displacement):
        
        

        base = byte & 0b00000111    # Extract the base register
        index = (byte >> 3) & 0b00000111  # Extract the index register
        scale = (byte >> 6) & 0b00000011  # Extract the scale factor


        memory_address = (2 ** scale) * index + base + displacement
        return memory_address



    def Decode_opcode(self,bytes:bytes):
        bytes_backup = bytes
        opcodes={
            0x00: "add",
            0x01: "add",
            0x02: "add",
            0x03: "add",
            0x04: "add",
            0x05: "add",
            0xA0: "mov",
            0xA1: "mov",
            0xA2: "mov",
            0xA3: "mov",
            0xE9: "jmp",
            0xEB: "jmp",
            0x98: "cbw",
            0x20: "and",
            0x21: "and",
        }
        size_of_opcode = len(bytes)
        old_opcode = 0
        opcode = 0
        for i in range(9999):
            try:
                opcode = int(bytes.hex(), 16)
                old_opcode = opcode # grab after just in case there a error
            except ValueError:
                raise Exception(f"Bytes in opcode list, killing app\nif the opcode is one byte it is:{hex(old_opcode)}\nfor two byte:{hex(int(bytes_backup[:2].hex(), 16))}")
                import sys
                sys.exit()
            if opcode > 0xff:
                bytes = bytes[:size_of_opcode-1]
                size_of_opcode-=1
            elif(opcode not in opcodes):
                bytes = bytes[:size_of_opcode-1]
                size_of_opcode-=1
            else:
                break
        print(f"opcode is {size_of_opcode} bytes big\nopcode is {hex(opcode)} or {opcodes[opcode]}")

        return (size_of_opcode, opcodes[opcode])
                

        




    def Decode_registers(self,bytes):
        byte = bytes & 0b111
        REG = int(byte)
        reg_int = int(REG)
        registers_decoded = ""
        if(reg_int == 0):
            registers_decoded = "EAX"
        elif(reg_int == 1):
            registers_decoded = "ECX"
        elif(reg_int == 2):
            registers_decoded = "EDX"
        elif(reg_int == 3):
            registers_decoded = "EBX"
        elif(reg_int == 4):
            registers_decoded = "EBP"
        elif(reg_int == 5):
            registers_decoded = "ESP"
        elif(reg_int == 6):
            registers_decoded = "ESI"
        elif(reg_int == 7):
            registers_decoded = "EDI"
        else:
            raise Exception(f"This should`nt be possile \n the 3 bit number is {reg_int}")
        return registers_decoded
    

if __name__ == "__main__":
    print("Cant start from decoder starting from main")
    import main