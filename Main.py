import numpy as np
import matplotlib.pyplot as plt


# NO other imports are allowed

class Shape:
    '''
    DO NOT MODIFY THIS CLASS

    DO NOT ADD ANY NEW METHODS TO THIS CLASS
    '''

    def __init__(self):
        self.T_s = None
        self.T_r = None
        self.T_t = None

    def translate(self, dx, dy):
        '''
        Polygon and Circle class should use this function to calculate the translation
        '''
        self.T_t = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])

    def scale(self, sx, sy):
        '''
        Polygon and Circle class should use this function to calculate the scaling
        '''
        self.T_s = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])

    def rotate(self, deg):
        '''
        Polygon and Circle class should use this function to calculate the rotation
        '''
        rad = deg * (np.pi / 180)
        self.T_r = np.array([[np.cos(rad), np.sin(rad), 0], [-np.sin(rad), np.cos(rad), 0], [0, 0, 1]])

    def plot(self, x_dim, y_dim):
        '''
        Polygon and Circle class should use this function while plotting
        x_dim and y_dim should be such that both the figures are visible inside the plot
        '''
        x_dim, y_dim = 1.2 * x_dim, 1.2 * y_dim
        plt.plot((-x_dim, x_dim), [0, 0], 'k-')
        plt.plot([0, 0], (-y_dim, y_dim), 'k-')
        plt.xlim(-x_dim, x_dim)
        plt.ylim(-y_dim, y_dim)
        plt.grid()
        plt.show()


class Polygon(Shape):
    '''
    Object of class Polygon should be created when shape type is 'polygon'
    '''

    def __init__(self, A):
        '''
        Initializations here
        '''
        Shape.__init__(self)
        self.arr = np.transpose(A)
        self.prev_x = self.arr[0]
        self.prev_y = self.arr[1]

    def translate(self, dx, dy):
        '''
        Function to translate the polygon

        This function takes 2 arguments: dx and dy

        This function returns the final coordinates
        '''
        Shape.translate(self, dx, dy)
        wco = self.T_t

        self.prev_x = self.arr[0]
        self.prev_y = self.arr[1]

        z = np.dot(wco, self.arr)

        z[0] = np.round(z[0], decimals=2)
        z[1] = np.round(z[1], decimals=2)
        z[2] = np.round(z[2], decimals=2)

        self.arr[0] = z[0]
        self.arr[1] = z[1]
        self.arr[2] = z[2]

        return z[0], z[1]

    def scale(self, sx, sy):
        '''
        Function to scale the polygon

        This function takes 2 arguments: sx and sx

        This function returns the final coordinates
        '''
        Shape.scale(self, sx, sy)
        b = self.T_s

        self.prev_x = self.arr[0]
        self.prev_y = self.arr[1]

        r = np.dot(b, self.arr)
        m = np.array([sum(r[0]) / len(r[0]), sum(r[1]) / len(r[1])])
        n = np.array([sum(self.arr[0]) / len(self.arr[0]), sum(self.arr[1]) / len(self.arr[1])])
        dif = np.subtract(m, n)

        #        for ele in r[0]:
        #            for element in self.arr[0]:
        #               element = ele - dif[0]
        #                break

        #        for ele in r[1]:
        #            for element in self.arr[1]:
        #                element = ele - dif[1]
        #               break
        j = []
        k = []

        for ele in r[0]:
            j.append(ele - dif[0])

        for ele in r[1]:
            k.append(ele - dif[1])

        j = np.round(j, decimals=2)
        k = np.round(k, decimals=2)

        self.arr[0] = j
        self.arr[1] = k

        return j, k

    def rotate(self, deg, rx=0, ry=0):
        '''
        Function to rotate the polygon

        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)

        This function returns the final coordinates
        '''
        Shape.rotate(self, deg)
        w = self.T_r

        self.prev_x = self.arr[0]
        self.prev_y = self.arr[1]

        if rx != 0:
            if rx > 0:
                self.arr[0] = rx - self.arr[0]
            else:
                self.arr[1] = rx + self.arr[0]

        if ry != 0:
            if ry > 0:
                self.arr[1] = rx - self.arr[1]
            else:
                self.arr[1] = ry + self.arr[1]

        res = np.dot(w, self.arr)

        res[0] = np.round(res[0], decimals=2)
        res[1] = np.round(res[1], decimals=2)
        res[2] = np.round(res[2], decimals=2)

        self.arr[0] = np.array(res[0])
        self.arr[1] = np.array(res[1])
        self.arr[2] = np.array(res[2])

        if rx != 0:
            if rx > 0:
                res[0] = rx - res[0]
            else:
                res[1] = rx + res[0]

        if ry != 0:
            if ry > 0:
                res[1] = rx - res[1]
            else:
                res[1] = ry + res[1]

        return res[0], res[1]

    def plot(self):
        '''
        Function to plot the polygon

        This function should plot both the initial and the transformed polygon

        This function should use the parent's class plot method as well

        This function does not take any input

        This function does not return anything
        '''

        s1 = [self.prev_x[0], self.prev_x[-1]]

        s2 = [self.prev_y[0], self.prev_y[-1]]

        s3 = [self.arr[0][0], self.arr[0][-1]]

        s4 = [self.arr[1][0], self.arr[1][-1]]

        plt.plot(self.arr[0], self.arr[1], marker='o')
        plt.plot(self.prev_x, self.prev_y, linestyle='dashed', marker='o')
        plt.plot(s3, s4, marker='o')
        plt.plot(s1, s2, marker='o')
        dimx = self.prev_x[0]
        dimy = self.prev_y[0]

        for item in self.prev_x:
            if item > dimx:
                dimx = item

        for item in self.arr[0]:
            if item > dimx:
                dimx = item

        for item in self.prev_y:
            if item > dimy:
                dimy = item

        for item in self.arr[1]:
            if item > dimy:
                dimy = item

        Shape.plot(self, dimx, dimy)

        plt.plot()


