#!/usr/bin/env python3
"""Interactive test for Orion assistant"""

from Orion import summarize_day, daily_health, make_poster

def interactive_test():
    """Interactive testing of Orion functions"""
    
    print("=== Orion Interactive Test ===")
    print("Choose a function to test:")
    print("1. Daily Task Summary")
    print("2. Health Tracking")
    print("3. Motivational Poster")
    print("4. Run All Functions")
    print("5. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            print("\n--- Daily Task Summary ---")
            tasks_input = input("Enter tasks separated by commas (or press Enter for no tasks): ")
            if tasks_input.strip():
                tasks = [task.strip() for task in tasks_input.split(",")]
            else:
                tasks = []
            result = summarize_day(tasks)
            print(f"Summary: {result}")
            
        elif choice == "2":
            print("\n--- Health Tracking ---")
            try:
                steps = int(input("Enter steps taken: "))
                calories = int(input("Enter calories burned: "))
                water = int(input("Enter water consumed (ml): "))
                result = daily_health(steps, calories, water)
                print(f"Health Summary: {result}")
            except ValueError:
                print("Please enter valid numbers!")
                
        elif choice == "3":
            print("\n--- Motivational Poster ---")
            quote = input("Enter your motivational quote: ")
            result = make_poster(quote)
            print(f"Poster: {result}")
            
        elif choice == "4":
            print("\n--- Running All Functions ---")
            # Demo with sample data
            tasks = ["Code review", "Team standup", "Workout"]
            print(f"Daily Summary: {summarize_day(tasks)}")
            print(f"Health: {daily_health(7500, 450, 2200)}")
            print(f"Motivation: {make_poster('Keep pushing forward!')}")
            
        elif choice == "5":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice! Please select 1-5.")

if __name__ == "__main__":
    interactive_test()