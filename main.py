import display, cpu, memory, decoding, sys, time

print("This is still an expriment so if stuff doesnt work dont be surprized")


BOOT_DEVICE = "FD13BOOT.img"

print(f"Loading Boot Device {BOOT_DEVICE}")


BOOTIMG = bytes(open(f"boot_drives/{BOOT_DEVICE}",'rb').read())

BootSector = BOOTIMG[:512]



print("Loaded Boot Device, starting emuasion")

cpu = cpu.CPU()
memory = memory.memory(64)

for i in range(len(BootSector)):
    memory.memory[i] = BootSector[i]

decoder = decoding.Decoder() 

while True:
        
    opsize, opcode = decoder.Decode_opcode(memory.memory[cpu.cpu_memory_address:cpu.cpu_memory_address+ 8*3])
    
    displacement, rm = decoder.Decode_ModRm_rm(memory.memory[cpu.cpu_memory_address+opsize:cpu.cpu_memory_address + opsize + 1], BootSector,cpu)

    cpu.run_opcode(memory,opcode,opsize, displacement,decoding)
    
    
    print("next cycle")
    time.sleep(5)
        
