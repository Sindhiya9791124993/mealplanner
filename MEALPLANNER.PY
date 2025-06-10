import streamlit as st
import google.generativeai as genai # You'll need to install this: pip install google-generativeai

# --- Gemini API Configuration (PLACEHOLDER - REPLACE WITH YOUR ACTUAL KEY) ---
# It's recommended to store your API key securely, e.g., in Streamlit secrets or environment variables.
# For direct integration:
# genai.configure(api_key="AIzaSyCZ5V3tJG4Cq2RTp7PM5WQTrTXiwLngNNQ")

# Placeholder function for Gemini API call for main meal plan
def get_gemini_response(prompt):
    # --- REPLACE THIS WITH YOUR ACTUAL GEMINI API CALL ---
    # try:
    #     model = genai.GenerativeModel('gemini-pro') # Or 'gemini-1.5-pro' for more advanced
    #     response = model.generate_content(prompt)
    #     return response.text
    # except Exception as e:
    #     st.error(f"Error communicating with Gemini API: {e}")
    #     return "Could not generate meal plan. Please try again later."

    # Dummy response for demonstration if API is not set up
    return """
    **Your Weekly Meal Plan (Example Data)**

    **Day 1: Monday - Fresh Start!**
    * **Breakfast:** Tropical Smoothie Bowl ☀️
        * *Description:* A vibrant and refreshing smoothie bowl packed with fruits and a sprinkle of granola.
        * *Image Suggestion:* Image: A colorful smoothie bowl topped with sliced kiwi, mango, and toasted coconut flakes.
        * *Recipe:*
            * **Ingredients (for 1 person):**
                * 1 cup frozen mixed berries
                * 1/2 banana
                * 1/2 cup almond milk (or preferred milk)
                * 1 scoop protein powder (optional)
                * Toppings: 2 tbsp granola, 1/4 cup sliced fresh fruit (e.g., kiwi, mango)
            * **Instructions:**
                1.  Blend frozen berries, banana, milk, and protein powder until smooth.
                2.  Pour into a bowl.
                3.  Arrange granola and fresh fruit on top. Serve immediately.
    * **Lunch:** Mediterranean Quinoa Salad 🥗
        * *Description:* A light yet satisfying salad bursting with Mediterranean flavors and healthy quinoa.
        * *Image Suggestion:* Image: A bright quinoa salad with cherry tomatoes, cucumber, olives, and crumbled feta.
        * *Recipe:*
            * **Ingredients (for 1 person):**
                * 1/2 cup cooked quinoa
                * 1/4 cup chopped cucumber
                * 1/4 cup cherry tomatoes, halved
                * 2 tbsp chopped Kalamata olives
                * 1 oz crumbled feta cheese (optional, omit for vegan)
                * 1 tbsp olive oil
                * 1 tbsp lemon juice
                * Salt and pepper to taste
            * **Instructions:**
                1.  In a bowl, combine cooked quinoa, cucumber, cherry tomatoes, and olives.
                2.  Add feta cheese if using.
                3.  Whisk together olive oil, lemon juice, salt, and pepper. Pour dressing over salad and toss to combine.
    * **Dinner:** One-Pan Lemon Herb Chicken and Veggies 🍗🥦
        * *Description:* A super easy and flavorful dinner that cooks all on one pan for minimal cleanup.
        * *Image Suggestion:* Image: Roasted chicken thighs with vibrant broccoli florets and golden potato wedges on a baking sheet.
        * *Recipe:*
            * **Ingredients (for 1 person):**
                * 1 boneless, skinless chicken thigh or breast
                * 1 cup broccoli florets
                * 1 small potato, cubed
                * 1 tbsp olive oil
                * 1 tsp dried Italian herbs
                * 1/2 lemon, sliced
                * Salt and black pepper to taste
            * **Instructions:**
                1.  Preheat oven to 400°F (200°C).
                2.  On a baking sheet, toss chicken, broccoli, and potato with olive oil, Italian herbs, salt, and pepper.
                3.  Arrange lemon slices over the chicken and veggies.
                4.  Roast for 20-25 minutes, or until chicken is cooked through and vegetables are tender.

    ---

    **Shopping List (Example Data)**
    * **Produce:**
        * Mixed berries (fresh or frozen)
        * Bananas
        * Kiwi
        * Mango
        * Cucumber
        * Cherry tomatoes
        * Kalamata olives
        * Broccoli
        * Potatoes
        * Lemons
    * **Pantry:**
        * Granola
        * Quinoa
        * Olive oil
        * Dried Italian herbs
        * Salt
        * Black pepper
    * **Proteins:**
        * Chicken thighs/breasts
        * Protein powder (optional)
    * **Dairy/Alternatives:**
        * Almond milk (or preferred milk)
        * Feta cheese (optional)
    """

