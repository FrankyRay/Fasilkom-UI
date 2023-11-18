import os, sys, time

# Constant variables
FILES = os.listdir("dataset/")
WIDTH = os.get_terminal_size()[0]
SECTIONS = ["kepala_putusan", "identitas", "riwayat_penahanan", "riwayat_perkara",
            "riwayat_tuntutan", "riwayat_dakwaan","fakta", "fakta_umum",
            "pertimbangan_hukum", "amar_putusan", "penutup", "all"]
OPERATOR = ["AND", "OR", "ANDNOT"]
FILTERS = {"amar": 'a', "amar-lainnya": 'm', "klasifikasi": 'k', "lama-hukuman": 'l', "lembaga-peradilan": 'p', "provinsi": 'r', "status": 't', "sub-klasifikasi": 's'}
OPTIONS = {"help": 'h', "verbose": 'v'}

# Functions
def help_print():
    print(
"""Python 'search.py' ~ Mencari dokumen-dokumen berdasarkan kata kunci yang dicari.

Usage:
  python search.py <section> <keyword> [operator] [keyword_op] [--FILTER] [--OPTION]

Parameter:
  section                  Mencari kata kunci dari bagian tertentu atau semua bagian
  keyword                  Kata kunci pencarian
  operator                 Operasi boolean sebagai filter tambahan
  keyword_op               Kata kunci lainnya sebagai filter

Filter:
  -a  [amar             ]  Bunyi putusan sesudah kata memutuskan, mengadili
  -m  [amar-lainnya     ]  Jenis bunyi putusan
  -k  [klasifikasi      ]  Klasifikasi hukuman/pidana
  -l  [lama-hukuman     ]  Lama waktu hukuman ([awal][,[akhir]])
  -p  [lembaga-peradilan]  Nama dari lembaga peradilan
  -r  [provinsi         ]  Lokasi provinsi lembaga peradilan
  -t  [status           ]  Status hukuman/pidana
  -s  [sub-klasifikasi  ]  Tipe klasifikasi hukuman/pidana

Option:
  -h  [help             ]  Menampilkan pesan help ini
  -v  [verbose          ]  Menampilkan progress dari program ini""")

def get_metadata(header: str):
    """Get the metadata of the xml file"""
    raw_metadata = [meta.split("=") for meta in header.split(" ")]
    return {key: val[1:-1] for (key, val) in raw_metadata}

def print_table(data: list[dict]):
    print(" " * WIDTH)
    print("File Kasus".rjust(36), "Provinsi".rjust(15), "Klarifikasi".rjust(15), "Sub Klarifikasi".rjust(30), "Lembaga Peradilan".rjust(20))
    print("-" * 120)
    for d in data: print(d["id"] + ".xml",
                         d["provinsi"][:15].rjust(15),
                         d['klasifikasi'][:15].rjust(15),
                         d['sub_klasifikasi'][:30].rjust(30),
                         d['lembaga_peradilan'][:20].rjust(20))
    print()

def filter_data(data: dict, filter: dict):
    for flt_key, flt_val in filter.items():
        if data[flt_key] != flt_val:
            return False
    return True



# Get the CLI arguments and options
args = sys.argv[1:]
verbose = False

# Print help message if no argument
if len(args) == 0:
    help_print()
    exit()

# Checking --FILTER and --OPTION flags
data_filter = {}
for arg in args.copy():
    if not arg.startswith("-"): continue

    arg_idx = args.index(arg)
    try:
        flt_idx = list(FILTERS.values()).index(arg[1])
        flt_key = list(FILTERS.keys())[flt_idx]

        data_filter[flt_key.replace("-", "_")] = args.pop(arg_idx + 1)
        args.pop(arg_idx)
    except ValueError:
        try:
            opt_idx = list(OPTIONS.values()).index(arg[1])
            if opt_idx == 0:
                help_print()
                exit()
            else:
                verbose = True
            args.pop(arg_idx)
        except ValueError:
            print(f"Invalid option or filter {arg}")
            exit()

# Get "section" and "keyword" value
# Return error if the arguments is missing
try:
    section = args[0]
    keyword = args[1]
except IndexError:
    print("Argument program tidak benar")
    exit()
else:
    # Validate "section" value
    if section not in SECTIONS:
        # print(f"Argument program tidak benar. Nilai 'section' yang valid adalah {', '.join(SECTIONS)}, dan all")
        print(f"Argument program tidak benar")
        exit()

# Get "operator" and "keyword_op" value
# If the user didn't pass "operator" args, skip
try:
    operator = args[2]
except IndexError:
    operator = None
else: # Run this code when "operator" exist
    # Validate "operator" value
    if operator not in OPERATOR:
        print("Mode harus berupa AND, OR atau ANDNOT")
        exit()

    # Take the "keyword_op" value
    # Return error if the arguments is missing
    try:
        keyword_op = args[3]
    except IndexError:
        print("Argument program tidak benar")
        exit()

# Initiate some variable
files_data = []

# Loop over files and start the timer
time_start = time.time()
for index, file in enumerate(FILES):
    # Print status message (may slow the program)
    if verbose:
        percentage = (index+1) / len(FILES)
        print(f"Membaca dokumen {file} ({percentage:.1%})[{'#' * int(percentage * 10)}{'-' * (10 - int(percentage * 10))}] | Ditemukan: {len(files_data)} dokumen | Waktu: {time.time() - time_start:.2f}s", end="\r")

    # Read the file data
    with open("dataset/" + file) as f:
        data = f.readlines()

    # Concat the data string
    if section == "all":
        data_section = "".join([ln for ln in data if not ln.startswith("<")]).replace("\n", " ")
    else:
        try:
            section_start = data.index(f"<{section}>\n")
            section_end = data.index(f"</{section}>\n")
        except: continue

        data_section = "".join(data[section_start + 1 : section_end]).replace("\n", " ")

    # Continue the loop if keyword doesn't exist etc.
    if not ((operator == "AND" and (keyword in data_section and keyword_op in data_section)) \
        or  (operator == "OR" and (keyword in data_section or keyword_op in data_section)) \
        or  (operator == "ANDNOT" and (keyword in data_section and keyword_op not in data_section)) \
        or  (operator == None and keyword in data_section)): continue
    
    # Take the files' metadata/header
    mtdt = get_metadata(data[0][9:-2])
    if filter_data(mtdt, data_filter):
        files_data.append(mtdt)

# End search
time_end = time.time()

# Print the output message
print_table(files_data)
print(f"Banyaknya dokumen yang ditemukan = {len(files_data)}")
print(f"Total waktu pencarian            = {time_end - time_start:.3f}s")