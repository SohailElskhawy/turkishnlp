import pickle, os, urllib.request

save_dir = os.path.join(os.environ.get('APPDATA', os.path.expanduser('~')), 'TRnlpdata')
os.makedirs(save_dir, exist_ok=True)

print("Downloading official Turkish word list from TDK dataset...")
url = "https://raw.githubusercontent.com/mertemin/turkish-word-list/master/words.txt"
urllib.request.urlretrieve(url, save_dir + "/words_raw.txt")

with open(save_dir + "/words_raw.txt", encoding="utf-8") as f:
    words = set(line.strip().lower() for line in f if line.strip())

print(f"Loaded {len(words)} words.")

with open(save_dir + "/words.pkl", "wb") as f:
    pickle.dump(words, f)

counted = {w: 1 for w in words}
with open(save_dir + "/words_counted.pkl", "wb") as f:
    pickle.dump(counted, f)

words_list = sorted(words)
with open(save_dir + "/words_alt.pkl", "wb") as f:
    pickle.dump(words_list, f)

print("Done. All .pkl files ready. Run pytest now.")

print("Done. Run pytest now.")