# Placeholder function for Gemini API call for kids' meal plan
def get_kids_gemini_response(prompt):
    # --- REPLACE THIS WITH YOUR ACTUAL GEMINI API CALL ---
    # try:
    #     model = genai.GenerativeModel('gemini-pro') # Or 'gemini-1.5-pro' for more advanced
    #     response = model.generate_content(prompt)
    #     return response.text
    # except Exception as e:
    #     st.error(f"Error communicating with Gemini API: {e}")
    #     return "Could not generate kids' meal plan. Please try again later."

    # Dummy response for demonstration if API is not set up
    return """
    **Kids' Fun & Healthy Meal Plan (Example Data)**

    **Day 1: Super Saturday! 🎉**
    * **Breakfast:** Animal-Shaped Pancakes with Fruit Smiles 🥞😊
        * *Description:* Fluffy pancakes cut into fun animal shapes, decorated with happy fruit faces to start the day with a smile!
        * *Image Suggestion:* Image: Round pancakes cut into bear shapes with banana slices for eyes, a blueberry for a nose, and a strawberry slice for a smile.
        * *Recipe (for 1 child):*
            * **Ingredients:**
                * 1/2 cup whole-wheat pancake mix
                * 1/4 cup milk
                * 1 small banana, sliced
                * 2-3 strawberries, sliced
                * A few blueberries
            * **Instructions:**
                1.  Prepare pancake batter according to package directions using whole-wheat mix and milk.
                2.  Cook small pancakes. Once cooked, use cookie cutters to make animal shapes.
                3.  Arrange banana slices, strawberry slices, and blueberries to create animal faces on the pancakes.
            * **Parent Tip:** Let kids help arrange the fruit faces for extra fun!
    * **Lunch:** Rainbow Veggie & Hummus Pinwheels 🌈🌀
        * *Description:* Colorful tortilla roll-ups filled with creamy hummus and crunchy, vibrant veggies – easy for little hands to hold!
        * *Image Suggestion:* Image: Sliced pinwheel sandwiches showing concentric circles of colorful vegetables and hummus.
        * *Recipe (for 1 child):*
            * **Ingredients:**
                * 1 whole-wheat tortilla
                * 2 tbsp hummus
                * 1 tbsp finely grated carrot
                * 1 tbsp finely diced cucumber
                * 1 tsp finely diced bell pepper (any color)
            * **Instructions:**
                1.  Spread hummus evenly over the tortilla.
                2.  Sprinkle grated carrot, diced cucumber, and diced bell pepper over the hummus.
                3.  Tightly roll up the tortilla.
                4.  Slice the rolled tortilla into 1-inch pinwheels.
            * **Parent Tip:** Offer different colored veggies for a vibrant rainbow!
    * **Dinner:** "Dinosaur" Broccoli Trees & Cheesy Pasta 🍝🦖
        * *Description:* Pasta served with a delicious, cheesy sauce that magically hides some green veggies, alongside "dinosaur trees" (broccoli)!
        * *Image Suggestion:* Image: A bowl of fun-shaped pasta with a creamy orange sauce, and small florets of steamed broccoli arranged next to it like trees.
        * *Recipe (for 1 child):*
            * **Ingredients:**
                * 1/2 cup fun-shaped pasta (e.g., rotini, alphabet, dinosaur)
                * 1/4 cup small broccoli florets
                * 2 tbsp cheese sauce (or 1 tbsp grated cheddar cheese melted into 2 tbsp milk)
                * Pinch of nutritional yeast (optional, for cheesy flavor)
            * **Instructions:**
                1.  Cook pasta according to package directions. Steam broccoli florets until tender-crisp.
                2.  Drain pasta. In the same pot (or a small saucepan), melt cheese with milk (or use prepared cheese sauce). Stir in optional nutritional yeast.
                3.  Toss pasta with cheese sauce. Arrange "dinosaur trees" (broccoli) next to the pasta.
            * **Parent Tip:** Call the broccoli "dinosaur trees" to encourage eating!

    ---

    **Kids' Shopping List (Example Data)**
    * **Produce (Colorful!):**
        * Bananas
        * Strawberries
        * Blueberries
        * Carrots
        * Cucumber
        * Bell pepper (any color)
        * Broccoli
    * **Pantry (Fun Grains!):**
        * Whole-wheat pancake mix
        * Whole-wheat tortillas
        * Hummus
        * Fun-shaped pasta
    * **Dairy/Alternatives:**
        * Milk
        * Cheddar cheese (or preferred cheese sauce)
    """

