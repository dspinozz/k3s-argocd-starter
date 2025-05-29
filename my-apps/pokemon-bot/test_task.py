from worker import check_product_stock

if __name__ == "__main__":
    result = check_product_stock.delay()
    print(f"✅ Task submitted! ID: {result.id}")
