from collections import defaultdict

class data_structure_node():

    city_dic = defaultdict(list)

    def __init__(self,country="India",state=None,city=None,district=None,year=0,population=None):
        self.country = country.lower()
        self.state = state.lower()
        self.city = city.lower()
        self.district = district.lower()

        data_structure_node.city_dic[city].append([year,population])

    def get_city(self):
        max_inc = 0
        ans_city = None
        for city, city_list in data_structure_node.city_dic.items():

            #Year wise sorted list of population
            year_list = sorted(city_list, key=lambda x: x[0])
            
            for i in range(len(year_list)-1):
                if year_list[i+1][2]-year_list[i][2] > max_inc:
                    max_inc = year_list[i+1][2]-year_list[i][2]
                    ans_city = city

        return ans_city

n1 = data_structure_node("India","Harayan","Hisar","a",2000,1000)
n2 = data_structure_node("India","Harayan","Hisar","a",2001,2000)
n3 = data_structure_node("India","Harayan","Hisar","a",2002,4000)
n4 = data_structure_node("India","Harayan","Delhi","a",2000,1000)
n5 = data_structure_node("India","Harayan","Delhi","a",2001,4000)
n6 = data_structure_node("India","Harayan","Delhi","a",2002,40000)

print(n6.get_city())