class Circle(Shape):
    '''
    Object of class Circle should be created when shape type is 'circle'
    '''

    def __init__(self, x=0, y=0, radius=5):
        '''
        Initializations here
        '''
        Shape.__init__(self)
        self.radius = float(radius)
        self.prev_rad = self.radius

        self.ar = np.array([[x], [y], [1]])

        self.prev_x = self.ar[0]
        self.prev_y = self.ar[1]

    def translate(self, dx, dy):
        '''
        Function to translate the circle

        This function takes 2 arguments: dx and dy (dy is optional).

        This function returns the final coordinates and the radius
        '''
        Shape.translate(self, dx, dy)
        wco = self.T_t

        self.prev_x = self.ar[0]
        self.prev_y = self.ar[1]
        self.prev_rad = self.radius

        z = np.dot(wco, self.ar)

        z[0] = np.round(z[0], decimals=2)
        z[1] = np.round(z[1], decimals=2)
        z[2] = np.round(z[2], decimals=2)

        #        self.ar[0] = z[0]
        #        self.ar[1] = z[1]

        return float(z[0]), float(z[1]), float(self.radius)

    def scale(self, sx):
        '''
        Function to scale the circle

        This function takes 1 argument: sx

        This function returns the final coordinates and the radius
        :param **kwargs:
        '''
        Shape.scale(self, sx, sx)
        b = self.T_s
        c = np.array([[self.radius], [0], [0]])

        self.prev_x = self.ar[0]
        self.prev_y = self.ar[1]
        self.prev_rad = self.radius

        r = np.dot(b, c)
        self.radius = r[0]
        return float(self.ar[0]), float(self.ar[1]), float(r[0])

    def rotate(self, deg, rx=0, ry=0):
        '''
        Function to rotate the circle

        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)

        This function returns the final coordinates and the radius
        '''
        Shape.rotate(self, deg)
        w = self.T_r

        self.prev_x = self.ar[0]
        self.prev_y = self.ar[1]
        self.prev_rad = self.radius

        res = np.dot(w, self.ar)

        res[0] = np.round(res[0], decimals=2)
        res[1] = np.round(res[1], decimals=2)
        res[2] = np.round(res[2], decimals=2)

        self.ar[0] = float(res[0])
        self.ar[1] = float(res[1])

        if rx != 0:
            if rx > 0:
                res[0] = rx - res[0]
            else:
                res[1] = rx + res[0]

        if ry != 0:
            if ry > 0:
                res[1] = rx - res[1]
            else:
                res[1] = ry + res[1]

        #        self.ar[0] = float(res[0])
        #       self.ar[1] = float(res[1])

        return float(res[0]), float(res[1]), float(self.radius)

    def plot(self):
        '''
        Function to plot the circle

        This function should plot both the initial and the transformed circle

        This function should use the parent's class plot method as well

        This function does not take any input

        This function does not return anything
        '''

        figure, axes = plt.subplots()
        old_c = plt.Circle((self.prev_x, self.prev_y), self.prev_rad, linestyle='dashed', fill=False)
        new_c = plt.Circle((self.ar[0], self.ar[1]), self.radius, fill=False)
        axes.set_aspect(1)
        axes.add_patch(old_c)
        axes.add_patch(new_c)
        axes.add_artist(old_c)
        axes.add_artist(new_c)

        dimx = max(abs(self.prev_x + self.prev_rad), abs(self.ar[0] + self.radius))
        dimy = max(abs(self.prev_y + self.prev_rad), abs(self.ar[1] + self.radius))

        Shape.plot(self, dimx, dimy)


