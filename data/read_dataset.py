
from pathlib import Path
from tsfile import TsFileReader

# Project directory
project_dir = Path(__file__).resolve().parent.parent

# Input and output files
train_path = project_dir / "data/raw/freshretailnet_50k_train.tsfile"

output_path = (
    project_dir / "data/processed/freshretailnet_train_full.csv"
)

output_path.parent.mkdir(parents=True, exist_ok=True)

total_rows = 0

with TsFileReader(str(train_path)) as reader:

    # Get all tables
    schemas = reader.get_all_table_schemas()
    print("Available tables:", list(schemas))

    # Select first table
    table_name = next(iter(schemas))
    table = schemas[table_name]

    # Get column names
    columns = [
        col.get_column_name()
        for col in table.get_columns()
    ]

    fields = [
        col for col in columns
        if col not in {"Time", "time"}
    ]

    # Read all batches
    with reader.query_table(
        table_name,
        fields,
        batch_size=1024
    ) as result:

        first_batch = True

        while True:
            batch = result.read_arrow_batch()

            if batch is None:
                break

            df_batch = batch.to_pandas()

            # Append batch to CSV
            df_batch.to_csv(
                output_path,
                mode="w" if first_batch else "a",
                header=first_batch,
                index=False
            )

            total_rows += len(df_batch)
            first_batch = False

            if total_rows % 10000 < len(df_batch):
                print(f"Exported {total_rows:,} rows")

print("\nExport completed!")
print(f"Total rows exported: {total_rows:,}")
print(f"CSV saved to: {output_path}")
