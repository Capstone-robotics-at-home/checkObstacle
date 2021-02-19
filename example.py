from polytope_obstacle import Obstacle
import numpy as np
import polytope as pt

ob = Obstacle()
ob.update_cart_postion([[0.1, 0],  [1.1, 0], [0.6, -0.5]])

ob.add_obstacle([[2.5, 0], [3, 0], [2, 2], [3, 2]])

# p1 = pt.qhull(np.asarray([[0, 0], [1, 0], [0, 1], [1, 1]]))
# ob.add_obstacle(pt.extreme(p1))
# p1 = p1.translation([1, 0.9])
# ob.add_obstacle(pt.extreme(p1))

ob.add_obstacle([[0, -1], [0, 3], [1, 2]])

print(ob.check_goal())
print(ob.check_crash())

ob.visualize()