item1_name  = "Маргарита"
item1_price = 2200
item1_qty   = 2
item1_sum = item1_price * item1_qty
print(f"item1_sum {item1_sum}")


item2_name  = "Пепперони"
item2_price = 2700
item2_qty   = 1
item2_sum = item2_price * item2_qty
print(f"item2_sum {item2_sum}")

item3_name  = "Кола 1л"
item3_price = 700
item3_qty   = 3
item3_sum = item3_price * item3_qty
print(f"item3_sum {item3_sum}")



item4_name  = "Чизкейк"
item4_price = 1500
item4_qty   = 2
item4_sum =  item4_price * item4_qty
print(f"item4_sum {item4_sum}")


item_sum = item1_sum + item2_sum + item3_sum + item4_sum
print(f"item_sum {item_sum}")

delivery         = True
delivery_price   = 800
discount_percent = 10

discount = item_sum / 100 * 10
print(f"discount {discount}")


# item_sum_no_skitki = item_sum - discount
# print(f"item_sum_no_skitki {item_sum_no_skitki}")