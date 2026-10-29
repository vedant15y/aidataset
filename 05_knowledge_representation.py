"""Practical 5: KNOWLEDGE REPRESENTATION USING PROLOG/PYTHON.

Extracted from BSBXLB302P_AI_Lab_Practical_Report.docx.
"""

# Knowledge base: parent(child, parent) means child reports to parent
facts = [
    ("Aarav", "Priya"),   # Aarav reports to Priya
    ("Priya", "Rohit"),   # Priya reports to Rohit
    ("Sneha", "Priya"),   # Sneha reports to Priya
    ("Rohit", "Kavya")    # Rohit reports to Kavya (CEO)
]

def is_parent(child, parent):
    return (child, parent) in facts

def is_ancestor(person, ancestor, visited=None):
    if visited is None:
        visited = set()
    for child, parent in facts:
        if child == person and parent not in visited:
            if parent == ancestor:
                return True
            visited.add(parent)
            if is_ancestor(parent, ancestor, visited):
                return True
    return False

print("Is Priya direct manager of Aarav?", is_parent("Aarav", "Priya"))
print("Is Rohit direct manager of Aarav?", is_parent("Aarav", "Rohit"))
print("Is Rohit an ancestor of Aarav?", is_ancestor("Aarav", "Rohit"))
print("Is Kavya an ancestor of Aarav?", is_ancestor("Aarav", "Kavya"))

def forward_chain(facts):
    derived = set(facts)
    changed = True
    while changed:
        changed = False
        new_facts = set()
        for (a, b) in derived:
            for (c, d) in derived:
                if b == c and (a, d) not in derived and (a, d) not in new_facts:
                    new_facts.add((a, d))
        if new_facts:
            derived.update(new_facts)
            changed = True
    return derived

all_relationships = forward_chain(facts)
print("All direct + derived reporting relationships:")
for rel in sorted(all_relationships):
    print(f"  {rel[0]} reports up to {rel[1]}")

def backward_chain(query_child, query_ancestor, facts, trace=None):
    if trace is None:
        trace = []
    for (child, parent) in facts:
        if child == query_child:
            trace.append(f"Checking: does {child} report directly to {parent}?")
            if parent == query_ancestor:
                trace.append(f"  Match found: {child} -> {parent}. Goal reached.")
                return True, trace
            else:
                trace.append(f"  Not a direct match. Recursing on {parent} -> {query_ancestor}")
                result, trace = backward_chain(parent, query_ancestor, facts, trace)
                if result:
                    return True, trace
    return False, trace

result, trace = backward_chain("Aarav", "Kavya", facts)
print(f"Query Result: Does Aarav report up to Kavya? {result}\n")
print("Reasoning steps (Trace):")
for step in trace:
    print(" ", step)
