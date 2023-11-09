# Snakes and ladders game 🐍🪜

Python package to play snake and ladders in the console.

## Setup ⚙️

   ```console
   poetry install --with=dev
   ```

## Play the game

   ```console
   python3 main.py
   ```
When playing the game, the board will be printed in every movement.  
The initial board is:

+----+----+----+----+----+  
| 21 | S4 | 23 | S3 | 25 |  
+----+----+----+----+----+  
| S4 | S2 | L3 | L2 | S3 |  
+----+----+----+----+----+  
| L1 | L4 | 13 | S1 | 15 |  
+----+----+----+----+----+  
| L4 | L3 | S2 | O7 | L2 |  
+----+----+----+----+----+  
| 01 | 02 | L1 | S1 | O5 |  
+----+----+----+----+----+  

Where:
- Sn corresponds to a snake head and tail cells, being n the id of the snake.
- Ln correspond to a start and end cells of a ladder, being n the id of the Ladder.
- XX the the current position of the player.

## Tests
[![Tests](https://github.com/alejandropr5/snakes-ladders-game/actions/workflows/test.yaml/badge.svg)](https://github.com/alejandropr5/snakes-ladders-game/actions/workflows/test.yaml)

   ```console
   pytest
   ```

## Apex implementation
In the [apex_salesforce](apex_salesforce) folder is the Apex implementation and tests.