# --- Page Configuration ---
st.set_page_config(
    page_title="NutriGenie: Your Personalized Meal Planner",
    page_icon="🍎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS for attractiveness ---
st.markdown("""
<style>
    .main-header {
        font-size: 3.5em;
        color: #4CAF50; /* A nice green */
        text-align: center;
        margin-bottom: 30px;
        font-family: 'Arial Black', sans-serif;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    .subheader {
        font-size: 2.2em;
        color: #2E8B57; /* Darker green */
        margin-top: 20px;
        margin-bottom: 15px;
        text-align: center;
        font-weight: bold;
    }
    .stButton>button {
        background-color: #FF6347; /* Tomato red for action buttons */
        color: white;
        font-size: 1.2em;
        padding: 10px 20px;
        border-radius: 10px;
        border: none;
        box-shadow: 3px 3px 6px rgba(0,0,0,0.2);
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #E64A19; /* Darker red on hover */
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 5%; /* Add some padding to the sides */
        padding-right: 5%;
    }
    .recipe-card {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        background-color: #f9f9f9;
    }
    .shopping-list-item {
        font-size: 1.1em;
        margin-bottom: 5px;
    }
    .stImage {
        border-radius: 10px; /* Rounded corners for images */
        box-shadow: 2px 2px 8px rgba(0,0,0,0.3);
    }
    .stSelectbox, .stMultiSelect, .stSlider, .stTextInput, .stNumberInput, .stCheckbox {
        margin-bottom: 15px;
    }
    .stForm {
        padding: 30px;
        border-radius: 15px;
        background-color: #e8f5e9; /* Light green for forms */
        box-shadow: 5px 5px 15px rgba(0,0,0,0.1);
    }
    .info-box {
        background-color: #e0f2f7; /* Light blue for info boxes */
        border-left: 5px solid #2196F3;
        padding: 15px;
        margin-bottom: 20px;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# --- Sidebar Navigation ---
st.sidebar.title("Navigate 🧭")
page = st.sidebar.radio("Go to", ["Home", "My Meal Plan", "Kids' Plan", "About NutriGenie"])

# --- Home Page ---
if page == "Home":
    st.markdown("<h1 class='main-header'>NutriGenie: Your Personalized Meal Planner 🍎✨</h1>", unsafe_allow_html=True)
    # Using an Unsplash URL for a hero image
    st.image("https://images.unsplash.com/photo-1540189549336-e6e7682779c2?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w1MDc5OTd8MHwxfHNlYXJjaHw1fHxoZWFsdGh5JTIwZm9vZHxlbnwxNzE3NTk4NDg2fDA&ixlib=rb-4.0.3&q=80&w=1080", use_column_width=True, caption="Fuel your body, nourish your life!")
    st.markdown("""
    <p style="font-size: 1.3em; text-align: center; margin-top: 30px; line-height: 1.6;">
    Welcome to <strong>NutriGenie</strong>, your ultimate companion for achieving your health and fitness goals!
    </p>
    <p style="font-size: 1.1em; text-align: center; margin-top: 15px; line-height: 1.6;">
    Simply tell us your preferences and aspirations, and our powerful AI will conjure up a delicious weekly meal plan, complete with exciting recipes and a smart shopping list.
    </p>
    """, unsafe_allow_html=True)
    st.markdown("<div class='info-box' style='text-align: center;'>Navigate to 'My Meal Plan' to get started on your healthy journey! ✨</div>", unsafe_allow_html=True)


# --- My Meal Plan Page ---
elif page == "My Meal Plan":
    st.markdown("<h2 class='subheader'>Design Your Personalized Meal Plan 📋</h2>", unsafe_allow_html=True)
    st.markdown("""
    <p style="font-size: 1.1em; text-align: center; margin-bottom: 30px;">
    Tell us about your dietary needs and goals, and let NutriGenie craft the perfect plan for you!
    </p>
    """, unsafe_allow_html=True)

    with st.form("meal_plan_form", clear_on_submit=True):
        col1, col2 = st.columns(2)

        with col1:
            dietary_preference = st.multiselect(
                "🥗 **Dietary Preferences:**",
                ["None", "Vegetarian", "Vegan", "Keto", "Paleo", "Gluten-Free", "Dairy-Free", "Pescatarian", "Low-Carb", "High-Protein"],
                default="None"
            )
            goals = st.multiselect(
                "🎯 **Health Goals:**",
                ["Weight Loss", "Muscle Gain", "Maintenance", "Healthy Eating", "Energy Boost", "Improved Digestion"],
                default="Healthy Eating"
            )
            allergies = st.text_input("⚠️ **Allergies (e.g., peanuts, shellfish, soy - comma separated):**")
            cuisine_preference = st.multiselect(
                "🌎 **Cuisine Preferences (optional):**",
                ["Italian", "Mexican", "Asian (General)", "Indian", "Mediterranean", "American", "Thai", "Middle Eastern", "No Preference"]
            )

        with col2:
            cooking_time = st.slider("⏰ **Max time per meal (minutes):**", 15, 120, 45, step=5)
            cooking_skill = st.select_slider(
                "🔪 **Your Cooking Skill Level:**",
                options=["Beginner", "Intermediate", "Advanced"]
            )
            num_people = st.number_input("👨‍👩‍👧‍👦 **Number of adults to plan for:**", 1, 10, 1)
            # Add an optional field for disliked ingredients
            disliked_ingredients = st.text_input("🤢 **Ingredients you dislike (e.g., cilantro, mushrooms - comma separated):**")

        st.markdown("---") # Separator for better UI
        submitted = st.form_submit_button("✨ Generate My Meal Plan!")

        if submitted:
            # Store inputs in session state to persist after rerun (due to form submit)
            st.session_state.dietary_preference = dietary_preference
            st.session_state.goals = goals
            st.session_state.allergies = allergies
            st.session_state.cooking_time = cooking_time
            st.session_state.cooking_skill = cooking_skill
            st.session_state.cuisine_preference = cuisine_preference
            st.session_state.num_people = num_people
            st.session_state.disliked_ingredients = disliked_ingredients
            st.session_state.show_meal_plan = True # Flag to show the plan

    if st.session_state.get('show_meal_plan'):
        with st.spinner("Conjuring your delicious meal plan... please wait! 🧙‍♀️"):
            user_prompt = f"""
            Create a detailed 7-day weekly meal plan including breakfast, lunch, and dinner, along with recipes and a comprehensive shopping list.
            The plan should cater to the following:
            - Dietary Preferences: {', '.join(st.session_state.dietary_preference) if st.session_state.dietary_preference else 'None'}
            - Health Goals: {', '.join(st.session_state.goals) if st.session_state.goals else 'Healthy Eating'}
            - Allergies: {st.session_state.allergies if st.session_state.allergies else 'None'}
            - Max cooking time per meal: {st.session_state.cooking_time} minutes
            - Cooking Skill Level: {st.session_state.cooking_skill}
            - Cuisine Preferences: {', '.join(st.session_state.cuisine_preference) if st.session_state.cuisine_preference else 'No Preference'}
            - Number of adults: {st.session_state.num_people}
            - Disliked Ingredients: {st.session_state.disliked_ingredients if st.session_state.disliked_ingredients else 'None'}

            For each meal, provide:
            1.  **Meal Name**
            2.  **A short, enticing description**
            3.  **A suggestion for a relevant image (e.g., "Image: A vibrant smoothie bowl")** - *Crucial for visual appeal!*
            4.  **Full Recipe:** Ingredients (with quantities adjusted for {st.session_state.num_people} people), step-by-step instructions.

            After the 7-day plan, provide a consolidated **Shopping List** categorized by type (e.g., Produce, Pantry, Proteins, Dairy).
            Ensure the language is encouraging and positive. Make it sound delicious and easy to follow.
            """

            gemini_output = get_gemini_response(user_prompt)

            st.success("Your personalized meal plan is ready! 🎉")
            st.markdown("---")
            st.markdown("<h3 class='subheader'>Your Weekly Meal Plan & Recipes</h3>", unsafe_allow_html=True)
            st.markdown(gemini_output, unsafe_allow_html=True) # Gemini's output will be markdown formatted


# --- Kids' Plan Page ---
elif page == "Kids' Plan":
    st.markdown("<h2 class='subheader'>Fun & Healthy Meal Plans for Kids! 👧👦</h2>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1574737604473-b615c0e12e3e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w1MDc5OTd8MHwxfHNlYXJjaHw1fHxoZWFsdGh5JTIwa2lkcyUyMGZvb2R8ZW58MTcxNzU5ODU2NHww&ixlib=rb-4.0.3&q=80&w=1080", use_column_width=True, caption="Making healthy eating fun for little ones!")

    st.markdown("""
    <p style="font-size: 1.1em; text-align: center; margin-bottom: 30px;">
    Get creative and nutritious meal ideas for your children. Our plans focus on making healthy food appealing and easy to eat, even for picky eaters!
    </p>
    """, unsafe_allow_html=True)

    with st.form("kids_meal_plan_form", clear_on_submit=True):
        col3, col4 = st.columns(2)

        with col3:
            kids_age_group = st.multiselect(
                "👶 **Kids' Age Group(s):**",
                ["Toddler (1-3)", "Preschool (3-5)", "School Age (6-12)", "Teen (13-18)"]
            )
            kids_allergies = st.text_input("⚠️ **Kids' Allergies (e.g., nuts, dairy - comma separated):**")
            num_kids = st.number_input("🧒 **Number of children:**", 1, 5, 1)

        with col4:
            picky_eater = st.checkbox("🤪 **Are they picky eaters?** (We'll suggest ways to hide veggies!)")
            kids_disliked_food = st.text_input("🤢 **Foods your kids dislike (e.g., broccoli, spinach - comma separated):**")
            fun_elements = st.multiselect(
                "🎨 **Fun elements to include:**",
                ["Fun Shapes", "Hidden Veggies", "Colorful Meals", "Dipping Sauces", "Kid-Friendly Themes"]
            )

        st.markdown("---") # Separator for better UI
        submitted_kids = st.form_submit_button("🌈 Generate Kids' Meal Plan!")

        if submitted_kids:
            st.session_state.kids_age_group = kids_age_group
            st.session_state.kids_allergies = kids_allergies
            st.session_state.picky_eater = picky_eater
            st.session_state.num_kids = num_kids
            st.session_state.kids_disliked_food = kids_disliked_food
            st.session_state.fun_elements = fun_elements
            st.session_state.show_kids_plan = True

    if st.session_state.get('show_kids_plan'):
        with st.spinner("Whipping up a fun plan for your little ones... 🧚"):
            kids_prompt = f"""
            Design a fun, healthy, and appealing 7-day weekly meal plan specifically for children, including breakfast, lunch, and dinner for each day. Provide kid-friendly recipes and a comprehensive shopping list.
            The plan should cater to:
            - Kids' Age Group(s): {', '.join(st.session_state.kids_age_group) if st.session_state.kids_age_group else 'All ages'}
            - Kids' Allergies: {st.session_state.kids_allergies if st.session_state.kids_allergies else 'None'}
            - Picky Eaters: {'Yes, incorporate strategies for picky eaters like hidden veggies and fun shapes.' if st.session_state.picky_eater else 'No'}
            - Number of children: {st.session_state.num_kids}
            - Disliked Foods: {st.session_state.kids_disliked_food if st.session_state.kids_disliked_food else 'None'}
            - Fun Elements to Include: {', '.join(st.session_state.fun_elements) if st.session_state.fun_elements else 'Standard'}


            For each meal, provide:
            1.  **Meal Name (fun and catchy)**
            2.  **A short, enticing description for kids**
            3.  **A suggestion for a relevant, kid-friendly image (e.g., "Image: Animal-shaped sandwiches")** - *Crucial!*
            4.  **Full Recipe:** Simple ingredients (with quantities adjusted for {st.session_state.num_kids} children), easy step-by-step instructions. Include tips for presentation to make it appealing to kids.

            After the 7-day plan, provide a consolidated **Kids' Shopping List** categorized.
            Emphasize colors, shapes, and hidden veggies. Make it sound exciting for both parents and kids!
            """

            kids_gemini_output = get_kids_gemini_response(kids_prompt)

            st.success("Your kids' meal plan is ready! 🌈👶")
            st.markdown("---")
            st.markdown("<h3 class='subheader'>Your Kids' Weekly Meal Plan & Recipes</h3>", unsafe_allow_html=True)
            st.markdown(kids_gemini_output, unsafe_allow_html=True)


# --- About Page (Optional) ---
elif page == "About NutriGenie":
    st.markdown("<h2 class='subheader'>About NutriGenie 🌟</h2>", unsafe_allow_html=True)
    st.markdown("""
    <p style="font-size: 1.1em; line-height: 1.6;">
    NutriGenie is your intelligent meal planning assistant, powered by cutting-edge AI (Google Gemini!). Our mission is to transform the way you approach healthy eating by providing personalized, delicious, and easy-to-follow meal plans tailored to your unique dietary preferences and health goals.
    </p>
    <p style="font-size: 1.1em; line-height: 1.6;">
    We believe that healthy eating should be enjoyable, sustainable, and accessible for everyone, including the little ones! That's why we've also included a special feature for fun and nutritious kids' meal plans.
    </p>
    <p style="font-size: 1.1em; line-height: 1.6;">
    Developed with passion by a team dedicated to making healthy living simpler and more exciting.
    </p>
    """, unsafe_allow_html=True)
    st.write("For support or inquiries, contact us at: **support@nutrigenie.com**")
    st.markdown("---")
    st.write("Follow us on social media for healthy tips and updates! (Links coming soon!)")