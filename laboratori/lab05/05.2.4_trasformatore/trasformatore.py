for n in range(1, 201):
    n /= 100

    potenza = 8 * (n * 40) ** 2 / (n ** 2 * 20 + 8) ** 2
    print(f"Rapporto spire {n}, potenza: {potenza:.2f}W")

