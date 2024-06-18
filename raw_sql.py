import sqlite3
import csv


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
        for row in cursor.execute(f"SELECT * FROM {tabela}"):
            


database = input("Digite o nome da tabela:")
tabelas = extrair_nome_tabelas(database)
exportar_tabelas_csv(database, tabelas)

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
