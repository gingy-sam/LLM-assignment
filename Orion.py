# Orion.py
# Simple personal assistant using Google Gemini API

import random
import re
from datetime import date
from pathlib import Path

import google.generativeai as genai

genai.configure(api_key="AIzaSyD4eAP1_to0pxgNVZ4BlJj8V1xE_mD8U7E")
MODEL = "gemini-2.0-flash"
BASE_DIR = Path(__file__).resolve().parent


def summarize_day(tasks):
    """Quick summary of tasks for the day."""
    if not tasks:
        return "No tasks today. Maybe relax?"
    joined = "; ".join(tasks)
    return f"{date.today().strftime('%B %d')}: {joined}."


def _resolve_photo_path(photo_path):
    photo_path = Path(photo_path)
    if not photo_path.is_absolute():
        photo_path = BASE_DIR / photo_path
    return photo_path


def _clean_meal_names(raw_text):
    cleaned = []
    for line in raw_text.splitlines():
        stripped = re.sub(r"^[\s\-\*\d\.)]+", "", line).strip()
        if stripped:
            cleaned.append(stripped)
    return "\n".join(cleaned) if cleaned else raw_text


def meal_from_fridge(photo_path):
    """Suggest meal ideas strictly by name based on a fridge image."""
    photo_path = _resolve_photo_path(photo_path)
    with open(photo_path, "rb") as img:
        data = img.read()
    model = genai.GenerativeModel(MODEL)
    prompt = (
        "Look at this fridge photo and infer three possible healthy meal ideas I could make. "
        "Respond with only the meal names separated by new lines. Do not include ingredients or descriptions."
    )
    response = model.generate_content([
        prompt,
        {"mime_type": "image/jpeg", "data": data},
    ])
    return _clean_meal_names(response.text.strip())


def comfort_puppy():
    """Provide a comforting puppy description when image generation is unavailable."""
    prompt = (
        "Offer a short, uplifting description of an adorable puppy to cheer someone up. "
        "Keep it to two sentences."
    )
    try:
        model = genai.GenerativeModel(MODEL)
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as err:
        return f"Could not fetch a puppy boost right now: {err}"


def pick_video_game():
    """Pick a random video game for the evening."""
    suggestions = [
        "Stardew Valley",
        "Hades",
        "Mario Kart 8 Deluxe",
        "Animal Crossing: New Horizons",
        "The Legend of Zelda: Tears of the Kingdom",
        "Overcooked! 2",
        "Rocket League",
        "Minecraft",
        "Fortnite",
        "Hollow Knight",
    ]
    return random.choice(suggestions)


def workout_split():
    """Return a simple four-day workout split."""
    split_plan = [
        "Day 1 - Push: Chest, shoulders, triceps",
        "Day 2 - Pull: Back, biceps, rear delts",
        "Day 3 - Legs: Quads, hamstrings, calves",
        "Day 4 - Active Recovery: Core work and light cardio",
    ]
    return "\n".join(split_plan)


def daily_summary_action():
    schedule = ["Morning jog", "Work project", "Call with John", "Do homework"]
    print(summarize_day(schedule))


def meal_ideas_action():
    try:
        print(meal_from_fridge("fridge.jpg"))
    except FileNotFoundError:
        print("Fridge image not found. Add 'fridge.jpg' next to Orion.py to use this option.")
    except Exception as err:
        print(f"Error analyzing fridge: {err}")


def puppy_action():
    print(comfort_puppy())


def video_game_action():
    print(f"Play this tonight: {pick_video_game()}")


def workout_action():
    print(workout_split())


def main():
    actions = {
        "1": ("Daily schedule summary", daily_summary_action),
        "2": ("Meal ideas from fridge.jpg", meal_ideas_action),
        "3": ("Cheer up with a cute puppy", puppy_action),
        "4": ("Pick a video game for tonight", video_game_action),
        "5": ("Get a workout split", workout_action),
    }

    while True:
        print("\n=== Orion Personal Assistant ===")
        for key, (label, _) in actions.items():
            print(f"{key}. {label}")
        print("0. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "0":
            print("See you next time!")
            break

        action = actions.get(choice)
        if not action:
            print("Invalid selection. Try again.")
            continue

        label, handler = action
        print(f"\n--- {label} ---")
        handler()
        print()


if __name__ == "__main__":
    main()
