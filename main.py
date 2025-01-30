from computer import Computer

if __name__ == "__main__":
    computers = []

    num = int(input("Enter number of computers: "))

    for i in range(num):
        print(f"Enter details of the computer №{i+1}")
        cpu = input("CPU Name: ")
        mem = int(input("Memory Size(GB): "))
        gpu = input("GPU Name: ")
        hard_drive = input("Hard Drive Name: ")
        psu = input("PSU Name: ")

        comp = Computer(psu, cpu, mem, gpu, hard_drive)
        computers.append(comp)

        print(f"Computer information: {i+1}")
        for i, comp in enumerate(computers, 1):
            print(f"Computer {i}:")
            comp.display_info()

    while True:
        upgrade_choice = input("Would you like to upgrade memory for a computer? (yes/no)\n")
        if upgrade_choice == "yes":
            comp_num = int(input(f"Enter number of computer (1-{num}): ")) - 1
            if 0 <= comp_num < num:
                additional_mem = int(input("Enter additional memory you would like to add (GB): "))
                computers[comp_num].upgrade_mem(additional_mem)
            else:
                print("Invalid computer number!")
        elif upgrade_choice == "no":
            break
        else:
            print("Please enter a valid option 'yes' or 'no'!")