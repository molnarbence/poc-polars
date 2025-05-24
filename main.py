import polars as pl


def foo(a: int, b: int) -> int:
    return a + b


def query_local_db() -> None:
    uri = "postgresql://testuser:testpassword@localhost:5432/testdb"
    query = "SELECT * from flights"

    foo_df = pl.read_database_uri(query=query, uri=uri)
    print(foo_df)

    foo_df.write_csv("./outputs/bar.csv")
    foo_df.write_parquet("./outputs/bar.parquet")


if __name__ == "__main__":
    query_local_db()
