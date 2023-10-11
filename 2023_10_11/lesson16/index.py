import dataSource

def main():
    names = dataSource.cityName()
    city =  dataSource.info(name='澎湖縣望安鄉')
    print(names)
    print(city)


if __name__ == "__main__":
    main()