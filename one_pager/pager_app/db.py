# This file is for reading data from the db/ directory

# parses text files (only) found in the db directory
def parse_text(filename):

    file_path = "data/" + filename
    with open(file_path,"r") as f:
        data = f.read()
        f.close()

    processed_data = data.split("\n\n\n")

    return processed_data

# print(len(parse_text("uses.txt")))
