from computer import Computer

if __name__ == "__main__":
    computers = []

    num = int(input("Enter number of computers: "))

    for i in range(num):
        print(f"Enter details of the computer №{i+1}")
        cpu = input("CPU Name: ")
        mem = input("Memory Name: ")
        gpu = input("GPU Name: ")
        hard_drive = input("Hard Drive Name: ")
        psu = input("PSU Name: ")

        comp = Computer(cpu, mem, gpu, hard_drive, psu)
        computers.append(comp)

        print(f"Computer information: {i+1}")
        for i, comp in enumerate(computers, 1):
            print(f"Computer {i}:")
            comp.display_info()