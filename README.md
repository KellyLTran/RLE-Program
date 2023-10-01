# RLE-Program

Gameplay Description
Each game begins with the player being dealt a card, and the player must get as close to 21 without exceeding.
They can choose to get another card (hit) or keep their current cards (stand).
The dealer's objective is to surpass the player's hand without exceeding 21.
The winner is determined at the game's conclusion based on proximity to 21. The game keeps track of wins over successive rounds.

Project Structure
The game initializes by printing "START GAME #1" and auto-dealing the player's first card.
Cards are represented by numbers: 1 (ACE!), 2-10 (face values), 11 (JACK!), 12 (QUEEN!), and 13 (KING!). 
Face cards are valued at 10, and Aces are valued at 1.
A menu guides player actions: Get another card, Hold hand, Print statistics, and Exit.
The game tracks statistics, including total games, player wins, dealer wins, and ties. These stats are presented upon player request.

Credits
The UF CISE Department provided the console_gfx.py file and the objectives for this project to complete.
