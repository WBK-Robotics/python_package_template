import os
import unittest

import numpy as np
from python_package import particle_optimizer


class TestExampleCode(unittest.TestCase):

    def test_particle_optimizer(self):
        def banana_function(x):
            return (1-x[0])**2+100*(x[1]-x[0]**2)**2

        def quadratic_function(x):
            return (x[2]-6)**2

        # Create particles
        n_particles = 20
        np.random.seed(100)
        start_position = np.random.rand(3, n_particles) * 5
        start_velocities = np.random.randn(3, n_particles) * 0.1

        simple_value, _ = particle_optimizer(
            quadratic_function, start_position, start_velocities, 5000)
        banana_value, _ = particle_optimizer(
            banana_function, start_position[:2], start_velocities[:2], 5000)

        self.assertTrue(simple_value[2] == 6)
        self.assertTrue((banana_value-np.ones(2) <= 0.001).all())



if __name__ == '__main__':
    unittest.main()
