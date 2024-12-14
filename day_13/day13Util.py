from myMaths import *

from typing import List

class ClawMachine:
    BUTTON_A_PRICE: int = 3
    BUTTON_B_PRICE: int = 1
    
    def __init__(self, button_A_movement: Vector2i = None, button_B_movement: Vector2i = None, prize_position: Vector2i = None) ->  None:
        self.claw_position: Vector2i = Vector2i.ZERO
        
        self.button_A_movement: Vector2i = button_A_movement
        self.button_B_movement: Vector2i = button_B_movement
        
        self.prize_position: Vector2i = prize_position
        
    
    def __str__(self) -> str:
        button_A_line: str = f"Button A: X{get_signed_value_string(self.button_A_movement.x)}, Y{get_signed_value_string(self.button_A_movement.y)}"
        button_B_line: str = f""f"Button B: X{get_signed_value_string(self.button_B_movement.x)}, Y{get_signed_value_string(self.button_B_movement.y)}"
        prize_line: str = f"Prize: X={self.prize_position.x}, Y={self.prize_position.y}" # Always positive
        return f"{button_A_line} \n{button_B_line} \n{prize_line}"
    
    def set_button_A_movement(self, button_A_movement: Vector2i) -> None:
        self.button_A_movement = button_A_movement
    
    def set_button_B_movement(self, button_B_movement: Vector2i) -> None:
        self.button_B_movement = button_B_movement
    
    def set_prize_position(self, prize_position: Vector2i) -> None:
        self.prize_position = prize_position
    
    
    # PART 1 (brute-force)
    def get_minimum_cost(self) -> int:
        minimum_cost: int = 999999 # Start at cost above our max cost to replace with 0 later
        
        for button_presses_A in range(0, 100+1):
            for button_presses_B in range(0, 100+1):
                cost = button_presses_A + button_presses_B
                if cost > 100:
                    break
                
                resulting_claw_position = \
                    self.button_A_movement * button_presses_A + \
                    self.button_B_movement * button_presses_B
                print(resulting_claw_position.x)
                if resulting_claw_position.x == 8400: 
                    print(f"With {button_presses_A} A Presses and {button_presses_B} B Presses: ")
                    print(f"{resulting_claw_position} was reached")
                if resulting_claw_position != self.prize_position:
                    continue
                
                minimum_cost = min(cost, minimum_cost)
        
        return 0 if minimum_cost > 100 else minimum_cost