import time
import pytesseract
from PIL import ImageGrab
from collections import Counter

# Ensure Tesseract OCR is installed and pytesseract is correctly configured
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

value_list = {
    # Tier 1
    "Party_Balloons": 11.5,
    "Spooky_Brew": 10.5,
    "Pumpkin_Slice": 8.0,
    "Devilish_Flame": 6.0,
    "Dark_Bone": 5.0,
    "Gothic_Rose": 5.0,
    "Sinister_Seas": 5.0,
    "Soulless_Theater": 5.0,
    "Blood_Bounty": 4.8,
    "Devilborn": 4.8,
    "Phantom_Light": 4.2,

    # Tier 2
    "Lovesick": 4.0,
    "Merry_Music": 3.4,
    "Marine_Anchor": 3.0,
    "Egg_Basket": 3.0,
    "Acidic_Potions": 2.7,
    "Dark_Mansion": 2.7,
    "Yuletide_Gift": 2.5,
    "Blossom": 2.5,
    "Magic_Portal": 2.5,
    "Pot_O'_Gold": 2.5,
    "Candelabra": 2.4,

    # Tier 3
    "Strawberry": 2.3,
    "Pegasus_Blade": 2.0,
    "Lemon": 1.9,
    "Blueberry": 1.9,
    "Clock": 1.8,
    "Marching_Drums": 1.6,
    "Piñata": 1.6,
    "Inferno_Phoenix": 1.5,
    "Santa's_Surprise": 1.5,
    "2nd_Anniversary": 1.2,

    # Tier 4
    "Witch_Hunter": 1.1,
    "Light_Bone": 1.1,
    "Midnight_Light": 1.0,
    "Toy_Box": 1.0,
    "Cocoa_Maker": 1.0,
    "Warlock_Hunter": 1.0,
    "Alchemist_Hunter": 1.0,
    "Doomthrust": 1.0,
    "Frost_Engine": 0.95,
    "Coffin": 0.85,
    "Lucky": 0.85,

    # Tier 5
    "Mothership": 0.75,
    "Santa_Boot": 0.7,
    "Snowglobe": 0.7,
    "Tombstone": 0.65,
    "Candy_Cane_Bar": 0.65,
    "Red_Nutcracker": 0.65,
    "2019": 0.65,
    "Snowman": 0.55,
    "Toy_Santa": 0.5,
    "Lil_Tree": 0.5,
    "Santa_Chimney": 0.5,

    # Tier 6
    "Mystical_Trident": 0.4,
    "Ancestral_Trident": 0.4,
    "Ancient_Trident": 0.4,
    "3rd_Anniversary": 0.35,
    "1_Billion": 0.35,
    "2020": 0.3,
    "Blue_Nutcracker": 0.3,
    "Krampus": 0.3,
    "Toy_Elf": 0.3,
    "BLM": 0.3,
    "Fish_Tank": 0.3,

    # Tier 7
    "Dave_Pumpkins": 0.3,
    "Moonstone": 0.25,
    "Vintage_TV": 0.25,
    "Circus_Cage": 0.25,
    "Spookpumpkin": 0.25,
    "Deathberry": 0.25,
    "Scareapple": 0.25,
    "2021": 0.2,
    "2022": 0.2,
    "4th_Anniversary": 0.2,
    "5th_Anniversary": 0.2,

    # Tier 8
    "2023": 0.2,
    "6th_Anniversary": 0.2,
    "Celestial_Broom": 0.2,
    "Lunar_Broom": 0.2,
    "Solar_Broom": 0.2,
    "Owl_Tree": 0.2,
    "Fortune_Teller": 0.15,
    "Autumn_Harvest": 0.15,
    "Chromatic": 0.15,
    "Winter's_Wreath": 0.15,
    "Festive_Train": 0.15,

    # Tier 9
    "Winter_Train": 0.15,
    "Sweet_Train": 0.15,
    "2024": 0.15,
    "Cold_Hour": 0.15,
    "Cozy_Cocoa": 0.15,
    "Festive_Pinecone": 0.15,
    "Jingle_Bells": 0.15,
    "Eggnog_Maker": 0.15,
    "Stack_of_Presents": 0.15,
    "Gingerbread": 0.15,
    "Cursed_Circus": 0.15,

    # Tier 10
    "Haunted_Circus": 0.15,
    "Enchanted_Circus": 0.15,
    "Irish_Harp": 0.1,
    "Honey_Tree": 0.1,
    "Mycelium": 0.1,
    "Fungal": 0.1,
    "Shroomy": 0.1,
    "Watering_Can": 0.1,
    "Ancient_Portal": 0.1,
    "7th_Anniversary": 0.1,
    "Fairy_Tale_Book": 0.1,
}

def calculate_trade_value(items):
    """Calculate the total value of a set of items."""
    total_value = 0
    for item in items:
        total_value += value_list.get(item, 0)  # Default to 0 if item not in value_list
    return total_value

def monitor_trade_area(bounding_box):
    """Monitors the trade area on the screen and calculates trade values."""
    previous_trade_state = Counter()  # Keeps track of the last detected state

    while True:
        # Capture the trade area on screen
        screenshot = ImageGrab.grab(bbox=bounding_box)
        detected_text = pytesseract.image_to_string(screenshot)

        # Parse item names (split by newlines or spaces)
        current_items = [item.strip() for item in detected_text.splitlines() if item.strip() in value_list]

        # Compare with previous state to detect changes
        current_trade_state = Counter(current_items)
        if current_trade_state != previous_trade_state:
            # Calculate values for traded and received items
            trade_value = calculate_trade_value(current_trade_state.keys())
            print(f"Current Trade Value: {trade_value}")
            previous_trade_state = current_trade_state

        # Pause for a short time before the next check
        time.sleep(0.5)

# Define the bounding box for the trade area on your screen (left, top, right, bottom)
# You need to adjust these coordinates based on your screen resolution and trade window position
bounding_box = (449, 226, 1468, 805)

print("Monitoring trade area...")
monitor_trade_area(bounding_box)
