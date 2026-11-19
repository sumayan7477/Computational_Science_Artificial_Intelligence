def count_products(products):
    counts={}

    for product in products:
        if product in counts:
            counts[product]+=1

        else:
            counts[product]=1

    return counts

def create_receipt(counts):
    receipt =[]
    for product in counts:
        receipt.append((product , counts[product]))
    receipt.sort()
    return receipt


def print_receipt(receipt):
    print("\nReceipt")
    print("-" * 30)
    for product, quantity in receipt:
        print(f"{product:<20} x{quantity}")
    print("-" * 30)

def main():
    products = input("Enter purchased products: ").split()
    counts = count_products(products)
    receipt = create_receipt(counts)

    print_receipt(receipt)
    print(f"Total items: {len(products)}")
    print(f"Different products: {len(receipt)}")
main()