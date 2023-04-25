import subprocess

def main():
    
    subprocess.run(["python", "raw_data.py"])
    subprocess.run(["python", "preprocessing.py"])

if __name__ == '__main__':
    main()