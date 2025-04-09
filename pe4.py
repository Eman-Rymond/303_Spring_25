import wikipedia
import time
from concurrent.futures import ThreadPoolExecutor

# PART A: Sequential download
print("Starting sequential download...")

start_time_seq = time.perf_counter()

# Step 1: Search for topics related to "generative artificial intelligence"
topics = wikipedia.search("generative artificial intelligence")

# Step 2: Go through each topic one at a time
for topic in topics:
    try:
        # Get the page for this topic
        page = wikipedia.page(topic, auto_suggest=False)

        # Get the title of the page
        title = page.title

        # Get the references (list of links)
        references = page.references

        # Create a text file using the title as filename
        filename = title + ".txt"
        with open(filename, "w", encoding="utf-8") as f:
            # Write each reference on its own line
            for ref in references:
                f.write(ref + "\n")

    except Exception as e:
        print("There was an error with topic:", topic)
        print("Error:", e)

end_time_seq = time.perf_counter()
print("Sequential download finished in", round(end_time_seq - start_time_seq, 2), "seconds")


# PART B: Concurrent download using threads
print("\nStarting concurrent download...")

def wiki_dl_and_save(topic):
    try:
        page = wikipedia.page(topic, auto_suggest=False)
        title = page.title
        references = page.references
        filename = title + ".txt"
        with open(filename, "w", encoding="utf-8") as f:
            for ref in references:
                f.write(ref + "\n")
    except Exception as e:
        print("There was an error with topic:", topic)
        print("Error:", e)

start_time_conc = time.perf_counter()

# Use ThreadPoolExecutor to run multiple downloads at once
with ThreadPoolExecutor() as executor:
    executor.map(wiki_dl_and_save, topics)

end_time_conc = time.perf_counter()
print("Concurrent download finished in", round(end_time_conc - start_time_conc, 2), "seconds")
