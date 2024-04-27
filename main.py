import display, cpu, memory, decoding, sys, time

MEMORY_MB = 64
CPU_SEED = 5 # number of cycles per seccond



print("This is still an expriment so if stuff doesnt work dont be surprized")


BOOT_DEVICE = "FD13BOOT.img"

print(f"Loading Boot Device {BOOT_DEVICE}")


BOOTIMG = bytes(open(f"boot_drives/{BOOT_DEVICE}",'rb').read())

BootSector = BOOTIMG[:512]



print("Loaded Boot Device, starting emuasion")

cpu = cpu.CPU(BootSector) 
memory = memory.memory(MEMORY_MB)

for i in range(len(BootSector)):
    memory.memory[i] = BootSector[i]

decoder = decoding.Decoder() 

while True:
    print(f"Starting next cpu cycle at {hex(cpu.cpu_memory_address)}")
        
    opsize, opcode = decoder.Decode_opcode(memory.memory[cpu.cpu_memory_address:cpu.cpu_memory_address+ 8*3])
    
    displacement, rm = decoder.Decode_ModRm_rm(memory.memory[cpu.cpu_memory_address+opsize], BootSector,cpu)

    cpu.run_opcode(memory,opcode,opsize, displacement,decoding)
    
    
    print("next cycle")
    time.sleep(CPU_SEED) # tmp high number
        
