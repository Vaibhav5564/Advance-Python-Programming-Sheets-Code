facts = {"bird"}

rules = {
    "bird": "fly",
    "fly": "move"
}

while True:
    new_fact = None
    
    for condition, result in rules.items():
        if condition in facts and result not in facts:
            new_fact = result
            break
        
    if new_fact is None:
            break
        
    facts.add(new_fact)
    
print("Facts:", facts)