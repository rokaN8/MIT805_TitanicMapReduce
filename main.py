from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import TextProtocol

class TitanicExampleMapReduce(MRJob):
    # Sorts the results
    SORT_VALUES = True
    # format for the output, can be JSON/Raw
    OUTPUT_PROTOCOL = TextProtocol

    def steps(self):

        # Step order
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer)
            # Can nest a number of steps for more complex jobs
            #,MRStep(mapper=self.mapper, reducer=self.reducer)
            ]

    def mapper(self, _, line):
        # splits the CSV file into array of elements 'a,b,c,d,e' becomes ['a','b','c','d','e']
        entry = line.split(',')
        # gets the first element in entry i.e. 'a' if not a number as in titanic.csv this is the first line and is 'Passenger' will not process this entry
        if entry[0].isdigit():
            # gets the gender 'male/female'
            gender = entry[4]
            # combines the gender with 'boarded-' into the key and sets a value of 1 for counting in the reducer
            yield "boarded-" + gender, 1

            # Tests for if the person survived or not
            if entry[1] == "1":
                # Combines 'survived-' and gender for second key, value pair
                yield "survived-" + gender, 1
        pass

    def reducer(self, key, values):
        # converts values to array of ones [1, 1, 1, ..., 1]
        array = [x for x in values]
        # counts the number of 1s/elements in the array
        totals = sum(array)
        # retuns the key 'boarded-male/female' or 'survived-male/female' with the sum
        yield (key, str(totals))

if __name__ == '__main__':
    TitanicExampleMapReduce.run()

