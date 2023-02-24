from getFiles import load_data
from prep import prep_data
from toGGS import update_ggs

def main():
    # Load data
    df = load_data()
    
    # Clean data
    df = prep_data(df)

    # up to ggs
    update_ggs(df)

if __name__ == '__main__':
    main()