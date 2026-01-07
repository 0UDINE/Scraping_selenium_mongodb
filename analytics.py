import matplotlib.pyplot as plt
from load2mongodb import collection


def show_analytics():
    # 1. Calcul du prix moyen via Aggregation Pipeline
    pipeline_avg = [{"$group": {"_id": None, "avg_price": {"$avg": "$price"}}}]
    avg_result = list(collection.aggregate(pipeline_avg))

    if avg_result:
        print(f"Prix moyen global : {avg_result[0]['avg_price']:.2f} £")

    # 2. Préparation du graphique
    data = list(collection.find().limit(10))  # On prend les 10 premiers

    if not data:
        print("Erreur : La base de données est vide !")
        return

    titles = [b["title"][:10] for b in data]
    prices = [b["price"] for b in data]

    plt.bar(titles, prices)
    plt.title("Distribution des prix des livres")
    plt.ylabel("Prix (£)")
    plt.show()


if __name__ == "__main__":
    show_analytics()