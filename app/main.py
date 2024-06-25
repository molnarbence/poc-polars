import polars as pl
import psycopg


def foo(a: int, b: int) -> int:
    return a + b


def query_local_db() -> None:
    with psycopg.connect(
        "host=localhost port=5432 dbname=postgres user=postgres password=postgres connect_timeout=10"
    ) as conn:
        foo_df = pl.read_database("SELECT * from foo.bar", connection=conn)

        print(foo_df)

        foo_df.write_csv("./outputs/bar.csv")
        foo_df.write_parquet("./outputs/bar.parquet")


if __name__ == "__main__":
    query_local_db()
