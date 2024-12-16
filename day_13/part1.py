from day13Util import *

machines: List[ClawMachine] = []

def get_claw_machine(machine_description: str) -> ClawMachine:
    machine: ClawMachine = ClawMachine()
    
    for line in machine_description.split("\n"):
        property_name: str = line.split(": ")[0]
        
        values_sting: List[str] = line.split(": ")[1].strip().split(", ")
        property_value: Vector2i = Vector2i (
            int(values_sting[0].replace('X', '').replace('=', '')),
            int(values_sting[1].replace('Y', '').replace('=', ''))
        )

        match property_name:
            case "Button A":
                machine.set_button_A_movement(property_value)
            case "Button B":
                machine.set_button_B_movement(property_value)
            case "Prize":
                machine.set_prize_position(property_value)
    
    return machine

with open("day_13/input.txt") as file:
    for machine_description in file.read().split("\n\n"):
        machines.append(get_claw_machine(machine_description))

totalCost = 0
for machine in machines:
    print(machine)
    
    cost = machine.get_minimum_cost() # Return 0 if impossible
    totalCost += cost
    
    if cost == 0:
        print("❌ Prize is unobtainable")
    else:
        print(f"✅ Minimum Cost: {cost}")
    print('\n')

print(f"{20*'-'}")
print("Total Cost:", totalCost)