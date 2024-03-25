# Skończone
class Point:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
        self.point = (self.x,self.y)

    def __repr__(self) -> str:
        return f'({self.x},{self.y})'

    def get_point(self):
        return self.point
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def check_position(self, Q, R):
        L_PQ = self.length(Q)
        L_PR = self.length(R)
        if L_PQ < L_PR:
            return R
        else:
            return Q

    def length(self, other):
        x,y = self.point
        x1,y1 = other.point
        return ((x1 - x)**2 + (y1 - y)**2)**1/2



def Jarvis(list_points : list[Point], type = 1):
    
    P = None
    P_idx = None
    for idx, point in enumerate(list_points):
        x = point.get_x()
        if P is None:
            P = point
            P_idx = idx
        elif P.get_x() > x:
            P = point
            P_idx = idx
        elif P.get_x() == x:
            if P.get_y() > point.get_y():
                P = point
                P_idx = idx

    result_list = [P]
    n = len(list_points)
    i = P_idx + 1
    if i > n :
        i = 0
    Q = None
    while Q != result_list[0]:
        Q = list_points[i]
        
        
        x1,y1 = P.get_point()
        x2,y2 = Q.get_point()
        for R in list_points:
            if R != P and R != Q:
                x3,y3 = R.get_point()
                check = (y2 - y1)*(x3 - x2) - (y3 - y2)*(x2 - x1)
                if check > 0:
                    Q = R
                    x2,y2 = Q.get_point()
                elif check == 0:
                    if type == 2:
                        Q = P.check_position(Q,R)

                    

        if Q != result_list[0]:
            result_list.append(Q)
        P = Q

        i = list_points.index(P) + 1
        if i == n:
            i = 0
    return result_list

def print_sheath(list_sheath : list[Point]):
    txt = ''
    for idx, el in enumerate(list_sheath):
        if idx == 0:
            txt += f'{el}'
        else:
            txt += f' -> {el}'
    print(txt)

def main():
    lista = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]
    to_fun = []
    for el in lista:
        to_fun.append(Point(el[0], el[1]))

    print_sheath(Jarvis(to_fun))
    print_sheath(Jarvis(to_fun, 2))

main()