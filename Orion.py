# Orion.py
# Simple personal assistant using Google Gemini API

import google.generativeai as genai
from datetime import date
from pathlib import Path

genai.configure(api_key="AIzaSyD4eAP1_to0pxgNVZ4BlJj8V1xE_mD8U7E")
MODEL = "gemini-2.0-flash"
BASE_DIR = Path(__file__).resolve().parent

#5 Functions

def summarize_day(tasks):
    """Quick summary of tasks for the day."""
    if not tasks:
        return "No tasks today. Maybe relax?"
    joined = "; ".join(tasks)
    return f"{date.today().strftime('%B %d')}: {joined}."

def outfit_suggestion(photo_path):
    """Use Gemini to suggest an outfit from wardrobe image."""
    photo_path = Path(photo_path)
    if not photo_path.is_absolute():
        photo_path = BASE_DIR / photo_path
    with open(photo_path, "rb") as img:
        data = img.read()
    model = genai.GenerativeModel(MODEL)
    result = model.generate_content([
        "This is a photo of clothes. Suggest a simple outfit for casual wear.",
        {"mime_type": "image/jpeg", "data": data},
    ])
    return result.text.strip()

def meal_from_fridge(photo_path):
    """Suggest a meal idea based on fridge contents image."""
    photo_path = Path(photo_path)
    if not photo_path.is_absolute():
        photo_path = BASE_DIR / photo_path
    with open(photo_path, "rb") as img:
        data = img.read()
    model = genai.GenerativeModel(MODEL)
    res = model.generate_content([
        "Look at this fridge photo and suggest something healthy I could make.",
        {"mime_type": "image/jpeg", "data": data},
    ])
    return res.text.strip()

def make_poster(text):
    """Generate an image poster with a motivational quote."""
    # Note: Image generation may not be available in all regions
    # For now, return a text-based motivational message
    return f"Motivational Quote: '{text}' - Stay motivated!"

def daily_health(steps, calories, water):
    """Basic health recap."""
    msg = f"Steps: {steps} | Calories burned: {calories} | Water: {water}ml"
    if water < 2000:
        msg += " (Drink more water!)"
    return msg

# ---------------- Main Program ---------------- #

def main():
    print("=== Orion Personal Assistant ===\n")

    # 1. Daily summary
    schedule = ["Morning jog", "Work project", "Call with Sam", "Grocery run"]
    print(summarize_day(schedule), "\n")

    # 2. Wardrobe check (image reasoning)
    try:
        outfit = outfit_suggestion("wardrobe.jpg")
        print("Outfit suggestion:", outfit, "\n")
    except FileNotFoundError:
        print("Wardrobe image not found. Please add 'wardrobe.jpg' to test this feature.\n")
    except Exception as err:
        print(f"Error analyzing wardrobe: {err}\n")

    # 3. Fridge meal (image reasoning)
    try:
        meal = meal_from_fridge("fridge.jpg")
        print("Meal idea:", meal, "\n")
    except FileNotFoundError:
        print("Fridge image not found. Please add 'fridge.jpg' to test this feature.\n")
    except Exception as err:
        print(f"Error analyzing fridge: {err}\n")

    # 4. Motivational poster (image generation)
    poster_path = make_poster("Small progress is still progress.")
    print("Motivational poster saved as:", poster_path, "\n")

    # 5. Fitness summary
    print(daily_health(6500, 400, 1800))

if __name__ == "__main__":
    main()
