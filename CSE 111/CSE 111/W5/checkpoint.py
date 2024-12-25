def main():
    
    provinces = read_provinces('provinces.txt')
    print(provinces)
    provinces.pop(0)
    provinces.pop()
    
    while 'AB' in provinces:
        index = provinces.index('AB')
        provinces[index] = 'Alberta'
        
        ab_count = provinces.count('Alberta')
        print(f'{ab_count} instances of alberta found file.')
    provinces = read_provinces('provinces.txt')
    
def read_provinces(filename):
    provinces = []
    with open(filename, 'rt') as provinces_file:
        for line in provinces_file:
            clean_line = line.strip()
            provinces.append(clean_line)
        
    return provinces


if __name__ == '__main__':
    main ()