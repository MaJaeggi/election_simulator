"""
A basic program for generating random outcomes for parliamentary elections. In this case, each city
has a predefined number of seats to elect, and each party has a set % likelihood of electing a party to
each seat.
"""
#import the required libraries
import random

#Define cities and their corresponding number of seats
cities = {
    "Massalia": 24,
    "Agathe": 4,
    "Antipolis": 16,
    "Olbia-Ligystike": 16,
    "Ariston": 28,
    "Rhode": 14
}

#Define the popularity of each party in each city, expressed as a percentage
city_party_percentages = {
    "Massalia": {"SRP": 0.00, "GIP": 0.0, "MPP": 0.2, "PUG": 0.4, "PPM": 0.15, "MDP":0.2 },
    "Agathe": {"SRP": 0.25, "GIP": 0.0, "MPP": 0.40, "PUG": 0.25, "PPM": 0.10},
    "Antipolis": {"SRP": 0.3, "GIP": 0.0, "MPP": 0.20, "PUG": 0.4, "PPM": 0.10},
    "Olbia-Ligystike": {"SRP": 0.15, "GIP": 0.0, "MPP": 0.35, "PUG": 0.4, "PPM": 0.10},
    "Ariston": {"SRP": 0.10, "GIP": 0.50, "MPP": 0.2, "PUG": 0.2, "PPM": 0.0},
    "Rhode": {"SRP": 0.10, "GIP": 0.55, "MPP": 0.15, "PUG": 0.15, "PPM": 0.05}
}

#Define the function to simulate the distribution of votes
def simulate_votes(city, city_party_percentages):
    #Initialise counts for each party
    votes = {party: 0 for party in city_party_percentages[city]}
    
    total_stones = 1000
    for _ in range(total_stones):
        rand_num = random.random()  #Generate a random number between 0 and 1
        cumulative_percentage = 0
        for party, percentage in city_party_percentages[city].items():
            cumulative_percentage += percentage
            if rand_num < cumulative_percentage:
                votes[party] += 1
                break

    return votes

#Simulate the distribution of votes for each city
election_results = {city: simulate_votes(city, city_party_percentages) for city in cities}

#Calculate the number of seats each party won in each city
def calculate_seats(election_results, cities):
    seats_won = {city: {party: 0 for party in city_party_percentages[city]} for city in cities}

    for city, counts in election_results.items():
        total_votes = sum(counts.values())
        available_seats = cities[city]
        total_seats_allocated = 0
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

        for party, votes in sorted_counts:
            seats_won[city][party] = votes // (total_votes / available_seats)
            total_seats_allocated += seats_won[city][party]

        #Allocate remaining seats based on highest remainders
        remaining_seats = available_seats - total_seats_allocated
        while remaining_seats > 0:
            for party, votes in sorted_counts:
                if seats_won[city][party] < available_seats and remaining_seats > 0:
                    seats_won[city][party] += 1
                    remaining_seats -= 1
                else:
                    break

    return seats_won

# Calculate seats won by each party in each city
seats_won = calculate_seats(election_results, cities)

# Print results
for city, seats in seats_won.items():
    print(f"Seats won in {city}:")
    for party, count in seats.items():
        print(f"{party}: {count} seats")
    print()
