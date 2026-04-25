
import csv
import json
import sys
from datetime import datetime

CSV_FILE = "training_data.csv"
JSON_FILE = "training_summary.json"
FIELDNAMES = ["id", "timestamp", "prompt", "response", "rating", "annotator"]


def main():
    print("\n🤖 AI Training Data Logger")
    print("==========================")
    while True:
        print("\nOptions:")
        print("  1. Log a new prompt/response pair")
        print("  2. View all logged entries")
        print("  3. Export summary to JSON")
        print("  4. Exit")

        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "1":
            log_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            export_summary()
        elif choice == "4":
            print("\nExiting. Dataset saved. 👋\n")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


def log_entry():
    """Log a new prompt/response pair with annotation rating."""
    print("\n--- Log New Entry ---")
    prompt = input("Prompt: ").strip()
    if not prompt:
        print("Prompt cannot be empty.")
        return

    response = input("Response: ").strip()
    if not response:
        print("Response cannot be empty.")
        return

    rating = get_rating()
    annotator = input("Annotator name (or press Enter for 'anonymous'): ").strip()
    if not annotator:
        annotator = "anonymous"

    entry_id = get_next_id()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    row = {
        "id": entry_id,
        "timestamp": timestamp,
        "prompt": prompt,
        "response": response,
        "rating": rating,
        "annotator": annotator,
    }

    write_to_csv(row)
    print(f"\n✅ Entry #{entry_id} logged successfully.")


def get_rating():
    """Prompt user for a valid rating between 1 and 5."""
    while True:
        try:
            rating = int(input("Rate this response (1 = poor, 5 = excellent): ").strip())
            if 1 <= rating <= 5:
                return rating
            print("Rating must be between 1 and 5.")
        except ValueError:
            print("Please enter a number.")


def write_to_csv(row):
    """Append a new entry to the CSV file."""
    try:
        with open(CSV_FILE, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            if f.tell() == 0:
                writer.writeheader()
            writer.writerow(row)
    except IOError as e:
        print(f"Error writing to file: {e}")


def get_next_id():
    """Return the next available entry ID based on existing rows."""
    entries = read_all_entries()
    return len(entries) + 1


def read_all_entries():
    """Read and return all entries from the CSV file."""
    entries = []
    try:
        with open(CSV_FILE, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                entries.append(row)
    except FileNotFoundError:
        pass
    except IOError as e:
        print(f"Error reading file: {e}")
    return entries


def view_entries():
    """Display all logged entries in a readable format."""
    entries = read_all_entries()
    if not entries:
        print("\nNo entries logged yet.")
        return

    print(f"\n--- All Entries ({len(entries)} total) ---")
    for entry in entries:
        print(f"\n[#{entry['id']}] {entry['timestamp']}")
        print(f"  Prompt    : {entry['prompt']}")
        print(f"  Response  : {entry['response']}")
        print(f"  Rating    : {'⭐' * int(entry['rating'])} ({entry['rating']}/5)")
        print(f"  Annotator : {entry['annotator']}")


def export_summary():
    """Export a summary of all entries to a JSON file."""
    entries = read_all_entries()
    if not entries:
        print("\nNo entries to export.")
        return

    ratings = [int(e["rating"]) for e in entries]
    avg_rating = round(sum(ratings) / len(ratings), 2)
    rating_dist = {str(i): ratings.count(i) for i in range(1, 6)}

    annotators = {}
    for e in entries:
        annotators[e["annotator"]] = annotators.get(e["annotator"], 0) + 1

    summary = {
        "export_timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_entries": len(entries),
        "average_rating": avg_rating,
        "rating_distribution": rating_dist,
        "annotators": annotators,
        "entries": entries,
    }

    try:
        with open(JSON_FILE, "w") as f:
            json.dump(summary, f, indent=4)
        print(f"\n✅ Summary exported to '{JSON_FILE}' ({len(entries)} entries, avg rating: {avg_rating}/5)")
    except IOError as e:
        print(f"Error writing JSON: {e}")


if __name__ == "__main__":
    main()