import random
import csv


class VotingResultsUtility:

    def generate_voting_results_csv(self, voters_amount, options):
        if voters_amount > 1 and options is not None and len(options) == 6:
            votes = []
            for voter in range(voters_amount):
                result = random.sample(options, len(options))
                votes.append(result)
            success = self.write_votes_to_csv(self, votes)
            return success
        else:
            return False

    def write_votes_to_csv(self, votes):
        if len(votes) > 1:
            # field names
            field_names = ['Voter', 'Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5', 'Option 6']

            # name of csv file
            filename = 'vote_results.csv'

            # writing to csv file
            with open (filename, 'w', newline='') as csvfile:
                # creating a csv writer object
                csvwriter = csv.writer(csvfile)

                # write fields to csv
                csvwriter.writerow(field_names)

                # write rows
                count = 0
                for value in votes:
                    row = [count, value[0], value[1], value[2], value[3], value[4], value[5]]
                    csvwriter.writerow(row)
                    count = count+1
            return True
        else:
            return False


if __name__ == '__main__':
    result = VotingResultsUtility.generate_voting_results_csv(VotingResultsUtility, 500, ['ice cream', 'cake', 'doughnut', 'cheesecake', 'cookies', 'macaroon'])
    print(result)
