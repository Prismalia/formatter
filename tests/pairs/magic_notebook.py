#%%
from pathlib import Path

hotel_dir = Path(__file__).parent / "../../work/Crawls Groups Users/Lists"
hotel_files = list(hotel_dir.glob("**/hotels.csv"))


#%%
!pip install ../../tools_pointage/supply_updater
!pip install ../../tools_pointage/support
!pip install ../../customsearch_tools


#%%
from supply_updater.hotels import pointer

def clean_hotels(file):
  with open(file, "r") as f:
    hotels = f.readlines()
  
  hotels = [h.strip() for h in hotels]
  hotels = list(set(hotels))
  hotels = [h for h in hotels if h]
  return hotels

def post_pointer(file):
  """Move the output file to the right place"""
  try:
    Path("completed.txt").unlink()
  except:
    pass
  try:
    Path("exception.txt").unlink()
  except:
    pass
  destination = file.parent / "output.csv"
  Path("hotels16_fast.csv").rename(destination)
  [f.unlink() for f in Path(".").glob("*.csv")]


#%%
from tqdm import tqdm

# for file in tqdm(hotel_files[46:]):
# for file in empty_output_files:
for file in tripadvisored_output_files:
  print(file)
  hotels = clean_hotels(file)
  pointer(hotels)
  post_pointer(file)



output_files = list(hotel_dir.glob("**/output.csv"))

#%%
def is_file_empty(path):
  with open(path, "r") as f:
    lines = f.readlines()
  return len(lines) == 1 

empty_output_files = [f for f in output_files if is_file_empty(f)]
empty_output_files = [e.parent / "hotels.csv" for e in empty_output_files]
empty_output_files
print(f"{len(empty_output_files)} empty output files out of {len(output_files)}")

#%%
import pandas as pd
def does_file_contain_tripadvisor(path):
  df = pd.read_csv(path, sep="\t")

  try:
    return df["Hotel Name"].map(
      lambda x: "tripadvisor" in x.lower() if isinstance(x, str) else False
      ).any()
  except:
    return False

tripadvisored_output_files = [f for f in output_files if does_file_contain_tripadvisor(f)]
tripadvisored_output_files = [e.parent / "hotels.csv" for e in tripadvisored_output_files]
print(f"{len(tripadvisored_output_files)} tripadvisored output files out of {len(output_files)}")


#%%
# from tqdm import tqdm

# hotel_files = list(hotel_dir.glob("**/hotels.csv"))

# for file in tqdm(hotel_files):
#   with open(file, "r") as f:
#     hotels = f.readlines()
#   hotels = list(set(hotels))
#   hotels = [h.strip() for h in hotels]
#   hotels = [h for h in hotels if h]

#   with open(file, "w") as f:
#     f.write("\n".join(hotels))