def make_statement(statement, decoration):
    """Adds additional characters to the start and end of headings as decoration"""

    ends = decoration * 3
    print(f"\n{ends} {statement} {ends}")
