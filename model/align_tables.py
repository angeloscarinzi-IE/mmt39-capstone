"""Align markdown tables: pad cells so pipes line up, and report column-count errors."""
import re, sys, unicodedata

def width(s):
    """Character count. Table cells must contain no wide/emoji characters."""
    return len(s)

def pad(s, n, align):
    gap = n - width(s)
    if gap <= 0:
        return s
    if align == "right":
        return " " * gap + s
    if align == "center":
        l = gap // 2
        return " " * l + s + " " * (gap - l)
    return s + " " * gap

def split_row(line):
    t = line.strip()
    if t.startswith("|"): t = t[1:]
    if t.endswith("|"):   t = t[:-1]
    return [c.strip() for c in t.split("|")]

SEP = re.compile(r'^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$')

def process(path):
    lines = open(path).read().split("\n")
    out, i, issues, tables = [], 0, [], 0
    while i < len(lines):
        if (lines[i].strip().startswith("|") and i + 1 < len(lines)
                and SEP.match(lines[i + 1])):
            start = i
            block = [lines[i], lines[i + 1]]
            j = i + 2
            while j < len(lines) and lines[j].strip().startswith("|"):
                block.append(lines[j]); j += 1

            header = split_row(block[0])
            seps   = split_row(block[1])
            ncol   = len(header)
            aligns = []
            for s in seps:
                s = s.strip()
                if s.startswith(":") and s.endswith(":"): aligns.append("center")
                elif s.endswith(":"):                     aligns.append("right")
                else:                                     aligns.append("left")
            while len(aligns) < ncol: aligns.append("left")

            rows = [header] + [split_row(b) for b in block[2:]]
            for k, r in enumerate(rows):
                if len(r) != ncol:
                    issues.append(f"  line {start+1 if k==0 else start+2+k}: "
                                  f"{len(r)} cells, header has {ncol} -> {r}")
                    while len(r) < ncol: r.append("")
                    del r[ncol:]

            widths = [max(width(r[c]) for r in rows) for c in range(ncol)]
            widths = [max(w, 3) for w in widths]

            new = ["| " + " | ".join(pad(header[c], widths[c], aligns[c])
                                     for c in range(ncol)) + " |"]
            sepcells = []
            for c in range(ncol):
                w = widths[c]
                if aligns[c] == "right":    sepcells.append("-" * (w - 1) + ":")
                elif aligns[c] == "center": sepcells.append(":" + "-" * (w - 2) + ":")
                else:                       sepcells.append("-" * w)
            new.append("| " + " | ".join(sepcells) + " |")
            for r in rows[1:]:
                new.append("| " + " | ".join(pad(r[c], widths[c], aligns[c])
                                             for c in range(ncol)) + " |")
            out.extend(new)
            tables += 1
            i = j
        else:
            out.append(lines[i]); i += 1

    open(path, "w").write("\n".join(out))
    print(f"{path}: {tables} tables aligned")
    if issues:
        print("  COLUMN-COUNT PROBLEMS FOUND AND FIXED:")
        for x in issues: print(x)
    else:
        print("  all rows had matching column counts")

for p in sys.argv[1:]:
    process(p)
