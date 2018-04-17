import homework3
import unittest

class Checkunittest(unittest.TestCase):

    #Test for column names
    def testcolnamescheck(self):
        colnames = homework3.create_dataframe('class.db').columns
        self.assertEqual(sorted(colnames),sorted(['video_id','category_id','language']))

    #Test for number of rows
    def testnumrows(self):

        num_rows = homework3.create_dataframe('class.db').shape[0]
        self.assertEqual(num_rows,35950)

    #Check if video_id and Language is a key
    def testcheckkeys(self):

        df = homework3.create_dataframe('class.db')
        self.assertTrue(df.shape[0] == df.groupby(['video_id', 'language']).ngroups)

    #Check for valid path
    def testvalidpath(self):

        self.assertRaises(ValueError, homework3.create_dataframe,'class3.db')

suite = unittest.TestLoader().loadTestsFromTestCase(Checkunittest)
_ = unittest.TextTestRunner().run(suite)
