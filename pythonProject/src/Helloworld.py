import numpy as np

class TestNumpy(TestCase):
    def testReadFile(self):
        file_name = './demo.csv'
        end_prise, volume = np.loadtxt(
            file_name=file_name,
            delimiter=",",
            usecols=(2, 6),
            unpack=True
        )
        print(end_prise)
        print(volume)