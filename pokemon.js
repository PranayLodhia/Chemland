// Define Pokemon classes
class Pokemon {
  constructor(name, type, hp, attack, defense) {
    this.name = name;
    this.type = type;
    this.hp = hp;
    this.attack = attack;
    this.defense = defense;
  }

  attackOpponent(opponent) {
    const damage = this.attack - opponent.defense;
    opponent.hp -= damage;
    console.log(`${this.name} attacked ${opponent.name} for ${damage} damage!`);
  }
}

const Charmander = new Pokemon("Charmander", "Fire", 100, 50, 25);
const Bulbasaur = new Pokemon("Bulbasaur", "Grass", 100, 40, 30);

// Simulate battle
while (Charmander.hp > 0 && Bulbasaur.hp > 0) {
  // Players take turns making attacks
  Charmander.attackOpponent(Bulbasaur);
  if (Bulbasaur.hp > 0) {
    Bulbasaur.attackOpponent(Charmander);
  }
}

// Display results
if (Charmander.hp > 0) {
  console.log(`${Charmander.name} wins!`);
} else {
  console.log(`${Bulbasaur.name} wins!`);
}
