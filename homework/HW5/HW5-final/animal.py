
class Animal:

    # a class attribute of the valid species in our universe
    valid_species = {
        'cat',
        'dog',
        'duck',
        'elf',
        'goblin',
        'horse',
        'human',
        'mermaid',
        'nightingale',
        'pig',
        'swan',
        'wolf'
    }

    def __init__(self, name, species):
        self.name = name
        self._species = species

    def __repr__(self):
        return f'{self.name} ({self._species})'

    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, into):
        try:
            assert (into in self.valid_species), "AssertionError: invalid species: "+into
            self._species = into
            return self._species
        except AssertionError as error:
            print(error)


if __name__ == "__main__":
    dog = Animal('Fido', 'dog')
    print(dog.species)
    dog.species = 'cat'
    print(dog.species)
    dog.species = 'TheThing'
