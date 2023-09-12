# Problem Statement: Employee Performance Evaluation

def calculate_performance_scores(employees):
    result = []

    for employee in employees:
        name = employee['name']  # return the name
        scores = employee['scores']
        weights = employee['weights']

        # Calculate the weighted sum of scores for each criterion
        weighted_sum = sum(scores[criterion] * weights[criterion] for criterion in scores)

        # Create a dictionary for the employee's performance
        performance = {
            'name': name,
            'performance_score': weighted_sum
        }

        result.append(performance)

    return result


emp = [
    {"name": "John", "scores": {"Quality of Work": 90, "Team Collaboration": 80}, "weights": {"Quality of Work": 0.6, "Team Collaboration": 0.4}},
    {"name": "Alice", "scores": {"Quality of Work": 85, "Team Collaboration": 95}, "weights": {"Quality of Work": 0.5, "Team Collaboration": 0.5}},
   ]

print(calculate_performance_scores(emp))

# Q/p: [{'name': 'John', 'performance_score': 86.0}, {'name': 'Alice', 'performance_score': 90.0}]
