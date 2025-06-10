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

# Shopping list items per diet
SHOPPING_ITEMS = {
    "vegan": ["Tofu", "Lentils", "Chickpeas", "Vegetables"],
    "vegetarian": ["Eggs", "Cheese", "Yogurt", "Vegetables"],
    "keto": ["Meat", "Eggs", "Avocado", "Low-carb vegetables"]
}

def generate_meal_plan(diet: str, days: int = 7) -> dict:
    return {
        f"Day {day}": {
            "Breakfast": random.choice(MEAL_DATABASE[diet]["breakfast"]),
            "Lunch": random.choice(MEAL_DATABASE[diet]["lunch"]),
            "Dinner": random.choice(MEAL_DATABASE[diet]["dinner"]),
        }
        for day in range(1, days + 1)
    }

# Streamlit UI
st.set_page_config(page_title="Meal Plan Generator", page_icon="🍽️")
st.title("🍽️ Personalized Meal Plan Generator")

with st.sidebar:
    st.header("Settings")
    diet = st.selectbox(
        "Select your dietary preference:",
        ["Vegan", "Vegetarian", "Keto", "Paleo", "Mediterranean", "Omnivore"]
    ).lower()

    goal = st.selectbox(
        "Choose your goal:",
        ["Weight Loss", "Muscle Gain", "Maintenance"]
    )

    days = st.slider("Number of days to plan for:", min_value=1, max_value=14, value=7)

if st.button("Generate Meal Plan"):
    if diet not in MEAL_DATABASE:
        st.error(f"🚫 Sorry, we don't support the '{diet.capitalize()}' diet yet.")
    else:
        with st.spinner("Creating your personalized meal plan..."):
            meal_plan = generate_meal_plan(diet, days)

        st.success("✅ Your weekly meal plan is ready!")

        st.subheader("📅 Weekly Meal Plan")
        for day, meals in meal_plan.items():
            with st.expander(day):
                for meal_type, meal in meals.items():
                    st.markdown(f"**{meal_type}**: {meal}")

        st.subheader("🛒 Shopping List")
        st.markdown("\n".join(f"- {item}" for item in SHOPPING_ITEMS[diet]))

        st.subheader("🍳 Tips for Success")
        st.markdown("""
        - 🥗 Adjust portion sizes to fit your goal  
        - 💧 Stay hydrated throughout the day  
        - 🥣 Consider meal prepping to save time during the week  
        - 🛍️ Check your pantry before shopping  
        """)

st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
