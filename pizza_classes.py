class Pizza:
    """Общий класс всех пицц"""

    def __init__(self, size: str):
        self.ingredients = None
        self.title = None
        self._vocabulary = {}
        if size not in ('XL', 'L'):
            raise TypeError('Wrong size identification')
        self.size = size

    @property
    def dict(self) -> dict:
        d = {self.title: self.ingredients}
        return d

    def __eq__(self, other) -> bool:
        test1 = (self.title == other.title)
        test2 = (self.size == other.size)
        return test1 and test2


class Margherita(Pizza):
    """Создание пиццы Margherita"""
    def __init__(self, size: str):
        super().__init__(size)
        self.ingredients = ['tomato sauce', 'mozzarella', 'tomatoes']
        self.title = __class__.__name__
        self._vocabulary = {}


class Pepperoni(Pizza):
    """Создание пиццы Pepperoni"""
    def __init__(self, size: str):
        super().__init__(size)
        self.ingredients = ['tomato sauce', 'mozzarella', 'pepperoni']
        self.title = __class__.__name__
        self._vocabulary = {}


class Hawaiian(Pizza):
    """Создание пиццы Hawaiian"""
    def __init__(self, size: str):
        super().__init__(size)
        self.ingredients = ['tomato sauce', 'mozzarella', 'pepperoni']
        self.title = __class__.__name__
        self._vocabulary = {}


if __name__ == '__main__':
    mine = Margherita('XL')
    mine2 = Margherita('XL')
    mine3 = Hawaiian('L')
    assert mine == mine2
    assert mine != mine3
    assert mine.dict == {'Margherita': ['tomato sauce', 'mozzarella', 'tomatoes']}
    assert mine.size == 'XL'
