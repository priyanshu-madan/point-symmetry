def take_input():
    input_points = []
    options = {"Square" : [(0.0, 0.0), (1.0, 1.0), (0.0, 1.0), (1.0, 0.0)],
    "Rectangle" : [(0,0),(0,4),(6,4),(6,0)],
    "Rectangle_2" : [(-4,-3),(-4,1), (3,1), (3,-3)],
    "Twisted_rectangle" : [(-3,5),(3,7), (0,-4), (6,-2)],
    "Isoceles_triangle" : [(0,0),(8,0),(4,10)],
    "Equilateral_triangle" : [(1.0,1.0),(2.0,1.0),(1.5,1.8660254037844386)],
    "Kite" : [(-1, 5), (3, 1), (-1, -1), (-5, 1)],
    "Parallelogram" : [(-2,2),(-4,-2),(2,-2),(4,2)],
    "Isoceles_trapezoid" : [(-2,2),(2,2),(6,0),(-6,0)],
    "Star" : [(4,4),(0,4),(3.5,1),(2,6),(0.5,1)],
    "Parabola" : [(-2,-1),(-3,1),(-4,3),(2,-1),(3,1),(4,3)],
    "Random symmetrical points (0ver 100 points)": [(665,926),(836,582),(968,65),(83,6),(303,392),(786,678),(769,356),(125,92),(216,188),(873,988),(940,316),(995,461),(185,478),(500,353),(769,710),(995,68),(273,440),(800,726),(961,628),(678,946),(306,50),(336,90),(249,39),(873,628),(984,30),(43,815),(729,824),(842,107),(222,541),(181,122),(920,349),(894,899),(-665,926),(-836,582),(-968,65),(-83,6),(-303,392),(-786,678),(-769,356),(-125,92),(-216,188),(-873,988),(-940,316),(-995,461),(-185,478),(-500,353),(-769,710),(-995,68),(-273,440),(-800,726),(-961,628),(-678,946),(-306,50),(-336,90),(-249,39),(-873,628),(-984,30),(-43,815),(-729,824),(-842,107),(-222,541),(-181,122),(-920,349),(-894,899),(-665,-926),(-836,-582),(-968,-65),(-83,-6),(-303,-392),(-786,-678),(-769,-356),(-125,-92),(-216,-188),(-873,-988),(-940,-316),(-995,-461),(-185,-478),(-500,-353),(-769,-710),(-995,-68),(-273,-440),(-800,-726),(-961,-628),(-678,-946),(-306,-50),(-336,-90),(-249,-39),(-873,-628),(-984,-30),(-43,-815),(-729,-824),(-842,-107),(-222,-541),(-181,-122),(-920,-349),(-894,-899),(665,-926),(836,-582),(968,-65),(83,-6),(303,-392),(786,-678),(769,-356),(125,-92),(216,-188),(873,-988),(940,-316),(995,-461),(185,-478),(500,-353),(769,-710),(995,-68),(273,-440),(800,-726),(961,-628),(678,-946),(306,-50),(336,-90),(249,-39),(873,-628),(984,-30),(43,-815),(729,-824),(842,-107),(222,-541),(181,-122),(920,-349),(894,-899)]
}

    # Print out your options
    keys = list(options.keys())
    for i in range(len(options)):
        print(str(i+1) + ":", keys[i])

    inp = int(input("Enter a number: "))
    if inp in range(1, len(keys)+1):
        input_points = options[keys[inp-1]]
    else:
        print("Invalid input!")
        return []

    return input_points