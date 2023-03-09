import csv

if __name__ == '__main__':
    header = ['# nodes',
              '# corrupted',
              'total transactions(TXs)',
              'total delay(s)',
              'average delay(s/round)',
              'average throughout(TXs/s)',
              '1% longest delay(s)',
              '1% shortest delay(s)',
              '1% least throughout(TXs/s)',
              '1% largest throughout(TXs/s)']
    data_set = []
    node_set = [16, 25, 36, 49, 64]     # the number of nodes emerged in the consensus
    corrupted_set = [5, 8, 11, 16, 21]  # the number of corrupted nodes
    idx = 0
    num_round = 100
    batch_size = 5000
    with open('../log/consensus-node-0.log') as f:
        print('loading data...')
        data = f.readlines()
        round_throughout = []
        round_delay = []
        single_data = None
        for line in data:
            words = line.split(' ')
            if words[2] == "dumbo.py" and words[8] == "Delivers":
                single_data = float(words[16])
            elif words[2] == "dumbo.py" and words[6] == "ACS":
                round_delay.append(float(words[12]))
                round_throughout.append(single_data / float(words[12]))
            elif words[2] == "dumbo.py" and words[8] == "breaks":
                print(f'==========\ntotal: {words[16]}TXs, total delay: {words[10]}sec,'
                      f' average throughout: {float(words[16])/float(words[10])}TXs/sec')
                length = len(round_throughout)
                round_delay.sort()
                round_throughout.sort()
                print(f'1% longest delay: {sum(round_delay[length-6:])/6} sec, '
                      f'1% shortest delay: {sum(round_delay[:5])/6} sec')
                print(f'1% least throughout: {sum(round_throughout[:5])/6} TXs/sec, '
                      f'1% largest throughout: {sum(round_throughout[length-6:])/6} TXs/sec')
                data_set.append({
                    '# nodes': node_set[idx],
                    '# corrupted': corrupted_set[idx],
                    'total transactions(TXs)': float(words[16]),
                    'total delay(s)': float(words[10]),
                    'average delay(s/round)': float(words[10])/num_round,
                    'average throughout(TXs/s)': float(words[16])/float(words[10]),
                    '1% longest delay(s)': sum(round_delay[length-6:])/6,
                    '1% shortest delay(s)': sum(round_delay[:5])/6,
                    '1% least throughout(TXs/s)': sum(round_throughout[:5])/6,
                    '1% largest throughout(TXs/s)': sum(round_throughout[length-6:])/6
                })
                round_throughout = []
                round_delay = []
                idx += 1

    print(data_set)
    with open('data_opt_predicate.csv', 'a', newline='', encoding='utf-8') as out:
        writer = csv.DictWriter(out, fieldnames=header)
        writer.writeheader()
        writer.writerows(data_set)
