import sqlite3
import csv

total_falhas = 0


def conta_falhas():
    total_falhas + 1


def extrair_nome_tabelas(database):
    conectar = sqlite3.connect(f"database/{database}.db")
    cursor = conectar.cursor()
    raw_sql = "SELECT name FROM sqlite_master WHERE type='table';"
    lista_tabelas = []
    for item in cursor.execute(raw_sql):
        lista_tabelas.append(item[0])
    print(f"Tabelas Extraidas:\n{lista_tabelas}")
    return lista_tabelas


def exportar_tabelas_csv(database, tabelas):
    conectar = sqlite3.connect(f"database/{database}.db")
    cursor = conectar.cursor()
    for tabela in tabelas:
        with open(f"teste/{tabela}.csv", "w") as csvfile:
            write = csv.writer(csvfile)
            for row in cursor.execute(f"SELECT * FROM {tabela}"):
                row_filtrada = [
                    item for item in row if isinstance(item, (int, float, str))
                ]
                write.writerow(row_filtrada)


database = input("Digite o nome da tabela:")
tabelas = extrair_nome_tabelas(database)
exportar_tabelas_csv(database, tabelas)
print(total_falhas)
# def main() -> None:
#     number_of_top_customers = int(
#         input("How many top customers do you want to query? ")
#     )

#     con = sqlite3.connect("database/sample_database.db")

#     cur = con.cursor()

#     raw_sql = """
# 	SELECT
# 		c.id,
# 		c.first_name,
# 		SUM(i.total) AS total
# 	FROM Invoice i
# 	LEFT JOIN Customer c ON i.customer_id = c.id
# 	GROUP BY c.id, c.first_name
# 	ORDER BY total DESC
# 	LIMIT ?;
# 	"""

#     for row in cur.execute(raw_sql, (number_of_top_customers,)):
#         print(row)


# if __name__ == "__main__":
#     main()