if __name__ == "__main__":
    '''
    Add menu here as mentioned in the sample output section of the assignment document.
    '''

    verbose = int(input("verbose? 1 to plot, 0 otherwise: "))
    a = []
    b = []

    tcase = int(input("Enter the number of test cases: "))
    sh = int(input("Enter type of shape(polygon/circle): "))
    if sh == 0:
        sides = int(input("Enter the number of sides: "))
        x = []
        y = []
        lst = []

        for i in range(1, sides + 1):
            xs = list(map(float, input(f"enter (x{i},y{i}):").split()))
            x = int(xs[0])
            a.append(x)
            y = int(xs[1])
            b.append(y)
            z = int(1)
            lst.append([x, y, z])

        A = np.array(lst)
        obj = Polygon(A)

        que = int(input("Enter the number of queries: "))

        print("Enter Query:")

        print("1) R deg rx (ry)")
        print("2) T dx (dy)")
        print("3) S sx (sy)")
        print("4) P")

        for i in range(0, que):
            qu = input()
            if qu == 'T':
                T_inp = list(map(float, input('Enter values :').split()))
                T_op = obj.translate(T_inp[0], T_inp[1])
                for value in a:
                    print(float(value), end=' ')
                for value in b:
                    print(float(value), end=' ')
                print()
                for item in T_op:
                    for value in item:
                        print(float(value), end=' ')

                a = T_op[0]
                b = T_op[1]

                print()

                if verbose == 1:
                    obj.plot()

            elif qu == 'R':
                R_inp = list(map(float, input('Enter values :').split()))
                if len(R_inp) == 1:
                    R_op = obj.rotate(R_inp[0], 0, 0)
                elif len(R_inp) == 2:
                    R_op = obj.rotate(R_inp[0], R_inp[1], 0)
                else:
                    R_op = obj.rotate(R_inp[0], R_inp[1], R_inp[2])

                for value in a:
                    print(float(value), end=' ')
                for value in b:
                    print(float(value), end=' ')
                print()
                for item in R_op:
                    for value in item:
                        print(float(value), end=' ')

                a = R_op[0]
                b = R_op[1]

                print()

                if verbose == 1:
                    obj.plot()

            elif qu == 'S':
                S_inp = list(map(float, input('Enter values :').split()))
                if len(S_inp) == 1:
                    S_op = obj.scale(S_inp[0], 0)
                else:
                    S_op = obj.scale(S_inp[0], S_inp[1])

                for value in a:
                    print(float(value), end=' ')
                for value in b:
                    print(float(value), end=' ')
                print()
                for item in S_op:
                    for value in item:
                        print(float(value), end=' ')
                print()

                a = S_op[0]
                b = S_op[1]

                if verbose == 1:
                    obj.plot()

            elif qu == 'P':
                obj.plot()

            else:
                quit(0)

    elif sh == 1:

        fg = list(map(float, input(f"enter coordinates of centre and radius (x,y,radius) :").split()))
        xc = fg[0]
        yc = fg[1]
        rc = fg[2]

        obj = Circle(xc, yc, rc)

        que = int(input("Enter the number of queries: "))

        print("Enter Query:")

        print("1) R deg rx (ry)")
        print("2) T dx (dy)")
        print("3) S sx (sy)")
        print("4) P")

        for i in range(0, que):
            qu = input()
            if qu == 'T':
                T_inp = list(map(float, input('Enter values :').split()))

                if len(T_inp) == 2:
                    T_op = obj.translate(T_inp[0], T_inp[1])
                elif len(T_inp) == 1:
                    T_op = obj.translate(T_inp[0], 0)
                else:
                    quit(0)

                print(xc, end=' ')
                print(yc, end=' ')
                print(rc, end=' ')
                print()

                for item in T_op:
                    print(float(item), end=' ')

                if verbose == 1:
                    obj.plot()

                xc = T_op[0]
                yc = T_op[1]
                rc = T_op[2]

                print()



            elif qu == 'R':
                R_inp = list(map(float, input('Enter values deg, rx, ry :').split()))

                if len(R_inp) == 1:
                    R_op = obj.rotate(R_inp[0], 0, 0)
                elif len(R_inp) == 2:
                    R_op = obj.rotate(R_inp[0], R_inp[1])
                elif len(R_inp) == 3:
                    R_op = obj.rotate(R_inp[0], R_inp[1], R_inp[2])
                else:
                    quit(0)

                print(xc, end=' ')
                print(yc, end=' ')
                print(rc, end=' ')
                print()

                for item in R_op:
                    print(item, end=' ')

                print()

                if verbose == 1:
                    obj.plot()

                xc = R_op[0]
                yc = R_op[1]
                rc = R_op[2]

            elif qu == 'S':
                S_inp = list(map(float, input('Enter value of sx :').split()))

                if len(S_inp) == 1:
                    S_op = obj.scale(S_inp[0])
                else:
                    quit(0)

                print(xc, end=' ')
                print(yc, end=' ')
                print(rc, end=' ')
                print()

                for item in S_op:
                    print(float(item), end=' ')

                print()

                if verbose == 1:
                    obj.plot()

                xc = S_op[0]
                yc = S_op[1]
                rc = S_op[2]

            elif qu == 'P':
                obj.plot()

            else:
                quit(0)

    else:
        quit(0)
