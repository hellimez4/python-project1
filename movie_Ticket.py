# Movie Theater Booking System

#/*Simulate a movie theater booking system that:
#1. Shows a list of available movie titles, showtimes, and seat prices.
#2. Asks the user to choose a movie and number of tickets.
#3. Confirms total price and asks if they want to book another movie.
#4. Ends when they say “no” and displays total bookings and cost.
#skills practiced: loops, input, conditionals, calculations, nested dictionaries.

movies = {
    1: {"title": "Eternity", "showtime": "6:00 PM", "price": 12},
    2: {"title": "zootopia", "showtime": "7:30 PM", "price": 10},
    3: {"title": "David", "showtime": "8:45 PM", "price": 8}
}

total_cost = 0
total_bookings = 0

print("🎬 Welcome to the Movie Theater Booking System!\n")

while True:
    # Display movies
    print("Available Movies:")
    for movie_id, details in movies.items():
        print(f"{movie_id}. {details['title']} - {details['showtime']} - ${details['price']} per ticket")

    # Movie selection
    try:
        choice = int(input("\nEnter the movie number you want to book: "))
        if choice not in movies:
            print("Invalid movie number. Please try again.\n")
            continue
    except ValueError:
        print("Please enter a number.\n")
        continue

    # Number of tickets
    try:
        tickets = int(input(f"How many tickets for {movies[choice]['title']}? "))
        if tickets <= 0:
            print("Ticket count must be positive.\n")
            continue
    except ValueError:
        print("Please enter a valid number.\n")
        continue

    # Price calculation
    price = movies[choice]["price"] * tickets
    print(f"Total price: ${price}")

    # Update totals
    total_cost += price
    total_bookings += 1

    # Continue?
    again = input("Would you like to book another movie? (yes/no): ").lower()
    if again == "no":
        break
    print()

# Final summary
print("\n🎉 Booking Summary 🎉")
print(f"Total movies booked: {total_bookings}")
print(f"Total cost: ${total_cost}")
print("Thank you for booking with us!")
