import pandas as pd
import glob

files = glob.glob('../dataset/BCCC-CIC-IDS-2017/*.csv')

with open('../dataset/combined_dataset.csv', 'w') as combined_file:
    for i, file in enumerate(files):
        print(f"Loading and writing {file}...")

        if i == 0:
            for chunk in pd.read_csv(file, chunksize=100000):
                chunk.to_csv(combined_file, header=True, index=False)
        else:
            for chunk in pd.read_csv(file, chunksize=100000):
                chunk.to_csv(combined_file, header=False, index=False)
        
        print(f"File {file} completed.")

print("Combination completed.")
