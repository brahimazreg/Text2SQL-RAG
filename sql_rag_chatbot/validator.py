# The validator can be considered a security layer, but its role is a little broader than only security.
def validate_sql(sql):

    forbidden = [
        "DROP",
        "DELETE",
        "UPDATE",
        "INSERT",
        "ALTER"
    ]

    sql_upper = sql.upper()

    for word in forbidden:
        if word in sql_upper:
            raise ValueError(
                f"Forbidden SQL operation: {word}"
            )

    if not sql_upper.strip().startswith("SELECT"):
        raise ValueError(
            "Only SELECT queries are allowed"
        )

    return sql