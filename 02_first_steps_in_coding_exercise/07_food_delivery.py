# 7 Food Delivery
chicken_menu_price = float(10.35)
fish_menu_price = float(12.40)
vegetarian_menu_price = float(8.15)
delivery_price = float(2.50)
chicken_menu_quantity = int(input())
fish_menu_quantity = int(input())
vegetarian_menu_quantity = int(input())
total_chicken_menus_price = float(chicken_menu_price * chicken_menu_quantity)
total_fish_menu_price = float(fish_menu_price * fish_menu_quantity)
total_vegetarian_menu_price = float(vegetarian_menu_price * vegetarian_menu_quantity)
total_menu_price = float(total_chicken_menus_price + total_fish_menu_price + total_vegetarian_menu_price)
desert_price = float(total_menu_price * 0.2)
final_price = float(total_menu_price + desert_price + delivery_price)
print(f'Total price: {final_price} lv.')
