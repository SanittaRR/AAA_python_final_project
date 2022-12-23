from pizza_classes import *
import click


@click.group()
def cli():
    pass


@click.command()
def menu():
    """Выводит меню"""
    pizza1 = Margherita('L')
    pizza2 = Pepperoni('L')
    pizza3 = Hawaiian('L')
    ingredients1 = ', '.join(pizza1.ingredients)
    ingredients2 = ', '.join(pizza2.ingredients)
    ingredients3 = ', '.join(pizza3.ingredients)
    print(f'- {pizza1.title} 🧀: {ingredients1}')
    print(f'- {pizza2.title} 🍕: {ingredients2}')
    print(f'- {pizza3.title} 🍍: {ingredients3}')


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza_type', nargs=1)
def order(pizza_type: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    print(f'👨‍🍳Приготовили {pizza_type} за 2с!')
    if delivery:
        print(f'🛵Доставили {pizza_type} за 1с!')


cli.add_command(menu)
cli.add_command(order)

if __name__ == '__main__':
    cli()
    # $ python menu_order.py order Pepperoni
    # $ python menu_order.py order Pepperoni --delivery
    # $ python menu_order.py menu
