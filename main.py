from data_loader import load_csv
from operations import save_csv, summary, filter_data, group_by, sort_data
from sql_parser import parse_query, execute_query


# ---------------------------
# UI FUNCTION (TABLE DISPLAY)
# ---------------------------
def print_table(data):
    if not data:
        print("No data to display")
        return

    headers = list(data[0].keys())

    # calculate column widths
    col_widths = {}
    for h in headers:
        max_len = len(h)
        for row in data:
            max_len = max(max_len, len(row[h]))
        col_widths[h] = max_len

    # print header
    header_row = ""
    for h in headers:
        header_row += h.ljust(col_widths[h]) + " | "
    print("\n" + header_row)

    # separator
    print("-" * len(header_row))

    # print rows
    for row in data:
        row_str = ""
        for h in headers:
            row_str += row[h].ljust(col_widths[h]) + " | "
        print(row_str)

    print()


# ---------------------------
# MAIN PROGRAM
# ---------------------------
print("🚀 Welcome to DataCLI (Mini SQL Engine)")
print("Type 'help' to see available commands\n")

data = []
original_data = []

while True:
    command = input(">> ").strip()

    # ---------------------------
    # EXIT
    # ---------------------------
    if command == "exit":
        print("👋 Goodbye!")
        break

    # ---------------------------
    # LOAD
    # ---------------------------
    elif command.startswith("load"):
        parts = command.split()

        if len(parts) < 2:
            print("❌ Please provide filename")
            continue

        filename = parts[1]

        try:
            data = load_csv(filename)
            original_data = data.copy()
            print("✅ Data loaded successfully!")
        except:
            print("❌ Error loading file")

    # ---------------------------
    # SUMMARY
    # ---------------------------
    elif command == "summary":
        if not data:
            print("❌ No data loaded")
        else:
            summary(data)

    # ---------------------------
    # FILTER
    # ---------------------------
    elif command.startswith("filter"):
        if not data:
            print("❌ No data loaded")
            continue

        condition = command.replace("filter", "").strip()

        if "=" not in condition:
            print("❌ Use format: filter column=value")
            continue

        key, value = condition.split("=")
        key, value = key.strip(), value.strip()

        data = filter_data(data, key, value)

        print("✅ Filter applied!")
        print_table(data)

    # ---------------------------
    # GROUP BY
    # ---------------------------
    elif command.startswith("groupby"):
        if not data:
            print("❌ No data loaded")
            continue

        parts = command.split()

        if len(parts) < 2:
            print("❌ Provide column name")
            continue

        key = parts[1]
        result = group_by(data, key)

        print("\n📊 Grouped Result:")
        for k, v in result.items():
            print(f"{k} → {v}")
        print()

    # ---------------------------
    # SORT
    # ---------------------------
    elif command.startswith("sort"):
        if not data:
            print("❌ No data loaded")
            continue

        parts = command.split()

        if len(parts) < 3:
            print("❌ Use format: sort column asc/desc")
            continue

        key = parts[1]
        order = parts[2]

        reverse = True if order.lower() == "desc" else False

        new_data = sort_data(data, key, reverse)

        if new_data is not None:
            data = new_data
            print("✅ Data sorted!")
            print_table(data)

    # ---------------------------
    # SAVE
    # ---------------------------
    elif command.startswith("save"):
        if not data:
            print("❌ No data loaded")
            continue

        parts = command.split()

        if len(parts) < 2:
            print("❌ Provide filename")
            continue

        filename = parts[1]
        save_csv(data, filename)

    # ---------------------------
    # RESET
    # ---------------------------
    elif command == "reset":
        data = original_data.copy()
        print("🔄 Data reset to original!")

    # ---------------------------
    # HELP
    # ---------------------------
    elif command == "help":
        print("""
📌 Available Commands:
----------------------
load <file>
summary
filter column=value
groupby column
sort column asc/desc
save <file>
reset
SELECT * WHERE column=value SORT BY column DESC
exit
""")

    # ---------------------------
    # SQL SELECT
    # ---------------------------
    elif command.startswith("SELECT"):
        if not data:
            print("❌ No data loaded")
            continue

        parsed = parse_query(command)
        result = execute_query(data, parsed)

        if not result:
            print("❌ No results found")
        else:
            print_table(result)

    # ---------------------------
    # UNKNOWN
    # ---------------------------
    else:
        print("❌ Unknown command (type 'help')")