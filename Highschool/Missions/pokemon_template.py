# We are going to create a Pokemon game.
# a spell is a move that a pokemon can cast
# A Pokemon is a character with a name, hp, mp, atk, and type.
# A player is also a character with a name, hp, mp, and atk.
# A player can catch pokemons.
# If the player already has a pokemon of the same type, the player can choose to replace the old pokemon with the new one.
# Otherwise, the player can catch the new pokemon.
# Create a Pokemon class and a Player class which are subclasses of the Char class.


# Your code here
class Spell:
    def __init__(self, name, mp_cost, damage):
        self.name = name
        self.mp_cost = mp_cost
        self.damage = damage
    
    def get_name(self):
        return self.name
    
    def get_mp_cost(self):
        return self.mp_cost
    
    def get_damage(self):
        return self.damage

    def __str__(self):
        return 'Name: {} MP Cost: {} Damage: {}'.format(self.name, self.mp_cost, self.damage)

class Character:
    def __init__(self, name, hp, mp, atk):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.alive = True

    def get_name(self):
        return self.name
    
    def get_hp(self):
        return self.hp
    
    def get_mp(self):
        return self.mp
    
    def get_atk(self):
        return self.atk
    
    def update_hp(self, change):
        self.hp += change

    def update_mp(self, change):
        self.mp += change

    def update_status(self):
        if self.hp <= 0:
            self.alive = False

    def get_status(self):
        return self.alive
    
    def attack(self, target):
        target.update_hp(-self.atk)
        target.update_status()
        if target.get_status() == False:
            return print('{} attacks {}.\n{} is hit, hp changes from {} to {}.\n{} has fainted.'.format(self.name, target.name, target.name, target.hp+self.atk, target.hp, target.name))
        return print('{} attacks {}.\n{} is hit, hp changes from {} to {}'.format(self.name, target.name, target.name, target.hp+self.atk, target.hp))
    
    def __str__(self):
        return 'Name: {} HP: {} MP: {} ATK: {}'.format(self.name, self.hp, self.mp, self.atk)

class Pokemon(Character):
    def __init__(self, name, hp, mp, atk, p_type, spell):
        super().__init__(name, hp, mp, atk)
        self.p_type = p_type
        self.spell = spell

    def get_type(self):
        return self.p_type
    
    def get_spell(self):
        return self.spell
    
    def set_spell(self, new_spell):
        self.spell = new_spell

    def cast_spell(self, target):
        if target.get_status() == False:
            return print('Target is dead')
        
        if self.get_mp() < self.spell.get_mp_cost():
            return print('Not enough MP')

        initial_hp = target.get_hp()
        initial_mp = self.get_mp()

        target.update_hp(-self.spell.get_damage())

        temp = '{} casts {} on {}.'.format(self.get_name(), self.spell.get_name(), target.get_name())

        if target.get_status() == False:
            return print('{temp}\n{target} is hit, hp changes from {initial_hp} to {final_hp}.\n{target} has fainted.\nRemaining MP is {final_mp}'.format(temp=temp, target=target.get_name(), initial_hp=initial_hp, final_hp=target.get_hp(), final_mp=initial_mp-self.spell.get_mp_cost()))
        return print('{temp}\n{target} is hit, hp changes from {initial_hp} to {final_hp}.\nRemaining MP is {final_mp}'.format(temp=temp, target=target.get_name(), initial_hp=initial_hp, final_hp=target.get_hp(), final_mp=initial_mp-self.spell.get_mp_cost()))
    
    def __str__(self):
        return 'Name: {name} HP: {hp} MP: {mp} ATK: {atk} Type: {type} \nSpell details: {spell}'.format(name=self.name, hp=self.hp, mp=self.mp, atk=self.atk, type=self.p_type, spell=self.spell)
    
