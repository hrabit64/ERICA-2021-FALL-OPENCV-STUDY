import Preprocess

def main():
    class_index = {0: 'with_mask', 1: 'without_mask', 2: 'mask_weared_incorrect'}
    preprocessor = Preprocess.Preprocessing('./data')

if __name__ == '__main__':
    main()