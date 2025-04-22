import numpy as np

np.random.seed(42)

states = ['Sunny', 'Cloudy', 'Rainy']
state_indices = {state: idx for idx, state in enumerate(states)}

transition_matrix = np.array([
    [0.7, 0.2, 0.1],  # Sunny -> Sunny, Cloudy, Rainy
    [0.3, 0.4, 0.3],  # Cloudy -> Sunny, Cloudy, Rainy
    [0.2, 0.5, 0.3]   # Rainy -> Sunny, Cloudy, Rainy
])

def simulate_weather(days, start_state):
    current_state = state_indices[start_state]
    weather_sequence = [states[current_state]]
    
    for _ in range(days - 1):
        current_state = np.random.choice(
            [0, 1, 2],
            p=transition_matrix[current_state]
        )
        weather_sequence.append(states[current_state])
    
    return weather_sequence

def count_rainy_days(sequence):
    return sum(1 for day in sequence if day == 'Rainy')

n_simulations = 10000
days = 10
start_state = 'Sunny'
rainy_threshold = 3

rainy_days_count = 0
for _ in range(n_simulations):
    sequence = simulate_weather(days, start_state)
    if count_rainy_days(sequence) >= rainy_threshold:
        rainy_days_count += 1

probability = rainy_days_count / n_simulations

print("Transition Matrix:")
print(transition_matrix)
print("\nExample 10-day weather sequence starting from Sunny:")
print(simulate_weather(days, start_state))
print(f"\nProbability of at least {rainy_threshold} rainy days in {days} days: {probability:.4f}")