class Player(Character):
    def __init__(self, name, hp, mp, atk):
        super().__init__(name, hp, mp, atk)
        self.pokemons = []

    def get_pokemons(self):
        return self.pokemons
    
    def display_pokemons(self):
        if len(self.pokemons) == 0:
            return print('{} have not caught any pokemons yet.'.format(self.name))
        print('Here are the pokemons in {}\'s team:'.format(self.name))
        for pokemon in self.pokemons:
            print(pokemon)

    def catch_pokemon(self, pokemon):
        for pok in self.pokemons:
            if pok.get_type() == pokemon.get_type():
                print('{}, you already have:\n{}.\nNow you meet:\n{}'.format(self.name, pok, pokemon))
                choice = input('Would you like to replace the pokemon of the same type? [Y/N]').upper()

                if choice == 'Y':
                    self.pokemons.remove(pok)
                    self.pokemons.append(pokemon)
                    return print('{} have released {}, and caught {}.'.format(self.name, pok.get_name(), pokemon.get_name()))
                elif choice == 'N':
                    return print('You have chose not to catch {}.'.format(pokemon.get_name()))
                else:
                    return print('error, pokemon escaped...')
        self.pokemons.append(pokemon)
        return print('{} have caught {}.'.format(self.name, pokemon.get_name()))


# below are test functions and their expected outputs
# dmg spells (electric, fire, water)
fireball = Spell("Fireball", 12, 25)
fireblast = Spell("Fireblast", 15, 30)
thunderbolt = Spell("Thunderbolt", 10, 20)
frostbolt = Spell("Frostbolt", 8, 16)

# healing spells (grass)
heal = Spell("Heal", 10, -20)


def test_01():
    print("--- Test 01: test cataching different types of pokemons ---")
    player = Player("Ash Ketchum", 100, 100, 20)
    pokemon_01 = Pokemon("Charmander", 50, 60, 18, "Fire", fireball)
    pokemon_02 = Pokemon("Squirtle", 55, 60, 15, "Water", frostbolt)
    pokemon_03 = Pokemon("Bulbasaur", 80, 60, 12, "Grass", heal)
    pokemon_04 = Pokemon("Pikachu", 60, 60, 15, "Electric", thunderbolt)
    pokemon_05 = Pokemon("Ponyta", 60, 60, 18, "Fire", fireblast)

    print(player)

    player.display_pokemons()
    player.catch_pokemon(pokemon_01)
    player.catch_pokemon(pokemon_02)
    player.catch_pokemon(pokemon_03)
    player.catch_pokemon(pokemon_04)
    player.display_pokemons()
    player.catch_pokemon(pokemon_05)
    player.display_pokemons()

    print("--- End of Test 01 ---\n")


test_01()


def test_02():
    print("--- Test 02: test attacking between players and pokemons ---")

    # pokemons with various types and slightly different stats
    pikachu = Pokemon("Pikachu", 120, 100, 10, "Electric", thunderbolt)
    charmander = Pokemon("Charmander", 80, 120, 10, "Fire", fireball)
    squirtle = Pokemon("Squirtle", 100, 90, 10, "Water", frostbolt)
    bulbasaur = Pokemon("Bulbasaur", 120, 100, 10, "Grass", heal)

    # two players
    p1 = Player("Ash", 100, 100, 10)
    p2 = Player("Misty", 100, 100, 10)

    # p1 catches pikachu and charmander
    p1.catch_pokemon(pikachu)
    p1.catch_pokemon(charmander)
    p1.display_pokemons()

    # p2 catches squirtle and bulbasaur
    p2.catch_pokemon(squirtle)
    p2.catch_pokemon(bulbasaur)
    p2.display_pokemons()

    # player take turns to attack
    # player can attack
    # each pokemon can cast 1 spell

    # p1's turn
    p1.attack(p2)
    p1.get_pokemons()[0].cast_spell(p2.get_pokemons()[0])
    p1.get_pokemons()[1].cast_spell(p2.get_pokemons()[0])

    # p2's turn
    p2.attack(p1)
    p2.get_pokemons()[0].cast_spell(p1.get_pokemons()[0])
    p2.get_pokemons()[1].cast_spell(p2.get_pokemons()[0])  # heal

    # display status
    p1.display_pokemons()
    p2.display_pokemons()

    print("--- End of Test 02 ---\n")


test_02()


