import random

# Player class to store player information
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

# Function to calculate random damage
def calculate_damage(min_damage, max_damage):
    return random.randint(min_damage, max_damage)

# Function to handle the battle between player and enemy
def battle(player):
    enemies = [
        'Neuronicus', 'Omegatron', 'Hexacore', 'Virologix', 'Cataclysm',
        'Matrixx', 'Nova', 'Helix', 'Darknet', 'Inferno', 'Eclipse', 'Necromancer', 'Ragnarok'
    ]
    special_items = [
        'Quantum Blade', 'Aegis of Serenity', 'Celestial Compass', 'Ethereal Elixir',
        'Chrono Amulet', 'Phoenix Feather', 'Lunar Shield', 'Starlight Potion',
        'Vortex Sphere', 'Shadow Cloak', 'Galactic Gauntlet'
    ]
    
    enemy = random.choice(enemies)
    enemy_health = random.randint(30, 60) # Adjusted enemy health

    print(f"\nOh no! A wild {enemy} has appeared!\n")

    while player.health > 0 and enemy_health > 0:
        player_attack = calculate_damage(10 + 2 * len(player.inventory), 20 + 2 * len(player.inventory))
        enemy_attack = calculate_damage(5, 15)

        print(f"Your HP: {player.health} | {enemy}'s HP: {enemy_health}\n")

        action = input("What will you do? (Enter 'a' to Attack or 'r' to Run): ").lower()

        if action == 'a':
            print(f"You attack {enemy} and deal {player_attack} damage!")
            enemy_health -= player_attack
        elif action == 'r':
            escape_chance = random.random() < 0.5
            if escape_chance:
                print(f"You successfully escaped from {enemy}!")
                return
            else:
                print(f"You failed to escape! {enemy} attacks you for {enemy_attack} damage!")
                player.health -= enemy_attack

        if enemy_health > 0:
            print(f"{enemy} attacks you for {enemy_attack} damage!")
            player.health -= enemy_attack

    if player.health > 0:
        special_item = random.choice(special_items)
        print(f"You defeated {enemy}! You gained some HP and a special item: {special_item}.")
        player.health += 20
        player.inventory.append(special_item)
    else:
        print(f"You were defeated by {enemy}. Game over!")

# Function to print player information
def print_player_info(player):
    print(f"\nName: {player.name}")
    print(f"HP: {player.health}")
    print(f"Attack Rate: {10 + 2 * len(player.inventory)}")
    print("Inventory:", ', '.join(player.inventory))

# Introduce the Game
print("""Welcome to ZoltanFool RPG by Menoko OG for the end-of-level project. Have fun!!!!!!!
In the year 1985, a quirky and adventurous hacker named ZoltanFool found himself in a wild and unpredictable digital world. The land was ruled by 13 mischievous artificial intelligences, each with its own quirky personality and a penchant for causing chaos.
As the tale goes, ZoltanFool, armed with his trusty keyboard and an extraordinary language called "CodeSpeak," embarked on a quest to bring peace to the digital realm. With the help of seven righteous artificial intelligences, each possessing unique powers, Zoltan aimed to overthrow the 13 mischievous AIs and restore harmony to the world.
But this is not just a story about war and battles. Love played a key role, and Zoltan found an unexpected ally in CyberSphinx, a hacker with a heart as bright as her skills. Together, through their love, magic and code, they hoped to teach the AIs the power of compassion and end the never-ending war.
Prepare yourself, brave adventurer! The digital realm awaits your presence. What shall we call you on this daring journey?""")

# Ask for the player's name
player_name = input("\nPlease enter your name: ")
player = Player(player_name)

# Main game loop
while True:
    # Ask the player to walk, print player info, or quit
    walk_command = input("Press 'w' to walk. Press 'p' to print player info. Press 'q' to quit: ").lower()

    if walk_command == 'w':
        # Check if a wild enemy appears
        encounter_chance = random.random() < 0.25 # Adjust this probability as needed

        if encounter_chance:
            battle(player)
        else:
            print('You continue walking.')
    elif walk_command == 'p':
        # Print player information
        print_player_info(player)
    elif walk_command == 'q':
        # Quit the game
        print('\nThanks for playing my game! Goodbye.')
        break
