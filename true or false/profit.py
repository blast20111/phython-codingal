actual_cost=float(input("write the actual cost :"))
selling_cost=float(input("write the selling cost"))
profit=selling_cost - actual_cost
if selling_cost>actual_cost:
  print("the profit is",profit)
else:
    print("there is no profit")
