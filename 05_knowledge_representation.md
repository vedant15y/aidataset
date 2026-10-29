# Practical 5: KNOWLEDGE REPRESENTATION USING PROLOG/PYTHON

Objective: To represent facts and rules for an organizational hierarchy and perform forward- and backward-chaining logical inference.
Scenario: An enterprise HR system needs to reason about reporting relationships in an organization (who reports to whom, who is a manager-of-manager) using declarative facts and recursive rules — identical to expert system knowledge engineering.

## Questions 1 & 2: Facts Base & Recursive Ancestor Rule

### Questions 1 & 2 - Knowledge Base & Ancestor Rule

```python
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
```

### Sample output from the source report

```text
Is Priya direct manager of Aarav? True
Is Rohit direct manager of Aarav? False
Is Rohit an ancestor of Aarav? True
Is Kavya an ancestor of Aarav? True
```

## Question 3: Forward-Chaining Inference Engine

### Question 3 - Forward Chaining

```python
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
```

### Sample output from the source report

```text
All direct + derived reporting relationships:
  Aarav reports up to Kavya
  Aarav reports up to Priya
  Aarav reports up to Rohit
  Priya reports up to Kavya
  Priya reports up to Rohit
  Rohit reports up to Kavya
  Sneha reports up to Kavya
  Sneha reports up to Priya
  Sneha reports up to Rohit
```

## Questions 4 & 5: Backward-Chaining Goal-Driven Proof & Reasoning Trace

### Questions 4 & 5 - Backward Chaining & Trace

```python
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
```

### Sample output from the source report

```text
Query Result: Does Aarav report up to Kavya? True

Reasoning steps (Trace):
  Checking: does Aarav report directly to Priya?
   Not a direct match. Recursing on Priya -> Kavya
  Checking: does Priya report directly to Rohit?
   Not a direct match. Recursing on Rohit -> Kavya
  Checking: does Rohit report directly to Kavya?
   Match found: Rohit -> Kavya. Goal reached.
```
