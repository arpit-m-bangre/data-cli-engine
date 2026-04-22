# ---------------------------
# PARSE QUERY
# ---------------------------
def parse_query(query):
    # normalize query
    query = query.strip()

    # make uppercase version for keyword detection
    upper_query = query.upper()

    result = {
        "filter": None,
        "sort": None
    }

    # ---------------------------
    # HANDLE WHERE
    # ---------------------------
    if "WHERE" in upper_query:
        where_part = query[upper_query.index("WHERE") + len("WHERE"):]

        # remove SORT BY part if exists
        if "SORT BY" in upper_query:
            sort_index = upper_query.index("SORT BY")
            where_part = query[upper_query.index("WHERE") + len("WHERE"):sort_index]

        condition = where_part.strip()

        if "=" in condition:
            key, value = condition.split("=", 1)
            result["filter"] = (key.strip(), value.strip())

    # ---------------------------
    # HANDLE SORT
    # ---------------------------
    if "SORT BY" in upper_query:
        sort_part = query[upper_query.index("SORT BY") + len("SORT BY"):].strip()

        parts = sort_part.split()

        column = parts[0]
        order = "asc"

        if len(parts) > 1:
            order = parts[1]

        result["sort"] = (column.strip(), order.strip().lower())

    return result


# ---------------------------
# EXECUTE QUERY
# ---------------------------
from operations import filter_data, sort_data

def execute_query(data, parsed):
    if not data:
        print("❌ No data available")
        return []

    result_data = data.copy()

    # ---------------------------
    # APPLY FILTER
    # ---------------------------
    if parsed["filter"]:
        key, value = parsed["filter"]
        result_data = filter_data(result_data, key, value)

    # ---------------------------
    # APPLY SORT
    # ---------------------------
    if parsed["sort"]:
        column, order = parsed["sort"]

        reverse = True if order == "desc" else False

        sorted_result = sort_data(result_data, column, reverse)

        if sorted_result is not None:
            result_data = sorted_result

    return result_data