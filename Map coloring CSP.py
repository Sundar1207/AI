def map_coloring():
    colors = ['Red', 'Green', 'Blue']
    regions = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    neighbors = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['Q', 'SA', 'V'],
        'V': ['SA', 'NSW'],
        'T': []
    }
    
    assignment = {}
    
    def backtrack(assignment):
        if len(assignment) == len(regions):
            return assignment
        
        var = select_unassigned_variable(assignment, regions)
        for value in order_domain_values(var, assignment):
            if is_consistent(var, value, assignment):
                assignment[var] = value
                result = backtrack(assignment)
                if result is not None:
                    return result
                del assignment[var]
        return None
    
    def select_unassigned_variable(assignment, regions):
        unassigned = [r for r in regions if r not in assignment]
        return unassigned[0]
    
    def order_domain_values(var, assignment):
        return colors
    
    def is_consistent(var, color, assignment):
        for neighbor in neighbors[var]:
            if neighbor in assignment and assignment[neighbor] == color:
                return False
        return True
    
    return backtrack(assignment)

print(map_coloring())
