class Computer:
    def __init__(self, psu, cpu, mem, gpu, hard_drive):
        self.psu = psu
        self.cpu = cpu
        self.mem = mem
        self.gpu = gpu
        self.hard_drive = hard_drive

    def display_info(self):
        print("Computer Information")
        print("CPU Model:", self.cpu)
        print("Memory Model:", self.mem)
        print("GPU Model:", self.gpu)
        print("Hard Drive:", self.hard_drive)

    def upgrade_mem(self, additional_mem):
        print("Upgrade Memory")
        if additional_mem > 0:
            self.mem += additional_mem
            print("Your RAM memory was upgraded to", additional_mem, "GB! Now your RAM is", self.mem, 'GB!')
        else:
            print('Invalid memory value!')