"""
--- Test 01: test cataching different types of pokemons ---
Name: Ash Ketchum, hp: 100, mp: 100, atk: 20.
Ash Ketchum, you have not caught any pokemons yet.

Ash Ketchum have caught Charmander.
Ash Ketchum have caught Squirtle.
Ash Ketchum have caught Bulbasaur.
Ash Ketchum have caught Pikachu.
Here are the pokemons in Ash Ketchum's team:
Name: Charmander, hp: 50, mp: 60, atk: 18. type: Fire.
Spell details: name: Fireball, mp_cost: 12, damage: 25.
Name: Squirtle, hp: 55, mp: 60, atk: 15. type: Water.
Spell details: name: Frostbolt, mp_cost: 8, damage: 16.
Name: Bulbasaur, hp: 80, mp: 60, atk: 12. type: Grass.
Spell details: name: Heal, mp_cost: 10, damage: -20.
Name: Pikachu, hp: 60, mp: 60, atk: 15. type: Electric.
Spell details: name: Thunderbolt, mp_cost: 10, damage: 20.

Ash Ketchum, you already have:
Name: Charmander, hp: 50, mp: 60, atk: 18. type: Fire.
Spell details: name: Fireball, mp_cost: 12, damage: 25.
Now you meet:
Name: Ponyta, hp: 60, mp: 60, atk: 18. type: Fire.
Spell details: name: Fireblast, mp_cost: 15, damage: 30.
Would you like to replace the pokemon of the same type? [Y/N]y
Ash Ketchum have released Charmander, and caught Ponyta.
Here are the pokemons in Ash Ketchum's team:
Name: Squirtle, hp: 55, mp: 60, atk: 15. type: Water.
Spell details: name: Frostbolt, mp_cost: 8, damage: 16.
Name: Bulbasaur, hp: 80, mp: 60, atk: 12. type: Grass.
Spell details: name: Heal, mp_cost: 10, damage: -20.
Name: Pikachu, hp: 60, mp: 60, atk: 15. type: Electric.
Spell details: name: Thunderbolt, mp_cost: 10, damage: 20.
Name: Ponyta, hp: 60, mp: 60, atk: 18. type: Fire.
Spell details: name: Fireblast, mp_cost: 15, damage: 30.

--- End of Test 01 ---

--- Test 02: test attacking between players and pokemons ---
Ash have caught Pikachu.
Ash have caught Charmander.
Here are the pokemons in Ash's team:
Name: Pikachu, hp: 120, mp: 100, atk: 10. type: Electric.
Spell details: name: Thunderbolt, mp_cost: 10, damage: 20.
Name: Charmander, hp: 80, mp: 120, atk: 10. type: Fire.
Spell details: name: Fireball, mp_cost: 12, damage: 25.

Misty have caught Squirtle.
Misty have caught Bulbasaur.
Here are the pokemons in Misty's team:
Name: Squirtle, hp: 100, mp: 90, atk: 10. type: Water.
Spell details: name: Frostbolt, mp_cost: 8, damage: 16.
Name: Bulbasaur, hp: 120, mp: 100, atk: 10. type: Grass.
Spell details: name: Heal, mp_cost: 10, damage: -20.

Ash attacks Misty.
Misty is hit, hp changes from 100 to 90.

Pikachu casts Thunderbolt on Squirtle.
Squirtle is hit, hp changes from 100 to 80.

Charmander casts Fireball on Squirtle.
Squirtle is hit, hp changes from 80 to 55.

Misty attacks Ash.
Ash is hit, hp changes from 100 to 90.

Squirtle casts Frostbolt on Pikachu.
Pikachu is hit, hp changes from 120 to 104.

Bulbasaur casts Heal on Squirtle.
Squirtle is hit, hp changes from 55 to 75.

Here are the pokemons in Ash's team:
Name: Pikachu, hp: 104, mp: 90, atk: 10. type: Electric.
Spell details: name: Thunderbolt, mp_cost: 10, damage: 20.
Name: Charmander, hp: 80, mp: 108, atk: 10. type: Fire.
Spell details: name: Fireball, mp_cost: 12, damage: 25.

Here are the pokemons in Misty's team:
Name: Squirtle, hp: 75, mp: 82, atk: 10. type: Water.
Spell details: name: Frostbolt, mp_cost: 8, damage: 16.
Name: Bulbasaur, hp: 120, mp: 90, atk: 10. type: Grass.
Spell details: name: Heal, mp_cost: 10, damage: -20.

--- End of Test 02 ---

"""
