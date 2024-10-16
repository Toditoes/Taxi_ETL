import pyarrow.parquet as pq

trips = pq.read_table('./trip_data.parquet')
trips = trips.to_pandas()

trips.to_csv('trip_data.csv')