import pandas as pd
import glob

files = glob.glob('../dataset/BCCC-CIC-IDS-2017/*.csv')

with open('../dataset/combined_dataset.csv', 'w') as combined_file:
    for i, file in enumerate(files):
        print(f"Loading and writing {file}...")

        for chunk in pd.read_csv(file, chunksize=100000):
            if i==0:
                # if it's the first file, then I write the header as well
                chunk.to_csv(combined_file, header=True, index=False)
            else:
                chunk.to_csv(combined_file, header=False, index=False)
        print(f"File {file} completed.")

print("Combination completed.")
