class Solution:
    def calPoints(self, operations: List[str]) -> int:
        def invalid(record):
            record.pop()
            return record
        def doublescore(record,score):
            record.append(score*2)
            return record
        def addelethenadd(record):
            suma = record[-1] + record[-2]
            record.append(suma)
            return record
        record = []
        for i in range(len(operations)):
            if operations[i] == "+":
                record = addelethenadd(record)
            elif operations[i] == "C":
                record = invalid(record)
            elif operations[i] == "D":
                record = doublescore(record,record[-1])
            else:
                record.append(int(operations[i]))
        return sum(record)

            


        
        