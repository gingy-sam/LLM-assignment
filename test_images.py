#!/usr/bin/env python3
"""Custom test script for image features"""

from Orion import outfit_suggestion, meal_from_fridge
import os

def test_images():
    """Test the image analysis features individually"""
    
    print("=== Testing Orion Image Analysis ===\n")
    
    # Test wardrobe analysis
    if os.path.exists("wardrobe.jpg"):
        print("🔍 Analyzing your wardrobe...")
        try:
            outfit = outfit_suggestion("wardrobe.jpg")
            print(f"👕 Outfit Suggestion:\n{outfit}\n")
        except Exception as e:
            print(f"❌ Error: {e}\n")
    else:
        print("📷 No wardrobe.jpg found - add one to test outfit suggestions\n")
    
    # Test fridge analysis  
    if os.path.exists("fridge.jpg"):
        print("🔍 Analyzing your fridge...")
        try:
            meal = meal_from_fridge("fridge.jpg")
            print(f"🍽️ Meal Suggestion:\n{meal}\n")
        except Exception as e:
            print(f"❌ Error: {e}\n")
    else:
        print("📷 No fridge.jpg found - add one to test meal suggestions\n")
    
    print("✅ Image analysis complete!")

if __name__ == "__main__":
    test_images()