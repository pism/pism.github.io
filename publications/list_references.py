from pybtex.database import parse_file, BibliographyData
import io
import sys
import re

import pybtex.backends.markdown
backend = pybtex.backends.markdown.Backend()

import pybtex.style.formatting.plain
style = pybtex.style.formatting.plain.Style()

def get_year(bib_data, year):
    D = {}
    for k, v in bib_data.entries.items():
        if v.fields["year"] == str(year):
            D[k] = v
    return BibliographyData(D)

def format_list(bib_data):
    formatted = style.format_bibliography(bib_data)

    result = io.StringIO()

    for k, e in enumerate(formatted.entries):
        entry = io.StringIO()
        backend.write_to_stream([e], entry)
        text = entry.getvalue()
        # unwrap lines
        text = text.replace("\n", " ")
        # replace "[N] " with "N. " to make an ordered list in Markdown
        text = re.sub(r"^\[([0-9]+)\] ", r"\1. ", text)

        result.write(text)
        # add a line break at the end of the entry
        result.write("\n")

    return result.getvalue()

def years(bib_data):
    result = []
    for _, v in bib_data.entries.items():
        result.append(int(v.fields["year"]))
    return set(result)

if __name__ == "__main__":
    input_file = sys.argv[1]
    data = parse_file(input_file)
    try:
        year = int(sys.argv[2])
        print(format_list(get_year(data, year)))
    except:
        Y = years(data)
        for y in range(max(Y), min(Y) - 1, -1):
            year_data = get_year(data, y)
            if len(year_data.entries) > 0:
                print(f"### {y}\n")
                print(format_list(year_data))
