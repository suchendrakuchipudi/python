import csv
import json


class TestClass(object):

    def __init__(self, foo, bar, baz):
        self.foo = foo
        self.bar = bar
        self.baz = baz

    @staticmethod
    def fizz_buzz(digit_1, digit_2):
        for i in range(1, 100):
            if i % digit_1 == 0:
                if i % digit_2 == 0:
                    print 'fizzbuzz!'
                else:
                    print 'fizz!'
            elif i % digit_2 == 0:
                print 'buzz!'
            else:
                print i

    def my_first_method():
        j = []
        k=10
        for i in range(1, 100):
                j.append(i+k)
        print j

     def my_second_method():
        j = []
        k=10
        for i in range(1, 100):
                j.append(i-k)
        print j

    @staticmethod
    def json_to_csv(json_file_path, outfile_path):
        """Convert a file containing a list of flat JSON objects to a csv.
        What's a DictWriter, you say? Never heard of it!
        """
        with open(json_file_path) as f:
            data = json.load(f)
        fp = StringIO()
        with open(outfile_path, 'w') as fp:
            writer = csv.writer(fp)
            writer.writerow(data[0].keys())
            for item in data:
                writer.writerow(item.values())

if __name__ == '__main__':
    t = TestClass(1, 2, 3)
    TestClass.fizz_buzz(3, 5)