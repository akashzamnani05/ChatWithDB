import gdown

def down():
    print("downloading.........")
    gdown.download(f"'https://drive.google.com/file/d/1uIWd4DvU5AIPh0QuX_YPpl9uq33P5f5o/view?usp=sharing'", "mistral-7b-instruct-v0.2.Q3_K_M.gguf", quiet=False)