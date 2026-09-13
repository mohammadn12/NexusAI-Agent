import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# ---- यहाँ बदलाव किया गया है ----
# desktop/app फ़ाइल से सीधे 'app' (या जो भी नाम हो) को इम्पोर्ट करें
try:
    from desktop.app import app
except ImportError:
    # अगर आपके ऐप का नाम 'app' नहीं कुछ और है, तो हम नीचे फ़ंक्शन चलाएंगे
    app = None

def main():
    try:
        from desktop.app import start_app
        start_app()
    except Exception as error:
        print("\n" + "=" * 60 + "\nNEXUS STARTUP ERROR\n" + "=" * 60)
        print(error)
        print("=" * 60 + "\n")
        input("Press Enter to close...")

if __name__ == "__main__":
    main()
