import re
def rex_beginning(text):
    pattern = "x\s*=\s*(\w+),\s*y\s*=\s*(\w+)"
    match = re.search(pattern, text)
    return match.group(1), match.group(2)


def to_positions(text):
    curr, prev, row, col = 0, 0, 0, 0
    positions = []
    for i, v in enumerate(text):
        if v.isalpha() or v == '$': 
            if (i - prev) > 0:
                print(prev, i, text[prev:i])
                curr = int(text[prev:i])
            else:
                curr = 1

            if v == '$':
                row += 1
                col = 0
            elif v == 'b':
                col += curr
            elif v == 'o':
                for j in range(curr):
                    positions.append((row, col + j))
            prev = i + 1
    return positions

def parse_rle(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().split('\n')
        offset = -1
        for i, line in enumerate(lines):
            if len(line) == 0 or '#' == line[0]: continue
            offset = i
            break

        assert(offset != -1)
        lines = lines[offset:]
        rows, cols = rex_beginning(lines[0])
        cleaned_lines = ''.join(lines[1:])
        print(to_positions(cleaned_lines))
    



parse_rle('glider.rle')
