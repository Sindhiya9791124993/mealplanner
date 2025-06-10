import streamlit as st
import random

# Meal database
MEAL_DATABASE = {
    "vegan": {
        "breakfast": ["Oatmeal with berries", "Tofu scramble", "Avocado toast"],
        "lunch": ["Lentil soup", "Chickpea salad", "Vegan buddha bowl"],
        "dinner": ["Vegetable stir-fry", "Vegan chili", "Mushroom risotto"]
    },
    "vegetarian": {
        "breakfast": ["Greek yogurt with granola", "Vegetable omelette", "Smoothie bowl"],
        "lunch": ["Caprese salad", "Vegetable lasagna", "Quinoa salad"],
        "dinner": ["Stuffed bell peppers", "Paneer tikka masala", "Spinach ricotta pasta"]
    },
    "keto": {
        "breakfast": ["Bacon and eggs", "Avocado smoothie", "Chia pudding"],
        "lunch": ["Cauliflower rice bowl", "Bunless burger", "Cobb salad"],
        "dinner": ["Steak with butter", "Salmon with asparagus", "Chicken alfredo"]
    }
}

SHOPPING_ITEMS = {
    "vegan": ["Tofu", "Lentils", "Chickpeas", "Vegetables"],
    "vegetarian": ["Eggs", "Cheese", "Yogurt", "Vegetables"],
    "keto": ["Meat", "Eggs", "Avocado", "Low-carb vegetables"]
}

def generate_meal_plan(diet, days=7):
    plan = {}
    for day in range(1, days + 1):
        plan[f"Day {day}"] = {
            "Breakfast": random.choice(MEAL_DATABASE[diet]["breakfast"]),
            "Lunch": random.choice(MEAL_DATABASE[diet]["lunch"]),
            "Dinner": random.choice(MEAL_DATABASE[diet]["dinner"])
        }
    return plan

# Streamlit UI
st.title("🍽️ Meal Plan Generator")

col1, col2 = st.columns(2)
with col1:
    diet = st.selectbox(
        "Dietary Preference:",
        ["Vegan", "Vegetarian", "Keto", "Paleo", "Mediterranean", "Omnivore"]
    ).lower()

with col2:
    goal = st.selectbox(
        "Goal:",
        ["Weight Loss", "Muscle Gain", "Maintenance"]
    )

if st.button("Generate Meal Plan"):
    with st.spinner("Creating your personalized meal plan..."):
        meal_plan = generate_meal_plan(diet)
        
        st.success("Here's your weekly meal plan!")
        st.subheader("📅 Weekly Meal Plan")
        
        for day, meals in meal_plan.items():
            with st.expander(f"{day}"):
                for meal_type, meal in meals.items():
                    st.markdown(f"**{meal_type}**: {meal}")
        
        st.subheader("🛒 Shopping List")
        for item in SHOPPING_ITEMS.get(diet, []):
            st.markdown(f"- {item}")
        
        st.subheader("🍳 Recipe Suggestions")
        st.markdown("""
        - Adjust portion sizes based on your calorie needs
        - Drink plenty of water throughout the day
        - Meal prep on Sundays for easier weekdays
        """)
